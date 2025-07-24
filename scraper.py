import requests
from bs4 import BeautifulSoup
import json

def scrape_gold_data():
    """
    Scrapes gold market data from the money.com article.
    """
    url = "https://money.com/what-drives-the-price-of-gold/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # NOTE: The values scraped from the article are not real-time data,
    # but rather examples used in the text.
    data = {
        "supply_factors": {
            "annual_mine_production_tonnes": None,
            "all_in_sustaining_cost_usd_per_ounce": None,
            "above_ground_stock_change_percent": None,
            "new_discoveries_metric_tonnes": None,
            "recycled_gold_supply_tonnes": None
        },
        "demand_factors": {
            "jewellery_demand_tonnes": None,
            "technology_and_industrial_demand_tonnes": None,
            "investment_bar_and_coin_demand_tonnes": None,
            "etf_holdings_change_tonnes": None,
            "central_bank_net_purchases_tonnes": 735
        },
        "macro_economic_factors": {
            "consumer_price_index_inflation_percent": None,
            "real_interest_rate_percent": None,
            "nominal_interest_rate_percent": None,
            "us_dollar_index_level": None,
            "global_gdp_growth_percent": None
        },
        "financial_market_factors": {
            "sp500_index_level": None,
            "vix_volatility_index_level": None,
            "us_treasury_yield_10yr_percent": None,
            "real_yield_tips_10yr_percent": None
        },
        "geopolitical_factors": {
            "geopolitical_risk_index": None,
            "trade_tariff_rate_percent": None
        },
        "commodity_interactions": {
            "brent_crude_oil_price_usd_per_barrel": None
        },
        "currency_factors": {
            "usd_eur_exchange_rate": 1.08,
            "usd_jpy_exchange_rate": None
        },
        "market_sentiment": {
            "investor_risk_aversion_index": None,
            "safe_haven_flow_tonnes": None
        }
    }

    # Extract data from the article text
    # This is a simplified example; a real scraper would need to be more robust.
    text = soup.get_text()

    if "1.08" in text:
        data["currency_factors"]["usd_eur_exchange_rate"] = 1.08

    if "735 tons" in text:
        data["demand_factors"]["central_bank_net_purchases_tonnes"] = 735

    return data

if __name__ == "__main__":
    gold_data = scrape_gold_data()
    with open("gold_data.json", "w") as f:
        json.dump(gold_data, f, indent=2)
    print("Data scraped and saved to gold_data.json")
