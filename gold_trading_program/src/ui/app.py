from flask import Flask, render_template, jsonify
from ..data_ingestion.data_fetcher import DataFetcher
from ..data_processing.data_processor import DataProcessor
from ..analytics.technical_analyzer import TechnicalAnalyzer
from ..trading.trader import Trader
from ..trading.brokerage import AlpacaBrokerage

app = Flask(__name__)

# Initialize components
fetcher = DataFetcher(api_key="YOUR_API_KEY")
brokerage = AlpacaBrokerage()
trader = Trader(brokerage_api=brokerage)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', price="N/A", signal="N/A", position="N/A")

@app.route('/data')
def get_data():
    raw_data = fetcher.get_gold_price()
    if raw_data:
        processor = DataProcessor(raw_data)
        processed_df = processor.process_data()

        if not processed_df.empty:
            price = f"${processed_df.iloc[0]['exchange_rate']:.2f}"

            analyzer = TechnicalAnalyzer(data=processed_df.copy())
            analyzer.calculate_sma(window=10)
            analyzer.calculate_rsi(window=14)
            analyzed_df = analyzer.data

            latest_data = analyzed_df.iloc[-1]
            if latest_data['exchange_rate'] > latest_data['sma'] and latest_data['rsi'] < 30:
                signal = "Buy"
                trader.place_order("XAUUSD", 1, "buy")
            elif latest_data['exchange_rate'] < latest_data['sma'] and latest_data['rsi'] > 70:
                signal = "Sell"
                trader.place_order("XAUUSD", 1, "sell")
            else:
                signal = "Hold"

            position = trader.get_position("XAUUSD")

            return jsonify(price=price, signal=signal, position=position)

    return jsonify(price="Error", signal="Error", position="Error")

if __name__ == '__main__':
    app.run(debug=True)
