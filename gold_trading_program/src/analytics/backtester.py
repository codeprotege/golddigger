import backtrader as bt
import pandas as pd
from .technical_analyzer import TechnicalAnalyzer

class Backtester:
    def __init__(self, historical_data, strategy_func):
        self.historical_data = historical_data
        self.strategy_func = strategy_func
        self.cerebro = bt.Cerebro()

    def run_backtest(self):
        # Add the data feed
        data_feed = bt.feeds.PandasData(dataname=self.historical_data, datetime='last_refreshed', open='exchange_rate', high='exchange_rate', low='exchange_rate', close='exchange_rate', volume=None, openinterest=None)
        self.cerebro.adddata(data_feed)

        # Add the strategy
        self.cerebro.addstrategy(self.strategy_func)

        # Set starting cash
        self.cerebro.broker.setcash(100000.0)

        # Add analyzers
        self.cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe_ratio')
        self.cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        self.cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')

        print('Starting Portfolio Value: %.2f' % self.cerebro.broker.getvalue())

        results = self.cerebro.run()

        print('Final Portfolio Value: %.2f' % self.cerebro.broker.getvalue())

        # Print out the analysis
        sharpe_ratio = results[0].analyzers.sharpe_ratio.get_analysis()
        drawdown = results[0].analyzers.drawdown.get_analysis()
        returns = results[0].analyzers.returns.get_analysis()

        print(f"Sharpe Ratio: {sharpe_ratio['sharperatio']:.2f}")
        print(f"Max Drawdown: {drawdown.max.drawdown:.2f}%")
        print(f"Total Return: {returns['rtot'] * 100:.2f}%")

class ExampleStrategy(bt.Strategy):
    params = (
        ('sma_period', 20),
        ('rsi_period', 14),
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.sma_period)
        self.rsi = bt.indicators.RelativeStrengthIndex(self.data.close, period=self.params.rsi_period)

    def next(self):
        if not self.position:  # Not in the market
            if self.data.close[0] > self.sma[0] and self.rsi[0] < 30:
                self.buy()
        else:
            if self.data.close[0] < self.sma[0] and self.rsi[0] > 70:
                self.sell()

if __name__ == '__main__':
    # Create some dummy historical data
    historical_data = pd.DataFrame({
        'last_refreshed': pd.to_datetime(pd.date_range(start='2023-01-01', periods=100)),
        'exchange_rate': pd.Series(pd.np.random.uniform(1700, 1800, 100))
    })

    backtester = Backtester(historical_data, ExampleStrategy)
    backtester.run_backtest()
