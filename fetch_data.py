import yfinance as yf
import pandas as pd

def fetch_dji_data(period="60d", interval="60m"):
    """
    Fetches Dow Jones Industrial Average (DJI) data for a given period and interval.
    """
    print("Fetching DJI data...")
    dji = yf.Ticker("^DJI")

    # Get historical market data
    hist = dji.history(period=period, interval=interval)

    return hist

def save_to_csv(data, filename="dji_1h_data.csv"):
    """
    Saves a pandas DataFrame to a CSV file.
    """
    print(f"Saving data to {filename}...")
    data.to_csv(filename)
    print("Data saved successfully.")

if __name__ == "__main__":
    data = fetch_dji_data()
    if not data.empty:
        save_to_csv(data)
    else:
        print("No data fetched. Please check the ticker or network connection.")
