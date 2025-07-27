import yfinance as yf
import pandas as pd

def get_xauusd_data(period, interval):
    """Fetches XAUUSD data from Yahoo Finance."""
    ticker = "GC=F"  # Gold futures ticker
    data = yf.download(tickers=ticker, period=period, interval=interval)
    return data

def calculate_momentum(data, period=1):
    """Calculates the Rate of Change (ROC) momentum."""
    data['momentum'] = (data['Close'] / data['Close'].shift(period) - 1) * 100
    return data

def analyze_momentum():
    """Analyzes and displays XAUUSD momentum for different timeframes."""
    timeframes = {
        "1 Minute": ("2d", "1m"),
        "5 Minutes": ("5d", "5m"),
        "1 Day": ("1mo", "1d"),
        "3 Days": ("3mo", "1d"), # Note: yfinance might not support 3d interval directly
        "5 Days": ("6mo", "5d"),
        "1 Month": ("5y", "1mo")
    }

    print("XAUUSD Momentum Analysis")
    print("="*40)

    for name, (period, interval) in timeframes.items():
        print(f"Analyzing {name} data...")
        try:
            data = get_xauusd_data(period, interval)
            if not data.empty:
                data = calculate_momentum(data)
                last_momentum = data['momentum'].iloc[-1]
                print(f"  - Latest Momentum: {last_momentum:.2f}%")
            else:
                print("  - No data found for this timeframe.")
        except Exception as e:
            print(f"  - Error fetching or analyzing data: {e}")
        print("-" * 20)

if __name__ == "__main__":
    analyze_momentum()
