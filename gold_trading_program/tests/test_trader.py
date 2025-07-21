import unittest
from unittest.mock import Mock
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.trading.trader import Trader

class TestTrader(unittest.TestCase):
    """
    Unit tests for the Trader class.
    """

    def setUp(self):
        """
        Set up a mock brokerage and a Trader instance.
        """
        self.brokerage = Mock()
        self.trader = Trader(self.brokerage)

    def test_place_buy_order_success(self):
        """
        Test that place_order correctly places a buy order and updates the position.
        """
        self.brokerage.submit_order.return_value = True
        self.trader.place_order("XAUUSD", 1, "buy")
        self.brokerage.submit_order.assert_called_with(symbol="XAUUSD", quantity=1, order_type="buy")
        self.assertEqual(self.trader.get_position("XAUUSD"), 1)

    def test_place_sell_order_success(self):
        """
        Test that place_order correctly places a sell order and updates the position.
        """
        self.brokerage.submit_order.return_value = True
        self.trader.place_order("XAUUSD", 1, "buy")
        self.trader.place_order("XAUUSD", 0.5, "sell")
        self.assertEqual(self.trader.get_position("XAUUSD"), 0.5)

    def test_place_order_failure(self):
        """
        Test that the position is not updated when an order fails.
        """
        self.brokerage.submit_order.return_value = False
        self.trader.place_order("XAUUSD", 1, "buy")
        self.assertEqual(self.trader.get_position("XAUUSD"), 0)

if __name__ == '__main__':
    unittest.main()
