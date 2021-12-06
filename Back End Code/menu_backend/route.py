'''Common Routes'''
from flask import request, Response
from menu_backend import app, db
from menu_backend.models.food import create_relation
from menu_backend.decorators import token_required, admin_only

# pylint: disable=unused-argument


@app.route('/testing', methods=['POST'])
def testing_front_end():
    '''Front End testing'''
    print('dskhjfdshjjkfs')
    print(request)
    print(request.body)
    print(request.body.data)
    resp = Response("Foo bar baz")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

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


@app.route('/link', methods=['LINK'])
@token_required
@admin_only
def relation(current_user):
    '''Create Relation
    Data must be given with
    food_public_id, meal_public_id
    '''
    data = request.get_json()
    relation_instance = create_relation(data)
    return f'created relation {relation_instance}'
