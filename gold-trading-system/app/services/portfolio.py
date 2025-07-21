import pandas as pd

class Portfolio:
    def __init__(self, initial_capital):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.positions = {}
        self.history = []

    def add_position(self, symbol, quantity, price):
        if symbol not in self.positions:
            self.positions[symbol] = 0
        self.positions[symbol] += quantity
        self.cash -= quantity * price
        self.history.append({'symbol': symbol, 'quantity': quantity, 'price': price, 'action': 'buy'})

    def remove_position(self, symbol, quantity, price):
        if symbol in self.positions:
            self.positions[symbol] -= quantity
            self.cash += quantity * price
            self.history.append({'symbol': symbol, 'quantity': quantity, 'price': price, 'action': 'sell'})

    def get_portfolio_value(self, current_prices):
        value = self.cash
        for symbol, quantity in self.positions.items():
            value += quantity * current_prices.get(symbol, 0)
        return value

    def get_returns(self):
        df = pd.DataFrame(self.history)
        if df.empty:
            return pd.Series()
        df['value'] = df['quantity'] * df['price']
        buy_value = df[df['action'] == 'buy']['value'].sum()
        sell_value = df[df['action'] == 'sell']['value'].sum()
        return (sell_value - buy_value) / buy_value if buy_value != 0 else 0
