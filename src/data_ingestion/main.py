from fastapi import FastAPI
from .yfinance_data import get_ohlcv, get_etf_flows
from .fred_data import get_fred_series

app = FastAPI()

@app.get("/data/ohlcv/{ticker}")
def read_ohlcv(ticker: str, period: str = "max"):
    return get_ohlcv(ticker, period).to_json()

@app.get("/data/etf_flows/{ticker}")
def read_etf_flows(ticker: str, period: str = "max"):
    return get_etf_flows(ticker, period).to_json()

@app.get("/data/fred/{series_id}")
def read_fred_series(series_id: str, api_key: str):
    return get_fred_series(series_id, api_key).to_json()
