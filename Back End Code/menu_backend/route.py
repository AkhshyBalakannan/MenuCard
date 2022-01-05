'''Common Routes'''
from flask import request, jsonify
from flask.helpers import make_response
from flask_cors.decorator import cross_origin
from menu_backend import app, db
from menu_backend.models.food import create_relation, delete_relation
from menu_backend.decorators import token_required, admin_only

from menu_backend.service import get_menu_data

# pylint: disable=unused-argument


@app.route('/')
def testing():
    '''Testing'''
    return 'Hello from Menucard'


@app.route('/db-create')
def create_all():
    '''Create database'''
    db.create_all()
    return 'Database has been created'


@app.route('/db-drop', methods=['DELETE'])
@token_required
@admin_only
def drop_all(current_user):
    '''Drop database'''
    db.drop_all()
    return 'Database has been dropped'


@app.route('/link', methods=['GET', 'PATCH'])
@token_required
@admin_only
def make_relation(current_user):
    '''Create Relation
    Data must be given with
    food_public_id, meal_public_id
    '''
    if(request.method == 'GET'):
        menu_data = get_menu_data()
        return jsonify(menu_data)
    data = request.get_json()
    create_relation(data)
    return jsonify(message='Created Relation')


@app.route('/unlink', methods=['PATCH'])
@token_required
@admin_only
def undo_relation(current_user):
    '''Delete Relation
    Data must be given with
    food_public_id, meal_public_id
    '''
    data = request.get_json()
    delete_relation(data)
    return jsonify(message='Deleted Relation')
