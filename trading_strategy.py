
import pandas as pd

def moving_average_crossover_strategy(df):
    """
    A simple moving average crossover strategy.

    Args:
        df (pd.DataFrame): A DataFrame with gold price data, including 'SMA_50' and 'SMA_200'.

    Returns:
        pd.DataFrame: A DataFrame with an additional 'Signal' column.
    """
    df['Signal'] = 0
    df.loc[df['SMA_50'] > df['SMA_200'], 'Signal'] = 1
    df.loc[df['SMA_50'] < df['SMA_200'], 'Signal'] = -1
    return df

if __name__ == '__main__':
    with open('gold_prices.json', 'r') as f:
        data = pd.read_json(f)

    df = pd.DataFrame(data)
    df['Date_'] = pd.to_datetime(df['Date_'])
    df.set_index('Date_', inplace=True)

    df['SMA_50'] = df['Close_GC=F'].rolling(window=50).mean()
    df['SMA_200'] = df['Close_GC=F'].rolling(window=200).mean()

    df = moving_average_crossover_strategy(df)

    print(df.tail())
