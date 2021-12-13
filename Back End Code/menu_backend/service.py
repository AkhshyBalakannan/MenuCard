'''Service file contains helper function'''
import datetime
import jwt
from flask import json, make_response, jsonify
from menu_backend.models.user import User, db
from menu_backend.models.meal import Meal
from menu_backend import bcrypt, app

# pylint disable:no-member

def user_details(current_user):
    '''User details from database'''
    user = {}
    user['username'] = current_user.username
    user['email'] = current_user.email
    user['admin'] = current_user.admin
    user['public_id'] = current_user.public_id

    return user

def promote_user(public_id):
    '''To promote user to admin Role'''
    user = User.query.filter_by(public_id=public_id).first()
    user.admin = True
    db.session.commit()


def generate_token(auth):
    '''To generate token used as for login access'''
    if not auth or not auth['username'] or not auth['password']:
        return make_response('Could not verify', 401)

    user = User.query.filter_by(username=auth['username']).first()

    if not user:
        return make_response('Could not verify', 401)

    if bcrypt.check_password_hash(user.password, auth['password']):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(days=365)}, app.config['SECRET_KEY'])
        if user.admin:
            return jsonify({'token':token, 'admin': 'true'})
        return jsonify({'token': token})

    return make_response('Could not verify', 401)


def menu_card():
    '''Menucard setup with meals
     corresponding foods to meal
    '''
    datas = Meal.query.all()
    output = []

    for data in datas:
        meal_data = {}
        meal_data['meal_name'] = data.meal_name
        meal_data['public_id'] = data.public_id
        meal_data['meal_food'] = {}

        for index in range(len(data.meal_food)):
            meal_data['meal_food'][index+1] = data.meal_food[index].food_name
        
        output.append(meal_data)
    
    return output

def meal_list():
    '''List of Meal'''
    datas = Meal.query.all()
    output = []

    for data in datas:
        meal_data = {}
        meal_data['meal_name'] = data.meal_name
        meal_data['public_id'] = data.public_id
        output.append(meal_data)

    return output