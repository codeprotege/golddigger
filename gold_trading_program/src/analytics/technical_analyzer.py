import pandas as pd
import numpy as np
import logging

class TechnicalAnalyzer:
    """
    A class to perform technical analysis on price data.
    """
    def __init__(self, data):
        """
        Initializes the TechnicalAnalyzer.

        Args:
            data (pandas.DataFrame): A DataFrame containing the latest price data.
        """
        self.data = data
        self.fetch_historical_data()

    def fetch_historical_data(self):
        try:
            from influxdb_client import InfluxDBClient
            import os

            token = os.environ.get("INFLUXDB_TOKEN")
            org = os.environ.get("INFLUXDB_ORG")
            bucket = os.environ.get("INFLUXDB_BUCKET")
            url = "http://localhost:8086"

            if not all([token, org, bucket]):
                logging.warning("InfluxDB environment variables not set. Skipping historical data fetch.")
                return

            client = InfluxDBClient(url=url, token=token, org=org)
            query_api = client.query_api()

            query = f'from(bucket:"{bucket}") |> range(start: -30d) |> filter(fn:(r) => r._measurement == "gold_price")'
            result = query_api.query_data_frame(org=org, query=query)

            if not result.empty:
                # The result from InfluxDB is a DataFrame with a different structure.
                # We need to pivot it to get the desired format.
                result = result.pivot(index='_time', columns='_field', values='_value').reset_index()
                result = result.rename(columns={'_time': 'last_refreshed', 'exchange_rate': 'exchange_rate'})

                # Combine historical data with the new data
                self.data = pd.concat([result, self.data], ignore_index=True)
                self.data = self.data.sort_values(by='last_refreshed').reset_index(drop=True)

        except ImportError:
            logging.warning("influxdb-client not installed. Skipping historical data fetch.")
        except Exception as e:
            logging.error(f"Error fetching historical data from InfluxDB: {e}")

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
