import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataProcessor:
    """
    A class to process raw data from the data fetcher.
    """
    def __init__(self, raw_data):
        """
        Initializes the DataProcessor.

        Args:
            raw_data (dict): The raw data from the data fetcher.
        """
        self.raw_data = raw_data

    def process_data(self):
        """
        Processes the raw data, converts it to a DataFrame, and stores it.

        Returns:
            pandas.DataFrame: A DataFrame containing the processed data.
        """
        logging.info("Starting data processing.")
        if "Realtime Currency Exchange Rate" in self.raw_data:
            data = self.raw_data["Realtime Currency Exchange Rate"]
            logging.info(f"Processing data for {data.get('2. From_Currency Name')}.")
            df = pd.DataFrame([data])
            df = df.rename(columns={
                "1. From_Currency Code": "from_currency",
                "2. From_Currency Name": "from_currency_name",
                "3. To_Currency Code": "to_currency",
                "4. To_Currency Name": "to_currency_name",
                "5. Exchange Rate": "exchange_rate",
                "6. Last Refreshed": "last_refreshed",
                "7. Time Zone": "time_zone",
                "8. Bid Price": "bid_price",
                "9. Ask Price": "ask_price",
            })

            # Convert numeric columns
            numeric_cols = ['exchange_rate', 'bid_price', 'ask_price']
            for col in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors='coerce')

            # Convert to datetime
            df['last_refreshed'] = pd.to_datetime(df['last_refreshed'])

            logging.info("Data processing completed successfully.")
            self.store_data(df)
            return df
        else:
            logging.warning("No 'Realtime Currency Exchange Rate' data found in the raw data.")
            return pd.DataFrame()

    def store_data(self, df):
        try:
            df.to_csv("gold_prices.csv", mode='a', header=not pd.io.common.file_exists("gold_prices.csv"), index=False)
            logging.info("Data stored successfully.")
        except IOError as e:
            logging.error(f"Error storing data: {e}")

if __name__ == "__main__":
    # Example usage with dummy data
    dummy_data = {
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
    processor = DataProcessor(raw_data=dummy_data)
    processed_df = processor.process_data()
    print(processed_df)
    print(processed_df.info())
