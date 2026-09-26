# Day 148 Worked Examples: Interactive Charts

## Example 1 — Practical: Interactive Candlestick Financial Chart
```python
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=4),
    'Open': [100, 104, 102, 108],
    'High': [106, 107, 109, 112],
    'Low': [98, 101, 100, 105],
    'Close': [104, 102, 108, 110]
})

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'], high=df['High'],
    low=df['Low'], close=df['Close']
)])

fig.update_layout(title="Interactive Stock Candlestick Chart")
fig.write_html("candlestick.html")
print("Saved candlestick.html")
```
