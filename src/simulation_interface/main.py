from fastapi import FastAPI
from .simulation import run_weekly_simulation

app = FastAPI()

@app.post("/simulation/weekly")
def run_simulation(start_date: str, end_date: str, ticker: str, fred_series_id: str, fred_api_key: str):
    results = run_weekly_simulation(start_date, end_date, ticker, fred_series_id, fred_api_key)
    return {"simulation_results": results}
