import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import requests
from frontend.components import live_metrics, geographic_map, alert_panel

app = dash.Dash(__name__, suppress_callback_exceptions=True)

API_URL = "http://127.0.0.1:8000"

app.layout = html.Div([
    html.H1("T-Mobile Customer Happiness Index"),
    html.Button('Generate and Process New Data', id='trigger-button', n_clicks=0),
    dcc.Interval(
        id='interval-component',
        interval=5*1000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='live-metrics-container'),
    html.Div(id='geographic-map-container'),
    html.Div(id='alert-panel-container')
])

@app.callback(
    Output('trigger-button', 'style'), # Just to give some feedback
    [Input('trigger-button', 'n_clicks')]
)
def trigger_data_processing(n_clicks):
    if n_clicks > 0:
        try:
            requests.post(f"{API_URL}/api/data")
            return {'backgroundColor': '#d4edda'}
        except requests.exceptions.RequestException as e:
            print(f"Error triggering data processing: {e}")
            return {'backgroundColor': '#f8d7da'}
    return {}

@app.callback(
    [Output('live-metrics-container', 'children'),
     Output('alert-panel-container', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_dashboard(n):
    try:
        response = requests.get(f"{API_URL}/api/dashboard-data")
        response.raise_for_status()
        data = response.json()

        # Update Live Metrics
        live_metrics.layout.children[1].value = data.get('latest_score', 0)

        # Update Alert Panel
        alert_panel.layout.children[1].children = [
            html.Li(alert) for alert in data.get('alerts', [])
        ]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching dashboard data: {e}")
        # Return empty or error state for components
        return live_metrics.layout, alert_panel.layout

    # The geographic map is static for now, so we don't update it
    return live_metrics.layout, alert_panel.layout

if __name__ == '__main__':
    app.run_server(debug=True, port=8051) # Use a different port to avoid conflict with backend
