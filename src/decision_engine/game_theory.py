import numpy as np

def get_best_strategy(event_risk, model_confidence, market_volatility):
    """
    Determines the best strategy based on a game theory matrix.
    """
    # This is a simplified example. A real implementation would be more complex.
    payoff_matrix = {
        "Long-Conservative": 0.5 * model_confidence - 0.3 * event_risk - 0.2 * market_volatility,
        "Long-Aggressive": 0.7 * model_confidence - 0.5 * event_risk - 0.3 * market_volatility,
        "Short-Volatility": -0.3 * model_confidence + 0.5 * event_risk + 0.7 * market_volatility,
    }

    best_strategy = max(payoff_matrix, key=payoff_matrix.get)
    confidence = payoff_matrix[best_strategy]

    return best_strategy, confidence
