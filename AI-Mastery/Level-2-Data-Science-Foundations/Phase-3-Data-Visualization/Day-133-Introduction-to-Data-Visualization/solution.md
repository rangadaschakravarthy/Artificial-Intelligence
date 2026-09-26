# Day 133 Solutions: Introduction to Data Visualization

## Level 1 — Basic
1. Matplotlib, Seaborn, Plotly.
2. Plotly.
3. Spatial Position (X, Y coordinates).
4. True.
5. It proves that datasets with identical summary statistics can have completely different visual distributions.

## Level 2 — Coding
1.
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.close()
```
2.
```python
plt.title('Sales Trend')
plt.xlabel('Month')
```
3.
```python
import seaborn as sns
sns.set_theme(style='darkgrid')
```
4.
```python
sns.scatterplot(data=df, x='x', y='y')
```
5.
```python
import plotly.express as px
fig = px.bar(df, x='Cat', y='Val')
```

## Level 3 — Data Analysis
1. Matplotlib defaults require custom styling; Seaborn defaults include harmonious palettes and grids out-of-the-box.
2. Position (X, Y), Color (Hue), Size (Marker area).
3. Non-zero baselines exaggerate small relative differences between bar heights artificially.

## Level 4 — Debugging
1. Add `plt.close()` or `plt.clf()` after saving/showing plots.
2. Pass DataFrame `data=df` and column name strings `x='col1'`, `y='col2'`.

## Level 5 — AI/ML Application
1. Plotting training vs validation loss curves over epochs reveals overfitting when validation loss diverges upwards while training loss decreases.

## Level 6 — Interview Questions
1. Stateful `plt.plot()` manages an implicit current figure. Object-oriented `fig, ax = plt.subplots()` returns explicit figure and axes objects, offering far greater control for multi-panel subplots.
