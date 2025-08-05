import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta, timezone
import time
import os

def get_last_timestamp(filepath):
    """Gets the last timestamp from a CSV file."""
    if not os.path.exists(filepath):
        return None

    try:
        df = pd.read_csv(filepath, parse_dates=['Datetime'])
        # Ensure the Datetime column is timezone-aware
        df['Datetime'] = pd.to_datetime(df['Datetime'], utc=True)
        if df.empty:
            return None
        return df['Datetime'].max()
    except (FileNotFoundError, pd.errors.EmptyDataError, KeyError) as e:
        # Handle cases where file is empty, doesn't exist, or has no 'Datetime' column
        print(f"Could not read timestamp from {filepath}. Reason: {e}. Assuming no previous data.")
        return None

def scrape_and_append_data(ticker, name, filepath):
    """
    Scrapes the latest hourly data and appends only new records to the CSV.
    """
    print(f"--- Checking for new data for {name} ({ticker}) ---")

    last_timestamp = get_last_timestamp(filepath)

    # Fetch data for the last 730 days (yfinance requirement for hourly data)
    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=730)

    data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval="1h"
    )

    if data.empty:
        print(f"No data received for {ticker}.")
        return

    # Reset index to make 'Datetime' a column and ensure it's timezone-aware
    data = data.reset_index()
    data['Datetime'] = pd.to_datetime(data['Datetime'], utc=True)

    new_data = data
    if last_timestamp:
        # Ensure last_timestamp is timezone-aware for comparison
        last_timestamp_aware = pd.to_datetime(last_timestamp, utc=True)
        new_data = data[data['Datetime'] > last_timestamp_aware]

    if new_data.empty:
        print("No new records to add.")
        return

    print(f"Found {len(new_data)} new records. Appending to {filepath}...")

    # If file doesn't exist, write header. Otherwise, append without header.
    header = not os.path.exists(filepath)
    new_data.to_csv(filepath, mode='a', header=header, index=False)
    print("Append complete.")


if __name__ == "__main__":
    indices_to_scrape = [
        {"name": "S&P 500", "ticker": "^GSPC"},
        {"name": "NASDAQ Composite", "ticker": "^IXIC"},
        # Add other tickers here. Note: yfinance may not have hourly data for all.
        {"name": "FTSE 100", "ticker": "^FTSE"},
        {"name": "DAX", "ticker": "^GDAXI"},
        {"name": "Nikkei 225", "ticker": "^N225"},
        {"name": "Hang Seng Index", "ticker": "^HSI"}
    ]

    # Time to wait between each full scrape cycle (in seconds)
    # 3600 seconds = 1 hour
    SLEEP_INTERVAL = 3600

    while True:
        print("\n" + "="*50)
        print(f"Starting new scrape cycle at {datetime.now(timezone.utc).isoformat()}")
        print("="*50)

        for index in indices_to_scrape:
            filepath = f"{index['ticker'].replace('^','')}_hourly_data.csv"
            scrape_and_append_data(index["ticker"], index["name"], filepath)
            # Small delay between tickers to be polite to the API
            time.sleep(5)

        print("\n" + "="*50)
        print(f"Scrape cycle complete. Waiting for {SLEEP_INTERVAL / 60} minutes...")
        print("="*50)
        time.sleep(SLEEP_INTERVAL)
