import unittest
import pandas as pd
from src.feature_engineering.technicals import add_technical_indicators

class TestFeatureEngineering(unittest.TestCase):

    def test_add_technical_indicators(self):
        data = {'Close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]}
        df = pd.DataFrame(data)
        df = add_technical_indicators(df)
        self.assertIn('SMA_20', df.columns)
        self.assertIn('RSI_14', df.columns)

if __name__ == '__main__':
    unittest.main()
