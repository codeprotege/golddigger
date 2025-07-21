import numpy as np

class RiskAnalytics:
    def __init__(self, returns):
        self.returns = np.array(returns)

    def calculate_sharpe_ratio(self, risk_free_rate=0.0):
        mean_return = np.mean(self.returns)
        std_dev = np.std(self.returns)
        if std_dev == 0:
            return 0
        return (mean_return - risk_free_rate) / std_dev

    def calculate_max_drawdown(self):
        cumulative_returns = np.cumprod(1 + self.returns)
        peak = np.maximum.accumulate(cumulative_returns)
        drawdown = (cumulative_returns - peak) / peak
        return np.min(drawdown) if len(drawdown) > 0 else 0

    def calculate_var(self, confidence_level=0.95):
        if len(self.returns) == 0:
            return 0
        return np.percentile(self.returns, 100 * (1 - confidence_level))
