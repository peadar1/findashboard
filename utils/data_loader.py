import pandas as pd

def load_stock_data(csvfile: str) :
    df = pd.read_csv(csvfile)
    df["Date"] = pd.to_datetime(df["Date"])
    # Melt into longform
    df = pd.melt(df, id_vars=["Date"], var_name="Type", value_name="Price", value_vars=["Close", "High", "Low", "Open"])
    df = df.sort_values("Date")
    return df