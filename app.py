from dash import Dash, html, dcc
from utils.data_loader import load_stock_data

df = load_stock_data("data/MSFTSTOCKSHEET.csv")

# Intialise Dash App
app = Dash()

print(df.head())

# App layout
app.layout = [
    html.H1("MSFT Stock Dashboard")
]


# Run the app
if __name__ == "__main__":
    app.run(debug=True)


