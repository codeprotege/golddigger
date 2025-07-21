import pandas as pd
import pandas_ta as ta

class TechnicalAnalysis:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def calculate_rsi(self, length=14):
        return self.df.ta.rsi(length=length)

    def calculate_macd(self, fast=12, slow=26, signal=9):
        return self.df.ta.macd(fast=fast, slow=slow, signal=signal)

    def calculate_bollinger_bands(self, length=20, std=2):
        return self.df.ta.bbands(length=length, std=std)
