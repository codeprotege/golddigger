from fastapi import FastAPI
from ..data_ingestion.yfinance_data import get_ohlcv
from ..data_ingestion.fred_data import get_fred_series
from .technicals import add_technical_indicators
from .macro import add_macro_features

app = FastAPI()

@app.post("/features/full_feature_set")
def create_full_feature_set(ticker: str, fred_series_id: str, fred_api_key: str):
    # Fetch base data
    ohlcv_df = get_ohlcv(ticker)
    fred_df = get_fred_series(fred_series_id, fred_api_key)

    # Add technical indicators
    featured_df = add_technical_indicators(ohlcv_df)

    # Add macro features
    featured_df = add_macro_features(featured_df, fred_df, 'value')

    return featured_df.to_json()
