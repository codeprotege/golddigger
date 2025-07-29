import numpy as np

def predict_xgboost(model, data):
    """
    Makes a prediction using the XGBoost model.
    """
    dmatrix = xgb.DMatrix(data)
    return model.predict(dmatrix)

def predict_lstm(model, data):
    """
    Makes a prediction using the LSTM model.
    """
    # Reshape data for LSTM input
    data = np.reshape(data, (data.shape[0], 1, data.shape[1]))
    return model.predict(data)

def predict_hybrid(xgboost_model, lstm_model, data):
    """
    Makes a prediction using the hybrid model.
    """
    xgboost_pred = predict_xgboost(xgboost_model, data)
    lstm_pred = predict_lstm(lstm_model, data)

    # Combine predictions (e.g., simple averaging)
    hybrid_pred = (xgboost_pred + lstm_pred) / 2
    return hybrid_pred
