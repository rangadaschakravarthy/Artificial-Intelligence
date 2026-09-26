# Day 152 Worked Examples: Visualization Mini Project

## Complete Workflow Code Structure Overview
```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

# Load & Clean
df = pd.DataFrame({...})

# Static Seaborn Suite
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
sns.histplot(df['Age'], ax=axes[0,0])
sns.boxplot(data=df, x='Group', y='Spend', ax=axes[0,1])
sns.scatterplot(data=df, x='Age', y='Spend', ax=axes[1,0])
sns.heatmap(df.corr(numeric_only=True), annot=True, ax=axes[1,1])
fig.tight_layout()
fig.savefig("static_dashboard.png")

# Interactive Plotly Suite
fig_px = px.scatter(df, x='Age', y='Spend', color='Group')
fig_px.write_html("interactive_dashboard.html")
```
