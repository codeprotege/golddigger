import yfinance as yf

def scrape_commodity_interactions():
    """
    Scrapes commodity interactions data using the yfinance library.
    """
    brent = yf.Ticker("BZ=F")

    brent_price = brent.history(period="1d")['Close'].iloc[-1]

    return {
        "brent_crude_oil_price_usd_per_barrel": float(brent_price),
    }

if __name__ == '__main__':
    data = scrape_commodity_interactions()
    import json
    print(json.dumps(data, indent=2))
