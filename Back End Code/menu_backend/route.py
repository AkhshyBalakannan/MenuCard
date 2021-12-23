'''Common Routes'''
from flask import request, jsonify
from flask.helpers import make_response
from menu_backend import app, db
from menu_backend.models.food import create_relation
from menu_backend.decorators import token_required, admin_only
from flask_cors import CORS, cross_origin

from menu_backend.service import get_menu_data

# pylint: disable=unused-argument


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


@app.route('/link', methods=['GET','PATCH'])
@token_required
@admin_only
def relation(current_user):
    '''Create Relation
    Data must be given with
    food_public_id, meal_public_id
    '''
    if(request.method == 'GET'):
        menu_data = get_menu_data();
        return jsonify(menu_data)
    data = request.get_json()
    relation_instance = create_relation(data)
    return f'created relation {relation_instance}'
