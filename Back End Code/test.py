import unittest

from menu_backend import app
from flask import json


def login(client, username, password):
    """login Function called by other testing Function."""
    return client.post('/user/login', data=json.dumps(dict(
        username=username,
        password=password
    )), content_type='application/json', follow_redirects=True)


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
        username = app.config["USERNAME"]   #username from app
        password = app.config["PASSWORD"]   #password from app

        response = login(client, username, password) #calling function
        res = json.loads(response.data.decode("utf-8").replace("'", '"')) #converting into dict
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

        username="testuser_test6"
        email="testuser_test6@gmail.com"
        password="password"

        # Create New User
        response = client.post('/user/new', data=json.dumps(dict(
            username=username,
            password=password,
            email=email
        )), content_type='application/json', follow_redirects=True)
        
        res = json.loads(response.data.decode("utf-8").replace("'", '"'))
        self.assertEqual('Account created successfully', res['message'])

        public_id = res['public_id']
        
        #login to get token
        response = login(client, username, password)
        res = json.loads(response.data.decode("utf-8").replace("'", '"'))
        token = res['token']

        #Delete New User created
        response = client.delete(
            f'/user/delete/{public_id}', content_type='application/json', headers={'Authorization':token}, follow_redirects=True)
        res = json.loads(response.data.decode("utf-8").replace("'", '"'))
        
        self.assertEqual('Deleted user!', res['message'])

        #Create New User with no data
        response = client.post('/user/new', data=json.dumps(dict(
        )), content_type='application/json', follow_redirects=True)
        
        res = json.loads(response.data.decode("utf-8").replace("'", '"'))
        self.assertEqual('Please Provide User Details', res['message'])

        #Create New User with no email Data
        response = client.post('/user/new', data=json.dumps(dict(
        username=username, password=password, email='')), content_type='application/json', follow_redirects=True)
        
        res = json.loads(response.data.decode("utf-8").replace("'", '"'))
        self.assertEqual('Please Provide User Details', res['message'])


if __name__ == "__main__":
    unittest.main()
