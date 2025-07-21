import streamlit as st
import pandas as pd
import requests

st.title('Gold Trading System Dashboard')

# Real-time price
st.header('Real-time Gold Price')
symbol = 'XAU'
try:
    response = requests.get(f'http://127.0.0.1:5000/api/price/{symbol}')
    if response.status_code == 200:
        price_data = response.json()
        st.write(f"The current price of {price_data['symbol']} is ${price_data['price']:.2f}")
    else:
        st.error("Could not fetch real-time price.")
except requests.exceptions.ConnectionError:
    st.error("Could not connect to the API. Make sure the Flask app is running.")


# Historical data
st.header('Historical Gold Prices')
# In a real app, you would fetch this from your database or a service
chart_data = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
    'price': [1824.25, 1836.70, 1854.30, 1834.50]
})
st.line_chart(chart_data.rename(columns={'date':'index'}).set_index('index'))

# Portfolio
st.header('Portfolio')
# In a real app, you would fetch this from your database or a service
portfolio_data = {
    'Cash': 10000,
    'Gold (XAU)': 5
}
st.write(portfolio_data)

# Recent Transactions
st.header('Recent Transactions')
# In a real app, you would fetch this from your database or a service
transactions_data = pd.DataFrame({
    'Date': ['2023-01-04', '2023-01-03'],
    'Symbol': ['XAU', 'XAU'],
    'Type': ['Sell', 'Buy'],
    'Amount': [2, 3],
    'Price': [1834.50, 1854.30]
})
st.write(transactions_data)
