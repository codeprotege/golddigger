import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from run import create_app, db
from app.models.user import User
from app.models.gold import Gold
from app.models.transaction import Transaction
from app.models.price import Price

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_class='config.settings.TestingConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password'))
        self.assertFalse(user.check_password('wrongpassword'))

    def test_gold_model(self):
        gold = Gold(name='Gold', symbol='XAU')
        self.assertEqual(gold.name, 'Gold')
        self.assertEqual(gold.symbol, 'XAU')

    def test_transaction_model(self):
        transaction = Transaction(user_id=1, gold_id=1, transaction_type='buy', amount=10, price=1800)
        self.assertEqual(transaction.transaction_type, 'buy')
        self.assertEqual(transaction.amount, 10)

    def test_price_model(self):
        price = Price(gold_id=1, price=1805.50)
        self.assertEqual(price.gold_id, 1)
        self.assertEqual(price.price, 1805.50)

if __name__ == '__main__':
    unittest.main()
