'''Service file contains helper function'''
import datetime
import jwt
from flask import json, make_response, jsonify
from menu_backend.models.user import User, db, update_user
from menu_backend.models.meal import Meal
from menu_backend.models.food import Food
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
    if not auth:
        return make_response('Please Provide User Details')

    if not auth['username'] or not auth['password']:
        return make_response('Could not verify')

    user = User.query.filter_by(username=auth['username']).first()

    if not user:
        return make_response('User Not Found in database')

    if bcrypt.check_password_hash(user.password, auth['password']):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(days=365)}, app.config['SECRET_KEY'])
        if user.admin:
            return jsonify({'token':token, 'admin': 'true'})
        return jsonify({'token': token})

    return make_response('Could not verify')


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
            meal_data['meal_food'][index+1] = {}
            meal_data['meal_food'][index+1]['food_name'] = data.meal_food[index].food_name
            meal_data['meal_food'][index+1]['public_id'] = data.meal_food[index].public_id
        
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

def food_list():
    '''List of Food'''
    datas = Food.query.all()
    output = []

    for data in datas:
        food_data = {}
        food_data['food_name'] = data.food_name
        food_data['public_id'] = data.public_id
        output.append(food_data)

    return output


def get_menu_data():
    '''list of Meal and food'''
    meal_data = meal_list()
    food_data = food_list()
    relation_data = menu_card()

    return ({'meal_data':meal_data, 'food_data': food_data, 'relation_data':relation_data})

def check_user_and_update(data, current_user):
    if bcrypt.check_password_hash(current_user.password, data['password']):
        update_user(data, current_user)
        return True
    return False
