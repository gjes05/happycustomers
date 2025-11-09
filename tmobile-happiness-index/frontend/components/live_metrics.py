from dash import html
import dash_daq as daq

layout = html.Div([
    html.H2("Live Metrics"),
    daq.Gauge(
        id='happiness-gauge',
        label="Overall Happiness Score",
        value=85,
        max=100,
        min=0,
        showCurrentValue=True,
        units="%"
    ),
    html.Div(id='store-performance-table')
])
