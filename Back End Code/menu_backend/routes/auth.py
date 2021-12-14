'''Auth Route'''
from flask import request, Blueprint, jsonify
from flask_cors.decorator import cross_origin
from menu_backend.models.user import User, create_user, update_user, delete_user
from menu_backend.decorators import token_required, admin_only
from menu_backend.service import promote_user, generate_token, user_details

auth_routes = Blueprint("auth_routes", __name__)

# pylint: disable=unused-argument


@auth_routes.route('/all', methods=['GET'])
@token_required
@admin_only
def all_user(current_user):
    '''Get All User'''
    datas = User.query.all()
    output = []

    for data in datas:
        user_data = {}
        user_data['public_id'] = data.public_id
        user_data['username'] = data.username
        user_data['email'] = data.email
        user_data['admin'] = data.admin
        output.append(user_data)

    return jsonify(output)


@auth_routes.route('/new', methods=['POST'])
@cross_origin()
def register_user():
    '''Post Register User'''
    data = request.get_json()
    auth = create_user(data)
    return jsonify({'message': "account created successfully"})


@auth_routes.route('/login', methods=['POST'])
@cross_origin()
def login():
    '''Login function'''
    auth = request.get_json()
    res = generate_token(auth)
    return res

@auth_routes.route('/profile', methods=['GET'])
@token_required
def user_profile(current_user):
    '''User Profile'''
    data = user_details(current_user)
    return jsonify(data)

@auth_routes.route('/update', methods=['PATCH'])
@token_required
@cross_origin()
def user_updation(current_user):
    '''Patch Update User'''
    data = request.get_json()
    update_user(data, current_user)
    return jsonify({'message': 'Updated user!'})


@auth_routes.route('/promote/<public_id>', methods=['PUT'])
@token_required
@admin_only
@cross_origin()
def user_promotion(current_user, public_id):
    '''Put Promote User'''
    promote_user(public_id)
    return jsonify({'message': 'Promoted user!'})


@auth_routes.route('/delete/<public_id>', methods=['DELETE'])
@token_required
@admin_only
@cross_origin()
def user_deletion(current_user, public_id):
    '''Delete - Delete User'''
    delete_user(public_id)
    return jsonify({'message': 'Deleted user!'})
