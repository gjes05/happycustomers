from dash import html, dcc
import plotly.graph_objects as go

# Sample data - in a real app, this would come from a database
store_locations = {
    "Seattle": {"lat": 47.6062, "lon": -122.3321, "happiness": 92},
    "New York": {"lat": 40.7128, "lon": -74.0060, "happiness": 85},
    "Dallas": {"lat": 32.7767, "lon": -96.7970, "happiness": 78},
}

fig = go.Figure(data=go.Scattergeo(
    lon=[loc["lon"] for loc in store_locations.values()],
    lat=[loc["lat"] for loc in store_locations.values()],
    text=list(store_locations.keys()),
    mode='markers',
    marker=dict(
        size=10,
        color=[loc["happiness"] for loc in store_locations.values()],
        colorscale='Viridis',
        showscale=True,
        cmin=50,
        cmax=100
    )
))

fig.update_layout(
    title_text='Store Happiness Levels',
    geo_scope='usa',
)

layout = html.Div([
    html.H2("Geographic Map"),
    dcc.Graph(figure=fig)
])
