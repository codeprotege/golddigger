from fastapi import FastAPI
from .model_loader import load_xgboost_model, load_lstm_model
from .prediction import predict_hybrid
from ..feature_engineering.main import create_full_feature_set
import pandas as pd

app = FastAPI()

# Load models on startup
XGBOOST_MODEL_PATH = "models/xgboost_model.json"
LSTM_MODEL_PATH = "models/lstm_model.h5"
xgboost_model = load_xgboost_model(XGBOOST_MODEL_PATH)
lstm_model = load_lstm_model(LSTM_MODEL_PATH)


@app.post("/predict")
def predict(ticker: str, fred_series_id: str, fred_api_key: str):
    # Get features
    feature_set_json = create_full_feature_set(ticker, fred_series_id, fred_api_key)
    feature_set_df = pd.read_json(feature_set_json)

    # Make prediction
    prediction = predict_hybrid(xgboost_model, lstm_model, feature_set_df)

    return {"prediction": prediction.tolist()}
