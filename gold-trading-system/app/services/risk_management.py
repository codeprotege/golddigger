class RiskManagement:
    def __init__(self, balance, risk_per_trade=0.02):
        self.balance = balance
        self.risk_per_trade = risk_per_trade

    def calculate_position_size(self, entry_price, stop_loss_price):
        risk_amount = self.balance * self.risk_per_trade
        risk_per_share = entry_price - stop_loss_price
        if risk_per_share <= 0:
            return 0
        return risk_amount / risk_per_share

    def check_max_drawdown(self, current_equity, max_drawdown=0.15):
        return (self.balance - current_equity) / self.balance > max_drawdown
