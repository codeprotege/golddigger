import unittest
import sys
import os
from unittest.mock import patch

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.data_ingestion.data_fetcher import DataFetcher

class TestDataFetcher(unittest.TestCase):
    """
    Unit tests for the DataFetcher class.
    """

    @patch('src.data_ingestion.data_fetcher.requests.get')
    def test_get_gold_price_success(self, mock_get):
        """
        Test that get_gold_price returns a dictionary on a successful API call.
        """
        mock_response = {
            "Realtime Currency Exchange Rate": {
                "1. From_Currency Code": "XAU",
                "2. From_Currency Name": "Gold",
                "3. To_Currency Code": "USD",
                "4. To_Currency Name": "United States Dollar",
                "5. Exchange Rate": "1750.00000000",
                "6. Last Refreshed": "2025-07-21 05:30:00",
                "7. Time Zone": "UTC",
                "8. Bid Price": "1749.90000000",
                "9. Ask Price": "1750.10000000"
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        fetcher = DataFetcher(api_key="TEST_API_KEY")
        price_data = fetcher.get_gold_price()

        self.assertIsInstance(price_data, dict)
        self.assertIn("Realtime Currency Exchange Rate", price_data)

    @patch('src.data_ingestion.data_fetcher.requests.get')
    def test_get_gold_price_api_error(self, mock_get):
        """
        Test that get_gold_price returns None when the API returns an error.
        """
        mock_response = {"Error Message": "Invalid API call"}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        fetcher = DataFetcher(api_key="TEST_API_KEY")
        price_data = fetcher.get_gold_price()

        self.assertIsNone(price_data)

    @patch('src.data_ingestion.data_fetcher.requests.get')
    def test_get_gold_price_request_exception(self, mock_get):
        """
        Test that get_gold_price returns None after max retries on a request exception.
        """
        mock_get.side_effect = Exception("Test exception")

        fetcher = DataFetcher(api_key="TEST_API_KEY", max_retries=2, retry_delay=0.1)

        # This test is tricky because the exception is caught inside the function.
        # We can't use assertRaises. Instead, we'll just check the final result
        # and the number of calls.
        price_data = fetcher.get_gold_price()
        self.assertIsNone(price_data)
        self.assertEqual(mock_get.call_count, 2)

if __name__ == '__main__':
    unittest.main()
