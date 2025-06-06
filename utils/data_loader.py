import pandas as pd

def load_stock_data(csvfile: str) :
    df = pd.read_csv(csvfile)
    return df