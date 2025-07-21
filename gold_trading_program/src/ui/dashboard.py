import tkinter as tk
import pandas as pd
from src.data_ingestion.data_fetcher import DataFetcher
from src.data_processing.data_processor import DataProcessor
from src.analytics.technical_analyzer import TechnicalAnalyzer
from src.trading.trader import Trader

class TradingDashboard:
    """
    A class to create the trading dashboard UI.
    """
    def __init__(self, root):
        """
        Initializes the TradingDashboard.

        Args:
            root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Gold Trading Dashboard")

        self.price_label = tk.Label(root, text="Price: N/A", font=("Arial", 16))
        self.price_label.pack(pady=10)

        self.signal_label = tk.Label(root, text="Signal: N/A", font=("Arial", 16))
        self.signal_label.pack(pady=10)

        self.position_label = tk.Label(root, text="Position: N/A", font=("Arial", 16))
        self.position_label.pack(pady=10)

        # Initialize components
        self.fetcher = DataFetcher(api_key="YOUR_API_KEY")

        class DummyBrokerage:
            def submit_order(self, symbol, quantity, order_type):
                print(f"Dummy Brokerage: Submitted {order_type} order for {quantity} of {symbol}")
                return True
        self.trader = Trader(brokerage_api=DummyBrokerage())

        self.update_data()

    def update_data(self):
        # Fetch new data
        raw_data = self.fetcher.get_gold_price()
        if raw_data:
            processor = DataProcessor(raw_data)
            processed_df = processor.process_data()

            if not processed_df.empty:
                price = processed_df.iloc[0]['exchange_rate']
                self.price_label.config(text=f"Price: ${price:.2f}")

                # Analyze data
                historical_data = pd.read_csv("gold_prices.csv")
                combined_data = pd.concat([historical_data, processed_df], ignore_index=True)

                analyzer = TechnicalAnalyzer(data=combined_data.copy())
                analyzer.calculate_sma(window=10)
                analyzer.calculate_rsi(window=14)
                analyzed_df = analyzer.data

                # Trading logic
                latest_data = analyzed_df.iloc[-1]
                if latest_data['exchange_rate'] > latest_data['sma'] and latest_data['rsi'] < 30:
                    signal = "Buy"
                    self.trader.place_order("XAUUSD", 1, "buy")
                elif latest_data['exchange_rate'] < latest_data['sma'] and latest_data['rsi'] > 70:
                    signal = "Sell"
                    self.trader.place_order("XAUUSD", 1, "sell")
                else:
                    signal = "Hold"

                self.signal_label.config(text=f"Signal: {signal}")
                self.position_label.config(text=f"Position: {self.trader.get_position('XAUUSD')}")

        # Schedule the next update
        self.root.after(60000, self.update_data) # Update every 60 seconds

def create_dashboard():
    root = tk.Tk()
    app = TradingDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
