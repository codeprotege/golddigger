import requests
import time
import logging

class DataFetcher:
    """
    A class to fetch gold price data from the Alpha Vantage API.
    """
    def __init__(self, api_key, max_retries=3, retry_delay=60):
        """
        Initializes the DataFetcher.

        Args:
            api_key (str): The API key for Alpha Vantage.
            max_retries (int): The maximum number of retries for API calls.
            retry_delay (int): The delay in seconds between retries.
        """
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def get_gold_price(self):
        """
        Fetches the current gold price from Alpha Vantage.

        Returns:
            dict: A dictionary containing the gold price data, or None if the request fails.
        """
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": "XAU",
            "to_currency": "USD",
            "apikey": self.api_key,
        }

        for attempt in range(self.max_retries):
            try:
                response = requests.get(self.base_url, params=params)
                response.raise_for_status()  # Raise an exception for bad status codes
                data = response.json()

                if "Error Message" in data:
                    print(f"API Error: {data['Error Message']}")
                    return None

                if "Note" in data:
                    print(f"API Note: {data['Note']}")
                    # This often indicates a rate limit, so we'll wait and retry
                    time.sleep(self.retry_delay)
                    continue

                return data

            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                if attempt < self.max_retries - 1:
                    print(f"Retrying in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)
                else:
                    print("Max retries reached. Could not fetch data.")
                    return None
        return None

if __name__ == "__main__":
    # Replace with your actual Alpha Vantage API key
    fetcher = DataFetcher(api_key="YOUR_API_KEY")
    price_data = fetcher.get_gold_price()
    if price_data:
        print(price_data)
