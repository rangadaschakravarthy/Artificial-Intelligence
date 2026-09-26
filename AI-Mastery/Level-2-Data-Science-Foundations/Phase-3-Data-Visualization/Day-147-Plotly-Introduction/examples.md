# Day 147 Worked Examples: Plotly Introduction

## Example 1 — Practical: Plotly Express Interactive Scatter
```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'GDP': [5000, 12000, 35000, 48000],
    'LifeExp': [62, 70, 78, 82],
    'Country': ['Country A', 'Country B', 'Country C', 'Country D'],
    'Population': [10, 45, 12, 85]
})

fig = px.scatter(
    df, x='GDP', y='LifeExp',
    size='Population', color='Country',
    hover_name='Country', title="Interactive GDP vs Life Expectancy"
)

fig.write_html("plotly_scatter.html")
print("Saved plotly_scatter.html")
```
