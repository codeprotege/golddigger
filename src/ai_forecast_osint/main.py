from fastapi import FastAPI
from .nlp import get_model_bias

app = FastAPI()

@app.post("/ai_forecast/bias")
def get_bias(text: str):
    bias, confidence = get_model_bias(text)
    return {"model_bias": bias, "confidence": confidence}
