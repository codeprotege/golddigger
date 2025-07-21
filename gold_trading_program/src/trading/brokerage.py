import alpaca_trade_api as tradeapi
import os
import logging

class AlpacaBrokerage:
    """
    A class to interact with the Alpaca brokerage.
    """
    def __init__(self):
        """
        Initializes the AlpacaBrokerage.
        """
        try:
            self.api = tradeapi.REST(
                os.environ.get("APCA_API_KEY_ID"),
                os.environ.get("APCA_API_SECRET_KEY"),
                base_url=os.environ.get("APCA_API_BASE_URL", "https://paper-api.alpaca.markets")
            )
            self.account = self.api.get_account()
            logging.info("Connected to Alpaca brokerage.")
        except Exception as e:
            logging.error(f"Failed to connect to Alpaca: {e}")
            self.api = None
            self.account = None

    def submit_order(self, symbol, quantity, order_type):
        """
        Submits an order to the brokerage.

        Args:
            symbol (str): The symbol to trade.
            quantity (float): The quantity to trade.
            order_type (str): The type of order ('buy' or 'sell').

        Returns:
            bool: True if the order was submitted successfully, False otherwise.
        """
        if self.api:
            try:
                self.api.submit_order(
                    symbol=symbol,
                    qty=quantity,
                    side=order_type,
                    type='market',
                    time_in_force='gtc'
                )
                logging.info(f"Submitted {order_type} order for {quantity} of {symbol}")
                return True
            except Exception as e:
                logging.error(f"Failed to submit order: {e}")
                return False
        else:
            logging.error("Not connected to Alpaca. Cannot submit order.")
            return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    brokerage = AlpacaBrokerage()
    if brokerage.api:
        brokerage.submit_order("XAUUSD", 1, "buy")
