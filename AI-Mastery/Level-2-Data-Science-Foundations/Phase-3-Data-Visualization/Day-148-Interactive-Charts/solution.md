# Day 148 Solutions: Interactive Charts

## Level 1 — Basic
1. `plotly.graph_objects` (`go`).
2. `fig.add_trace()`.
3. `go.Scatter3d()`.

## Level 2 — Coding
1. `fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])`
2. `fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))`

## Level 3 — Data Analysis
1. Use `plotly.express` for rapid standard plots. Use `plotly.graph_objects` when building custom multi-axis charts, candlestick charts, 3D plots, or adding dynamic UI dropdown menus.
