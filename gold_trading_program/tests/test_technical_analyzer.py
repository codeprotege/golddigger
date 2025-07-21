import unittest
import pandas as pd
import numpy as np
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.analytics.technical_analyzer import TechnicalAnalyzer

class TestTechnicalAnalyzer(unittest.TestCase):
    """
    Unit tests for the TechnicalAnalyzer class.
    """

    def setUp(self):
        """
        Set up a sample DataFrame for testing.
        """
        self.data = pd.DataFrame({
            'exchange_rate': np.random.uniform(1700, 1800, 50)
        })
        self.analyzer = TechnicalAnalyzer(self.data)

    def test_calculate_sma(self):
        """
        Test that calculate_sma adds the 'sma' column to the DataFrame.
        """
        self.analyzer.calculate_sma(window=10)
        self.assertIn('sma', self.analyzer.data.columns)
        self.assertFalse(self.analyzer.data['sma'].isnull().all())

    def test_calculate_rsi(self):
        """
        Test that calculate_rsi adds the 'rsi' column to the DataFrame.
        """
        self.analyzer.calculate_rsi(window=14)
        self.assertIn('rsi', self.analyzer.data.columns)
        self.assertFalse(self.analyzer.data['rsi'].isnull().all())

    def test_calculate_macd(self):
        """
        Test that calculate_macd adds the 'macd' and 'macd_signal' columns.
        """
        self.analyzer.calculate_macd()
        self.assertIn('macd', self.analyzer.data.columns)
        self.assertIn('macd_signal', self.analyzer.data.columns)
        self.assertFalse(self.analyzer.data['macd'].isnull().all())
        self.assertFalse(self.analyzer.data['macd_signal'].isnull().all())

if __name__ == '__main__':
    unittest.main()
