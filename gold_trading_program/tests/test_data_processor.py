import unittest
import pandas as pd
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.data_processing.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    """
    Unit tests for the DataProcessor class.
    """

    def test_process_data_success(self):
        """
        Test that process_data correctly processes valid raw data.
        """
        raw_data = {
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
        processor = DataProcessor(raw_data)
        processed_df = processor.process_data()

        self.assertIsInstance(processed_df, pd.DataFrame)
        self.assertFalse(processed_df.empty)
        self.assertEqual(len(processed_df), 1)
        self.assertIn('exchange_rate', processed_df.columns)
        self.assertEqual(processed_df.iloc[0]['exchange_rate'], 1750.0)

    def test_process_data_missing_key(self):
        """
        Test that process_data returns an empty DataFrame when the required key is missing.
        """
        raw_data = {"some_other_key": "some_value"}
        processor = DataProcessor(raw_data)
        processed_df = processor.process_data()

        self.assertIsInstance(processed_df, pd.DataFrame)
        self.assertTrue(processed_df.empty)

if __name__ == '__main__':
    unittest.main()
