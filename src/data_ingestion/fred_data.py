import pandas as pd
from fredapi import Fred

def get_fred_series(series_id, api_key):
    """
    Fetches a single data series from FRED.
    """
    fred = Fred(api_key=api_key)
    data = fred.get_series(series_id)
    df = pd.DataFrame(data, columns=['value'])
    df.index.name = 'date'
    df.index = pd.to_datetime(df.index)
    return df
