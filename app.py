from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# 1. Initialize the Dash application instance
app = Dash(__name__)

# 2. Load the processed pink morsel data
df = pd.read_csv('formatted_output.csv')

# 3. Ensure the data is sorted chronologically so the line graph flows smoothly
df = df.sort_values(by='date')

# 4. Construct the Application Layout with customized CSS styling
app.layout = html.Div(
    style={
        'fontFamily': '"Segoe UI", Roboto, Helvetica, Arial, sans-serif',
        'backgroundColor': '#f0f2f5',
        'padding': '40px 20px',
        'minHeight': '100vh',
        'margin': '0'
    },
    children=[
        # App Card Container
        html.Div(
            style={
                'maxWidth': '1100px',
                'margin': '0 auto',
                'backgroundColor': '#ffffff',
                'borderRadius': '16px',
                'boxShadow': '0 8px 24px rgba(0, 0, 0, 0.08)',
                'padding': '40px'
            },
            children=[
                # Styled Header
                html.H1(
                    id='app-header',  # Add this unique identifier
                    children='Soul Foods: Pink Morsel Sales Performance Tracker',
                    style={'textAlign': 'center', 'color': '#1a202c'}
                ),

                # Context Subtitle
                html.P(
                    children="Examine the impact of the January 15th, 2021 price change across retail regions.",
                    style={
                        'textAlign': 'center',
                        'color': '#718096',
                        'fontSize': '1.1rem',
                        'marginBottom': '40px'
                    }
                ),

                # Interactive Radio Button Controls Container
                html.Div(
                    style={
                        'backgroundColor': '#f8fafc',
                        'padding': '20px',
                        'borderRadius': '12px',
                        'border': '1px solid #e2e8f0',
                        'marginBottom': '30px',
                        'textAlign': 'center'
                    },
                    children=[
                        html.Label(
                            'Filter Visualisation by Region:',
                            style={
                                'fontWeight': '600',
                                'color': '#4a5568',
                                'display': 'block',
                                'marginBottom': '12px',
                                'fontSize': '1rem'
                            }
                        ),
                        # Radio items component
                        dcc.RadioItems(
                            id='region-filter',
                            options=[
                                {'label': ' All Regions', 'value': 'all'},
                                {'label': ' North', 'value': 'north'},
                                {'label': ' South', 'value': 'south'},
                                {'label': ' East', 'value': 'east'},
                                {'label': ' West', 'value': 'west'},
                            ],
                            value='all',
                            inline=True
                        ),
                    ]
                ),

                # Graph Placeholder Component
                html.Div(
                    dcc.Graph(
                        id='sales-line-chart'  # Already defined in the previous step
                    )
                )
            ]
        )
    ]
)


# 5. Define Callbacks to dynamically manage user interactions
@app.callback(
    Output(component_id='sales-line-chart', component_property='figure'),
    Input(component_id='region-filter', component_property='value')
)
def update_graph(selected_region):
    # Filter dataset depending on chosen selector value
    if selected_region == 'all':
        filtered_df = df
        chart_title = 'Pink Morsel Sales Performance — All Regions'
    else:
        filtered_df = df[df['region'] == selected_region]
        chart_title = f'Pink Morsel Sales Performance — {selected_region.title()} Region'

    # Generate the line chart configuration
    fig = px.line(
        filtered_df,
        x='date',
        y='Sales',
        title=chart_title,
        labels={'date': 'Transaction Date', 'Sales': 'Total Revenue ($)'},
        template='plotly_white'
    )

    # Add the target marker representing the price adjustment window
    fig.add_vline(
        x='2021-01-15',
        line_width=2,
        line_dash="dash",
        line_color="#e53e3e",
        annotation_text="Price Increase (Jan 15, 2021)",
        annotation_position="top left",
        annotation_font_color="#e53e3e"
    )

    # Modernize chart layout appearance
    fig.update_traces(line=dict(color='#3182ce', width=2.5))
    fig.update_layout(
        title_font_size=18,
        title_font_color='#2d3748',
        hovermode='x unified',
        font=dict(family='"Segoe UI", Roboto, sans-serif')
    )

    return fig


# 6. Initialize local server loop
if __name__ == '__main__':
    app.run(debug=True)
