import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import json

def get_gold_data_yfinance(symbol, start_date, end_date):
    """
    Fetches historical gold price data using yfinance.

    Args:
        symbol (str): The symbol for gold (e.g., 'GC=F' for Gold Futures).
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: A DataFrame containing the historical data.
    """
    try:
        gold_data = yf.download(symbol, start=start_date, end=end_date)
        return gold_data
    except Exception as e:
        print(f"Failed to fetch data using yfinance: {e}")
        return None

if __name__ == "__main__":
    # Define parameters
    symbol = 'GC=F'  # Gold Futures symbol for yfinance
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365*5)).strftime('%Y-%m-%d')  # 5 years of data

    # Fetch data
    gold_data = get_gold_data_yfinance(symbol, start_date, end_date)

    # Save data to JSON
    if gold_data is not None and not gold_data.empty:
        # Reset index to make date a column
        gold_data_reset = gold_data.reset_index()
        # Flatten multi-level column headers
        gold_data_reset.columns = ['_'.join(col).strip() for col in gold_data_reset.columns.values]
        # Convert Timestamp objects to strings
        gold_data_reset['Date_'] = gold_data_reset['Date_'].dt.strftime('%Y-%m-%d')
        print(gold_data_reset.head())
        # Convert DataFrame to a list of dictionaries
        gold_data_json = gold_data_reset.to_dict(orient='records')

        with open('gold_prices.json', 'w') as f:
            json.dump(gold_data_json, f, indent=4)

        print("Gold price data saved to gold_prices.json")
    else:
        print("Failed to fetch gold price data or no data available for the given symbol and date range.")
