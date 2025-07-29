import pandas as pd
import pandas_ta as ta

def add_technical_indicators(df):
    """
    Adds a set of technical indicators to the dataframe.
    """
    df.ta.sma(length=20, append=True)
    df.ta.sma(length=50, append=True)
    df.ta.sma(length=200, append=True)
    df.ta.rsi(length=14, append=True)
    df.ta.macd(fast=12, slow=26, signal=9, append=True)
    df.ta.bbands(length=20, std=2, append=True)
    return df
