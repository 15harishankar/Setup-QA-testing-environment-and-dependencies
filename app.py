import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load your processed CSV
df = pd.read_csv("processed_sales.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Create a line chart
fig = px.line(df, x='Date', y='Sales', color='Region', title='Pink Morsel Sales Over Time')
fig.update_layout(xaxis_title='Date', yaxis_title='Total Sales')

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == '__main__':
    app.run_server(debug=True)
