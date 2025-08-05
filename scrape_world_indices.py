import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta, timezone

def scrape_hourly_data(ticker, name):
    """
    Scrapes hourly data for a given ticker for the last 730 days using UTC.

    Args:
        ticker (str): The ticker symbol to scrape.
        name (str): The common name of the index.

    Returns:
        None
    """
    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=730)

    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    print(f"--------------------------------------------------")
    print(f"Fetching hourly data for {name} ({ticker}) from {start_date_str} to {end_date_str}...")

    data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval="1h"
    )

    if data.empty:
        print(f"No data found for {ticker}.")
        # Some indices might not have data for certain periods, especially on weekends/holidays
        # Also, yfinance sometimes fails for specific tickers for no clear reason.
        # We'll print a warning but continue with the other tickers.
        return

    output_filename = f"{ticker.replace('^','')}_hourly_data.csv"
    print(f"Scraping complete. Total records found: {len(data)}")
    print(f"Saving data to {output_filename}...")
    data.to_csv(output_filename)
    print(f"Data successfully saved to {output_filename}")
    print(f"--------------------------------------------------\n")


if __name__ == "__main__":
    indices_to_scrape = [
        {"name": "S&P 500", "ticker": "^GSPC"},
        {"name": "NASDAQ Composite", "ticker": "^IXIC"},
        {"name": "FTSE 100", "ticker": "^FTSE"},
        {"name": "DAX", "ticker": "^GDAXI"},
        {"name": "Nikkei 225", "ticker": "^N225"},
        {"name": "Hang Seng Index", "ticker": "^HSI"}
    ]

    print("Starting scraping process for major world indices...")

    for index in indices_to_scrape:
        scrape_hourly_data(index["ticker"], index["name"])

    print("All scraping tasks complete.")
