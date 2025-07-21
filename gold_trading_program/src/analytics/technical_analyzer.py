import pandas as pd
import numpy as np

class TechnicalAnalyzer:
    """
    A class to perform technical analysis on price data.
    """
    def __init__(self, data):
        """
        Initializes the TechnicalAnalyzer.

        Args:
            data (pandas.DataFrame): A DataFrame containing price data.
        """
        self.data = data

    def calculate_sma(self, window):
        """
        Calculates the Simple Moving Average (SMA).

        Args:
            window (int): The window size for the SMA.

        Returns:
            pandas.DataFrame: The DataFrame with the SMA column added.
        """
        if "exchange_rate" in self.data.columns:
            self.data["sma"] = self.data["exchange_rate"].rolling(window=window).mean()
        return self.data

    def calculate_rsi(self, window=14):
        if "exchange_rate" in self.data.columns:
            delta = self.data["exchange_rate"].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
            rs = gain / loss
            self.data["rsi"] = 100 - (100 / (1 + rs))
        return self.data

    def calculate_macd(self, fast_period=12, slow_period=26, signal_period=9):
        if "exchange_rate" in self.data.columns:
            fast_ema = self.data["exchange_rate"].ewm(span=fast_period, adjust=False).mean()
            slow_ema = self.data["exchange_rate"].ewm(span=slow_period, adjust=False).mean()
            self.data["macd"] = fast_ema - slow_ema
            self.data["macd_signal"] = self.data["macd"].ewm(span=signal_period, adjust=False).mean()
        return self.data

if __name__ == "__main__":
    # Example usage with dummy data
    dummy_df = pd.DataFrame({
        "exchange_rate": np.random.uniform(1700, 1800, 50)
    })
    analyzer = TechnicalAnalyzer(data=dummy_df)
    analyzer.calculate_sma(window=10)
    analyzer.calculate_rsi()
    analyzer.calculate_macd()
    print(analyzer.data.tail())
