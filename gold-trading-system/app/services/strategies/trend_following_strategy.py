from app.services.strategies.base_strategy import BaseStrategy
from app.services.technical_analysis import TechnicalAnalysis

class TrendFollowingStrategy(BaseStrategy):
    def generate_signals(self):
        ta = TechnicalAnalysis(self.data)
        macd = ta.calculate_macd()

        if macd['MACD_12_26_9'].iloc[-1] > macd['MACDs_12_26_9'].iloc[-1]:
            return 'buy'
        elif macd['MACD_12_26_9'].iloc[-1] < macd['MACDs_12_26_9'].iloc[-1]:
            return 'sell'
        else:
            return 'hold'
