import unittest
from src.data_ingestion.yfinance_data import get_ohlcv

class TestDataIngestion(unittest.TestCase):

    def test_get_ohlcv(self):
        df = get_ohlcv("GC=F")
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
