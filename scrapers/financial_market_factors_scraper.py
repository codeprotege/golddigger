import yfinance as yf

def scrape_financial_market_factors():
    """
    Scrapes financial market factors data using the yfinance library.
    """
    sp500 = yf.Ticker("^GSPC")
    vix = yf.Ticker("^VIX")
    tnx = yf.Ticker("^TNX")

    sp500_level = sp500.history(period="1d")['Close'].iloc[-1]
    vix_level = vix.history(period="1d")['Close'].iloc[-1]
    us_treasury_yield = tnx.history(period="1d")['Close'].iloc[-1]

    return {
        "sp500_index_level": float(sp500_level),
        "vix_volatility_index_level": float(vix_level),
        "us_treasury_yield_10yr_percent": float(us_treasury_yield),
    }

if __name__ == '__main__':
    data = scrape_financial_market_factors()
    import json
    print(json.dumps(data, indent=2))
