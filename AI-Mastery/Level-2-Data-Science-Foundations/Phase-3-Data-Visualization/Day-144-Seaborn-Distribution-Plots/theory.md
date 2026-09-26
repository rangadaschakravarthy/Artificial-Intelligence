# Day 144 Theory: Seaborn Distribution Plots

### 1. What Is It?
Seaborn Distribution Plots provide statistical visualizations for univariate and bivariate continuous feature distributions.

### 2. Key Functions
- **`histplot()`**: Enhanced histogram with optional KDE overlay.
- **`kdeplot()`**: Non-parametric kernel density estimate curve.
- **`ecdfplot()`**: Empirical cumulative distribution function (exact percentiles).
- **`jointplot()`**: Bivariate scatter/KDE plot with marginal 1D distribution plots on top and right axes.

### 3. Syntax
```python
# Histplot + KDE:
sns.histplot(data=df, x='Metric', hue='Group', kde=True, element='step')

# Jointplot:
g = sns.jointplot(data=df, x='X', y='Y', kind='kde', color='purple')
```

### 4. Summary
`histplot()` and `kdeplot()` reveal continuous shapes, while `jointplot()` combines bivariate relationships with marginal distributions.
