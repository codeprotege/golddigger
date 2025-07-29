import pandas as pd

def add_macro_features(df, macro_df, macro_feature):
    """
    Merges a macro feature into the main dataframe.
    """
    df = pd.merge(df, macro_df, left_index=True, right_index=True, how='left')
    df[macro_feature] = df[macro_feature].fillna(method='ffill')
    return df
