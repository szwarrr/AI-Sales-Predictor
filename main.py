import pandas as pd

def load_and_merge_data(sales_path, features_path, stores_path):
    sales = pd.read_csv(sales_path, parse_dates=['Date'])
    features = pd.read_csv(features_path, parse_dates=['Date'])
    stores = pd.read_csv(stores_path)

    df = pd.merge(sales, features, on=['Store', 'Date'], how='left')
    df = pd.merge(df, stores, on='Store', how='left')

    return df