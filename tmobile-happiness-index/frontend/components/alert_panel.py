from dash import html

layout = html.Div([
    html.H2("Alert Panel"),
    html.Ul([
        html.Li("Store 105: Happiness score dropped below 60"),
        html.Li("Anomaly detected in voice sentiment for Store 212"),
    ])
])
