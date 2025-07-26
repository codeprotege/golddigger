
import pandas as pd
from trading_strategy import moving_average_crossover_strategy

def backtest_strategy(df):
    """
    Backtests the moving average crossover strategy.

    Args:
        df (pd.DataFrame): A DataFrame with gold price data and a 'Signal' column.

    Returns:
        float: The final portfolio value.
    """
    initial_capital = 10000.0
    positions = pd.DataFrame(index=df.index).fillna(0.0)
    portfolio = pd.DataFrame(index=df.index).fillna(0.0)

    positions['GC=F'] = df['Signal']

    portfolio['positions'] = (positions['GC=F'].multiply(df['Close_GC=F'], axis=0))
    portfolio['cash'] = initial_capital - (positions.diff().multiply(df['Close_GC=F'], axis=0)).cumsum()
    portfolio['total'] = portfolio['positions'] + portfolio['cash']

    return portfolio

if __name__ == '__main__':
    with open('gold_prices.json', 'r') as f:
        data = pd.read_json(f)

    df = pd.DataFrame(data)
    df['Date_'] = pd.to_datetime(df['Date_'])
    df.set_index('Date_', inplace=True)

    df['SMA_50'] = df['Close_GC=F'].rolling(window=50).mean()
    df['SMA_200'] = df['Close_GC=F'].rolling(window=200).mean()

    df = moving_average_crossover_strategy(df)

    portfolio = backtest_strategy(df)

    print(portfolio.tail())
