from app.services.strategies.base_strategy import BaseStrategy
from app.services.technical_analysis import TechnicalAnalysis

class MeanReversionStrategy(BaseStrategy):
    def generate_signals(self):
        ta = TechnicalAnalysis(self.data)
        bollinger_bands = ta.calculate_bollinger_bands()

        if self.data['price'].iloc[-1] < bollinger_bands['BBL_20_2.0'].iloc[-1]:
            return 'buy'
        elif self.data['price'].iloc[-1] > bollinger_bands['BBU_20_2.0'].iloc[-1]:
            return 'sell'
        else:
            return 'hold'
