import xgboost as xgb
import tensorflow as tf

def load_xgboost_model(path):
    """
    Loads a pre-trained XGBoost model.
    """
    model = xgb.Booster()
    model.load_model(path)
    return model

def load_lstm_model(path):
    """
    Loads a pre-trained LSTM model.
    """
    model = tf.keras.models.load_model(path)
    return model
