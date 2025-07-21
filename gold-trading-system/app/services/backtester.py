from backtesting import Backtest, Strategy
from backtesting.lib import crossover

class Backtester:
    def __init__(self, data, strategy_class):
        self.data = data
        self.strategy_class = strategy_class

    def run_backtest(self):
        bt = Backtest(self.data, self.strategy_class, cash=10000, commission=.002)
        stats = bt.run()
        return stats

    def optimize_strategy(self):
        bt = Backtest(self.data, self.strategy_class, cash=10000, commission=.002)
        stats = bt.optimize(n1=range(5, 30, 5), n2=range(10, 70, 5), maximize='Sharpe Ratio')
        return stats

class MovingAverageCrossStrategy(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        self.sma1 = self.I(lambda x: pd.Series(x).rolling(self.n1).mean(), self.data.Close)
        self.sma2 = self.I(lambda x: pd.Series(x).rolling(self.n2).mean(), self.data.Close)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()
