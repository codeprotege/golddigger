"""
This script outlines trading strategies for XAU/USD for different trading styles.

Disclaimer: This is for educational purposes only and not financial advice.
"""

def get_scalping_strategy():
    """
    Outlines a scalping strategy for XAU/USD.
    """
    strategy = {
        "name": "XAU/USD Scalping",
        "timeframe": "1-minute to 5-minute charts",
        "indicators": ["Moving Average (MA) 50", "Stochastic Oscillator (5,3,3)"],
        "entry_logic": "Look for price to be above the 50 MA. Enter on a stochastic crossover from oversold territory.",
        "exit_logic": "Exit on a stochastic crossover from overbought territory, or a fixed take-profit of 10-20 pips.",
        "risk_management": "Stop-loss of 5-10 pips below the entry."
    }
    return strategy

def get_day_trading_strategy():
    """
    Outlines a day trading strategy for XAU/USD.
    """
    strategy = {
        "name": "XAU/USD Day Trading",
        "timeframe": "15-minute to 1-hour charts",
        "indicators": ["Relative Strength Index (RSI) 14", "MACD (12,26,9)"],
        "entry_logic": "Enter when RSI is oversold (below 30) and MACD line crosses above the signal line.",
        "exit_logic": "Exit when RSI is overbought (above 70) or MACD line crosses below the signal line.",
        "risk_management": "Stop-loss below a recent swing low, or a fixed 30-50 pips."
    }
    return strategy

def get_swing_trading_strategy():
    """
    Outlines a swing trading strategy for XAU/USD.
    """
    strategy = {
        "name": "XAU/USD Swing Trading",
        "timeframe": "4-hour to daily charts",
        "indicators": ["Fibonacci Retracement", "Ichimoku Cloud"],
        "entry_logic": "Identify a clear trend. Look for a pullback to a Fibonacci level (e.g., 50% or 61.8%) that coincides with support from the Ichimoku Cloud. Enter on a bullish candle confirmation.",
        "exit_logic": "Exit at a previous swing high or a key resistance level.",
        "risk_management": "Stop-loss below the recent swing low and the Ichimoku Cloud."
    }
    return strategy

def display_strategy(strategy):
    """Prints the strategy in a readable format."""
    print(f"--- {strategy['name']} ---")
    print(f"Timeframe: {strategy['timeframe']}")
    print(f"Indicators: {', '.join(strategy['indicators'])}")
    print(f"Entry Logic: {strategy['entry_logic']}")
    print(f"Exit Logic: {strategy['exit_logic']}")
    print(f"Risk Management: {strategy['risk_management']}")

if __name__ == '__main__':
    display_strategy(get_scalping_strategy())
    print()
    display_strategy(get_day_trading_strategy())
    print()
    display_strategy(get_swing_trading_strategy())

    print("\n--- Summary ---")
    print("This script provides a basic framework for creating automated trading strategies for XAU/USD.")
    print("Remember to backtest these strategies thoroughly before deploying them with real capital.")
