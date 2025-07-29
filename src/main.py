from fastapi import FastAPI
from .data_ingestion.main import app as data_app
from .feature_engineering.main import app as feature_app
from .model_layer.main import app as model_app
from .decision_engine.main import app as decision_app

app = FastAPI()

app.mount("/data", data_app)
app.mount("/features", feature_app)
app.mount("/model", model_app)
app.mount("/decision", decision_app)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Gold Trading AI API"}
