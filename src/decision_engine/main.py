from fastapi import FastAPI
from .game_theory import get_best_strategy
from ..model_layer.main import predict

app = FastAPI()

@app.post("/decision")
def make_decision(ticker: str, fred_series_id: str, fred_api_key: str, event_risk: float, market_volatility: float):
    # Get model prediction
    prediction_response = predict(ticker, fred_series_id, fred_api_key)
    model_confidence = prediction_response["prediction"][0] # Simplified

    # Get best strategy
    strategy, confidence = get_best_strategy(event_risk, model_confidence, market_volatility)

    return {"strategy": strategy, "confidence": confidence}
