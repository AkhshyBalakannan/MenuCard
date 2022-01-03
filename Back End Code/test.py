import unittest

from menu_backend import app
from flask import json


def convert_into_json(data):
    # converting into dict
    return json.loads(data.data.decode("utf-8").replace("'", '"'))


def login(client, username, password):
    """login Function called by other testing Function."""
    return client.post('/user/login', data=json.dumps(dict(
        username=username,
        password=password
    )), content_type='application/json', follow_redirects=True)


def create_food(client, token):
    food_response = client.post('/food/create',
                                data=json.dumps(
                                    dict(food_name='testfood')),
                                headers={'Authorization': token}, content_type='application/json')
    food_res = convert_into_json(food_response)
    if ("Created Food" == food_res['message']):
        return food_res['public_id']


def create_meal(client, token):
    meal_response = client.post('/meal/create',
                                data=json.dumps(
                                    dict(meal_name='testmeal')),
                                headers={'Authorization': token}, content_type='application/json')
    meal_res = convert_into_json(meal_response)
    if("Created Meal" == meal_res['message']):
        return meal_res['public_id']


def delete_food_meal(client, token, food_id, meal_id):
    client.delete(f'food/delete/{food_id}', headers={
        'Authorization': token}, content_type='application/json')
    client.delete(f'meal/delete/{meal_id}', headers={
        'Authorization': token}, content_type='application/json')


class FlaskTest(unittest.TestCase):

    def test_base_route(self):
        """Start with a blank Response."""
        client = app.test_client(self)
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello from Menucard')

    def test_login(self):
        """Make sure login route works."""
        client = app.test_client(self)
        username = app.config["USERNAME"]  # username from app
        password = app.config["PASSWORD"]  # password from app

        response = login(client, username, password)  # calling function
        res = convert_into_json(response)  # converting into dict
        self.assertTrue(res['token'])

        response = login(client, f"{username}x", password)
        self.assertEqual(404, response.status_code)
        self.assertEqual(response.data, b'User Not Found in database')

        response = login(client, username, f'{password}x')
        self.assertEqual(401, response.status_code)
        self.assertEqual(b'Could not verify', response.data)

        # login with no user data
        response = client.post('/user/login', data=json.dumps(dict()),
                               content_type='application/json', follow_redirects=True)
        self.assertEqual(b'Please Provide User Details', response.data)

    def test_create_and_delete_user(self):
        """Create User account
        Delete User Account"""
        client = app.test_client(self)

        username = "testuser_test6"
        email = "testuser_test6@gmail.com"
        password = "password"

        # Create New User
        response = client.post('/user/new', data=json.dumps(dict(
            username=username,
            password=password,
            email=email
        )), content_type='application/json', follow_redirects=True)

        res = convert_into_json(response)
        self.assertEqual('Account created successfully', res['message'])

        public_id = res['public_id']

        # login to get token
        response = login(client, username, password)
        res = convert_into_json(response)
        token = res['token']

        # Delete New User created
        response = client.delete(
            f'/user/delete/{public_id}', content_type='application/json', headers={'Authorization': token}, follow_redirects=True)
        res = convert_into_json(response)

        self.assertEqual('Deleted user!', res['message'])

        # Create New User with no data
        response = client.post('/user/new', data=json.dumps(dict(
        )), content_type='application/json', follow_redirects=True)

        res = convert_into_json(response)
        self.assertEqual('Please Provide User Details', res['message'])

        # Create New User with no email Data
        response = client.post('/user/new', data=json.dumps(dict(
            username=username, password=password, email='')), content_type='application/json', follow_redirects=True)

        res = convert_into_json(response)
        self.assertEqual('Please Provide User Details', res['message'])

    def test_food_crud(self):
        '''Create Read Update Delete Food Model'''
        client = app.test_client(self)
        username = app.config["USERNAME"]  # username from app
        password = app.config["PASSWORD"]  # password from app

        login_response = login(client, username, password)  # calling function
        res = convert_into_json(login_response)

        token = res['token']
        food_response = client.post('/food/create',
                                    data=json.dumps(
                                        dict(food_name='testfood')),
                                    headers={'Authorization': token}, content_type='application/json')
        food_res = convert_into_json(food_response)
        self.assertEqual("Created Food", food_res['message'])
        food_id = food_res['public_id']

        food_response = client.patch('/food/update', data=json.dumps(dict(
            public_id=food_id, food_name='Updated_food')), headers={'Authorization': token}, content_type='application/json')
        food_res = convert_into_json(food_response)
        self.assertEqual("Updated Food", food_res['message'])

        food_response = client.delete(f'food/delete/{food_id}', headers={
                                      'Authorization': token}, content_type='application/json')

    def test_meal_crud(self):
        '''Create Read Update Delete Meal'''
        client = app.test_client(self)
        username = app.config["USERNAME"]  # username from app
        password = app.config["PASSWORD"]  # password from app

        login_response = login(client, username, password)  # calling function
        res = convert_into_json(login_response)

        token = res['token']
        meal_response = client.post('/meal/create',
                                    data=json.dumps(
                                        dict(meal_name='testmeal')),
                                    headers={'Authorization': token}, content_type='application/json')
        meal_res = convert_into_json(meal_response)
        self.assertEqual("Created Meal", meal_res['message'])
        meal_id = meal_res['public_id']

        meal_response = client.patch('/meal/update', data=json.dumps(dict(
            public_id=meal_id, meal_name='Updated_meal')), headers={'Authorization': token}, content_type='application/json')
        meal_res = convert_into_json(meal_response)
        self.assertEqual("Updated Meal", meal_res['message'])

        meal_response = client.delete(f'meal/delete/{meal_id}', headers={
                                      'Authorization': token}, content_type='application/json')

    def test_relation_crud(self):
        '''Create Read Update Delete Relation'''
        client = app.test_client(self)
        username = app.config["USERNAME"]  # username from app
        password = app.config["PASSWORD"]  # password from app

        login_response = login(client, username, password)  # calling function
        res = convert_into_json(login_response)

        token = res['token']

        food_id = create_food(client, token)
        meal_id = create_meal(client, token)

        relation_response = client.patch('/link',
                                         data=json.dumps(
                                             dict(food_public_id=food_id, meal_public_id=meal_id)),
                                         headers={'Authorization': token}, content_type='application/json')
        relation_res = convert_into_json(relation_response)

        self.assertEqual("Created Relation", relation_res['message'])

        relation_response = client.patch('/unlink',
                                         data=json.dumps(
                                             dict(food_public_id=food_id, meal_public_id=meal_id)),
                                         headers={'Authorization': token}, content_type='application/json')
        relation_res = convert_into_json(relation_response)

        self.assertEqual("Deleted Relation", relation_res['message'])

        delete_food_meal(client,token, food_id, meal_id)


if __name__ == "__main__":
    unittest.main()
