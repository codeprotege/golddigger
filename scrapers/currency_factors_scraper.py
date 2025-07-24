import yfinance as yf

def scrape_currency_factors():
    """
    Scrapes currency factors data using the yfinance library.
    """
    eurusd = yf.Ticker("EURUSD=X")
    usdjpy = yf.Ticker("JPY=X")

    eurusd_rate = eurusd.history(period="1d")['Close'].iloc[-1]
    usdjpy_rate = usdjpy.history(period="1d")['Close'].iloc[-1]

    return {
        "usd_eur_exchange_rate": float(eurusd_rate),
        "usd_jpy_exchange_rate": float(usdjpy_rate),
    }

if __name__ == '__main__':
    data = scrape_currency_factors()
    import json
    print(json.dumps(data, indent=2))
