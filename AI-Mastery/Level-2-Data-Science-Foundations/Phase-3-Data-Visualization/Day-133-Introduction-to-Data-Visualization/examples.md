# Day 133 Worked Examples: Introduction to Data Visualization

## Example 1 — Beginner: Matplotlib Simple Plot
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Simple Matplotlib Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig("plt_basic.png")
plt.close()
print("Saved plt_basic.png")
```

## Example 2 — Practical: Seaborn Statistical Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'Age': [20, 25, 30, 35, 40], 'Income': [30000, 45000, 50000, 70000, 90000]})

sns.scatterplot(data=df, x='Age', y='Income', hue='Age', palette='viridis')
plt.title("Seaborn Scatter Plot")
plt.savefig("sns_basic.png")
plt.close()
print("Saved sns_basic.png")
```

## Example 3 — Intermediate: Plotly Interactive Express Plot
```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({'X': [1, 2, 3], 'Y': [10, 20, 15], 'Cat': ['A', 'B', 'A']})
fig = px.scatter(df, x='X', y='Y', color='Cat', title="Plotly Interactive Scatter")
# fig.show() in notebooks or fig.write_html("plotly_basic.html")
print("Plotly Figure Created Successfully!")
```
