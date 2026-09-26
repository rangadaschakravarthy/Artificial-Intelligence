# Day 147 Theory: Plotly Introduction

### 1. What Is It?
Plotly is an open-source interactive graphing library that renders web-based charts using D3.js and WebGL.

### 2. Plotly Express Syntax
```python
import plotly.express as px

fig = px.scatter(
    df, x='GDP', y='LifeExpectancy',
    color='Continent', size='Population',
    hover_name='Country', title="Global Indicators"
)
# Save interactive HTML file:
fig.write_html("plotly_chart.html")
```

### 3. Summary
Plotly Express generates interactive web-based charts with hover tooltips and dynamic zooming out-of-the-box.
