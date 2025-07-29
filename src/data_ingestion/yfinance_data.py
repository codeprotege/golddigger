import yfinance as yf
import pandas as pd

def get_ohlcv(ticker, period="max"):
    """
    Fetches historical OHLCV data for a given ticker from Yahoo Finance.
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df.index = df.index.tz_localize(None)
    df.index = pd.to_datetime(df.index)
    return df

def get_etf_flows(ticker, period="max"):
    """
    Fetches historical ETF flow data for a given ticker from Yahoo Finance.
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df.index = df.index.tz_localize(None)
    df.index = pd.to_datetime(df.index)
    return df
