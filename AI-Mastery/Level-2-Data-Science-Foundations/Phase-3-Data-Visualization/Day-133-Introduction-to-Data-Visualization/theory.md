# Day 133 Theory: Introduction to Data Visualization

### 1. What Is It?
Data Visualization is the graphical representation of information and data using visual elements like charts, graphs, maps, and interactive plots.

### 2. Why Does It Exist?
Human brains process visual patterns much faster than tabular numbers. Visualizations make trends, anomalies, distributions, and correlations immediately clear.

### 3. Intuition
- **Matplotlib**: The canvas and paintbrush — ultimate granular control, procedural/object-oriented.
- **Seaborn**: The high-level statistical gallery — beautiful aesthetic defaults, built for Pandas.
- **Plotly**: The interactive web dashboard — dynamic tooltips, zooming, HTML export.

### 4. Syntax Comparison
```python
# Matplotlib
import matplotlib.pyplot as plt
plt.plot(x, y); plt.show()

# Seaborn
import seaborn as sns
sns.scatterplot(data=df, x='x', y='y')

# Plotly
import plotly.express as px
fig = px.scatter(df, x='x', y='y'); fig.show()
```

### 5. Visual Encoding Channels
1. **Position**: X and Y coordinates (strongest cognitive perception channel).
2. **Color**: Hue (categories), Saturation/Brightness (magnitude).
3. **Size**: Area of points/bars (proportional to values).
4. **Shape**: Discrete markers (group separation).

### 6. Summary
Matplotlib offers foundational control, Seaborn provides statistical elegance, and Plotly adds web interactivity.
