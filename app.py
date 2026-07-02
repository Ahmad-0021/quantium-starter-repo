from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# 1. Initialize the Dash application instance
app = Dash(__name__)

# 2. Load the processed pink morsel data
df = pd.read_csv('formatted_output.csv')

# 3. Sort your sales data chronologically so the line graph flows correctly
df = df.sort_values(by='date')

# 4. Create the interactive line chart using Plotly Express
fig = px.line(
    df,
    x='date',
    y='Sales',
    title='Pink Morsel Sales Performance (Over Time)',
    labels={'date': 'Transaction Date', 'Sales': 'Total Sales ($)'},
    template='plotly_white'
)

# 5. Add a visual marker for the price increase date (January 15, 2021)
fig.add_vline(
    x='2021-01-15',
    line_width=2,
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase (Jan 15, 2021)",
    annotation_position="top left"
)

# Customize the chart line style
fig.update_traces(line=dict(color='#2c3e50', width=2))

# 6. Construct the visual layout of your web application
app.layout = html.Div(
    style={'fontFamily': 'Arial, sans-serif', 'padding': '20px', 'backgroundColor': '#f8f9fa'},
    children=[
        # App Header
        html.H1(
            children='Soul Foods: Pink Morsel Visualiser',
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
        ),

        # Sub-header explaining the objective
        html.P(
            children="Tracking sales data before and after the price adjustment on January 15th, 2021.",
            style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '16px'}
        ),

        # Graph Component
        html.Div(
            dcc.Graph(
                id='sales-line-chart',
                figure=fig
            ),
            style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px',
                   'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'}
        )
    ]
)

# 7. Run the local server (Fixed method name for newer Dash versions)
if __name__ == '__main__':
    app.run(debug=True)
