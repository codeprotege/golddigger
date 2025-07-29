# Gold Trading AI

This project is a predictive trading and strategic decision-making platform for XAUUSD (Gold/USD) using a feature-rich ML pipeline, game theory, and AI-based forecast mechanisms.

## Modules

- **Data Ingestion**: Ingests real-time and historical multi-source financial data.
- **Feature Engineering**: Engineers over 120 financial features.
- **Model Layer**: Feeds features into a hybrid model (e.g., LSTM + XGBoost).
- **Decision Engine**: Implements a Game Theory matrix for strategic recommendations.
- **Simulation Interface**: Provides a backend for running simulations.
- **AI Forecast & OSINT**: Uses NLP models to parse news and update model bias.

## API

The application is built with FastAPI and can be run with `uvicorn src.main:app --reload`.

### Endpoints

- `GET /`: Welcome message.
- `GET /data/ohlcv/{ticker}`: Get OHLCV data.
- `GET /data/etf_flows/{ticker}`: Get ETF flow data.
- `GET /data/fred/{series_id}`: Get data from FRED.
- `POST /features/full_feature_set`: Create a full feature set.
- `POST /predict`: Make a prediction.
- `POST /decision`: Make a decision.
- `POST /simulation/weekly`: Run a weekly simulation.
- `POST /ai_forecast/bias`: Get model bias from text.
