from app.services.technical_analysis import TechnicalAnalysis

class SignalGenerator:
    def __init__(self, data):
        self.ta = TechnicalAnalysis(data)

    def generate_signals(self):
        rsi = self.ta.calculate_rsi()
        macd = self.ta.calculate_macd()
        bollinger_bands = self.ta.calculate_bollinger_bands()

        # Example signal logic
        if rsi.iloc[-1] < 30 and macd['MACD_12_26_9'].iloc[-1] > macd['MACDs_12_26_9'].iloc[-1]:
            return 'buy'
        elif rsi.iloc[-1] > 70 and macd['MACD_12_26_9'].iloc[-1] < macd['MACDs_12_26_9'].iloc[-1]:
            return 'sell'
        else:
            return 'hold'
