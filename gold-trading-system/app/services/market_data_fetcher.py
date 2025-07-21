import random

class MarketDataFetcher:
    def get_real_time_price(self, symbol):
        # Mock implementation
        if symbol == 'XAU':
            return 1800 + random.uniform(-10, 10)
        return None

    def get_historical_data(self, symbol, start_date, end_date):
        # Mock implementation
        prices = []
        current_price = 1800
        from datetime import timedelta, date

        daterange = lambda start_date, end_date: (start_date + timedelta(n) for n in range(int((end_date - start_date).days)))

        for single_date in daterange(start_date, end_date):
            current_price += random.uniform(-5, 5)
            prices.append({'date': single_date, 'price': current_price})
        return prices
