import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def scrape_sp500_hourly_for_last_730_days(ticker="^GSPC"):
    """
    Scrapes hourly data for the S&P 500 index (^GSPC) for the last 730 days.

    Args:
        ticker (str): The ticker symbol to scrape. Defaults to "^GSPC".

    Returns:
        pandas.DataFrame: A DataFrame containing the hourly data, or None if no data is found.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=730)

    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    print(f"Fetching hourly data for {ticker} from {start_date_str} to {end_date_str}...")

    data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval="1h"
    )

    if data.empty:
        print("No data found for the specified range.")
        return None

    return data

if __name__ == "__main__":
    OUTPUT_CSV = "sp500_hourly_data_last_730_days.csv"

    print("Starting S&P 500 hourly data scraping process for the last 730 days...")
    sp500_data = scrape_sp500_hourly_for_last_730_days()

    if sp500_data is not None and not sp500_data.empty:
        print(f"Scraping complete. Total records found: {len(sp500_data)}")
        print(f"Saving data to {OUTPUT_CSV}...")
        sp500_data.to_csv(OUTPUT_CSV)
        print(f"Data successfully saved to {OUTPUT_CSV}")
    else:
        print("Failed to download data or no data was available.")
