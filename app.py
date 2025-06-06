from dash import Dash, Input, Output, callback, html, dcc
from utils.data_loader import load_stock_data
import plotly.express as px

df = load_stock_data("data/MSFTSTOCKSHEET.csv")

# Intialise Dash App
app = Dash()


fig = px.line(df, x = "Date", y = "Price", color="Type", title="Microsoft Daily Stock Price")

# App layout
app.layout = [
    html.H1("MSFT Stock Dashboard"),
    dcc.Graph(id='graph-with-slider'),
    dcc.Checklist(
        options=["Open", "Close", "Low", "High"],
        value=["Open", "Close", "Low", "High"],
        id="line-checklist"
    )
]

@callback(
    Output(component_id="graph-with-slider", component_property="figure"),
    Input(component_id="line-checklist", component_property="value")
)
def update_figure(lines_selected) :
    # print(lines_selected)
    filtered_df = df[df['Type'].isin(lines_selected)]
    fig = px.line(filtered_df, x='Date', y="Price", color="Type", title="MSFT Price Moves")
    
    return fig
    


# Run the app
if __name__ == "__main__":
    app.run(debug=True)


