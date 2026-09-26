# Day 148 Theory: Interactive Charts

### 1. What Is It?
`plotly.graph_objects` (`go`) provides an explicit object-oriented API for building complex, multi-trace interactive figures and custom controls.

### 2. Syntax
```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close Price'))
fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], name='Volume', yaxis='y2'))

fig.update_layout(
    title="Financial Dashboard",
    xaxis=dict(rangeslider=dict(visible=True))
)
fig.write_html("financial_dashboard.html")
```

### 3. Summary
`go.Figure()` and `add_trace()` enable custom multi-layer interactive plots and 3D visualizations.
