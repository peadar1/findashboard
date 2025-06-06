from dash import Dash, html, dcc
from utils.data_loader import load_stock_data
import plotly.express as px

df = load_stock_data("data/MSFTSTOCKSHEET.csv")

# Intialise Dash App
app = Dash()


fig = px.line(df, x = "Date", y = "Price", color="Type", title="Microsoft Daily Stock Price")

# App layout
app.layout = [
    html.H1("MSFT Stock Dashboard"),
    dcc.Graph(figure=fig)
]


# Run the app
if __name__ == "__main__":
    app.run(debug=True)


