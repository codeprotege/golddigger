import unittest
import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from run import create_app, db
from app.models.user import User
from app.models.gold import Gold

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_class='config.settings.TestingConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        response = self.client.post('/api/auth/register', data=json.dumps({
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        # First, register a user
        self.client.post('/api/auth/register', data=json.dumps({
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        # Then, login
        response = self.client.post('/api/auth/login', data=json.dumps({
            'username': 'testuser',
            'password': 'password'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

    def test_buy_sell(self):
        # Register and login to get a token
        self.client.post('/api/auth/register', data=json.dumps({
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        login_response = self.client.post('/api/auth/login', data=json.dumps({
            'username': 'testuser',
            'password': 'password'
        }), content_type='application/json')
        token = login_response.get_json()['token']

        gold = Gold(name='Gold', symbol='XAU')
        db.session.add(gold)
        db.session.commit()

        # Test buying
        response = self.client.post('/api/trading/buy', headers={
            'x-access-token': token
        }, data=json.dumps({
            'gold_id': 1,
            'amount': 1,
            'price': 1800
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # Test selling
        response = self.client.post('/api/trading/sell', headers={
            'x-access-token': token
        }, data=json.dumps({
            'gold_id': 1,
            'amount': 1,
            'price': 1800
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
