from flask import Blueprint, jsonify
from app.services.market_data_fetcher import MarketDataFetcher

price_bp = Blueprint('price', __name__)
market_data_fetcher = MarketDataFetcher()

@price_bp.route('/price/<symbol>', methods=['GET'])
def get_price(symbol):
    price = market_data_fetcher.get_real_time_price(symbol)
    if price:
        return jsonify({'symbol': symbol, 'price': price})
    return jsonify({'message': 'Price not found'}), 404
