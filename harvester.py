import json
from scrapers.macro_economic_factors_scraper import scrape_macro_economic_factors
from scrapers.financial_market_factors_scraper import scrape_financial_market_factors
from scrapers.commodity_interactions_scraper import scrape_commodity_interactions
from scrapers.currency_factors_scraper import scrape_currency_factors

def harvest_data():
    """
    Runs all the scrapers and aggregates the data.
    """
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
            "central_bank_net_purchases_tonnes": None
        },
        "macro_economic_factors": {},
        "financial_market_factors": {},
        "geopolitical_factors": {
            "geopolitical_risk_index": None,
            "trade_tariff_rate_percent": None
        },
        "commodity_interactions": {},
        "currency_factors": {},
        "market_sentiment": {
            "investor_risk_aversion_index": None,
            "safe_haven_flow_tonnes": None
        }
    }

    data["macro_economic_factors"].update(scrape_macro_economic_factors())
    data["financial_market_factors"].update(scrape_financial_market_factors())
    data["commodity_interactions"].update(scrape_commodity_interactions())
    data["currency_factors"].update(scrape_currency_factors())

    return data

if __name__ == "__main__":
    gold_data = harvest_data()
    with open("gold_data.json", "w") as f:
        json.dump(gold_data, f, indent=2)
    print("Data harvested and saved to gold_data.json")
