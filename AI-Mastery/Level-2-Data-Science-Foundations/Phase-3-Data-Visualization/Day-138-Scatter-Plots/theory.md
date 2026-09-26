# Day 138 Theory: Scatter Plots

### 1. What Is It?
A Scatter Plot displays values for two continuous variables as points on a Cartesian coordinate plane, revealing relationship patterns, clusters, and outliers.

### 2. Multi-Dimensional Encoding
- **X / Y**: Primary bivariate numerical relationship.
- **Color (`c`)**: Third dimension (categorical or continuous heatmap via `cmap`).
- **Size (`s`)**: Fourth dimension (magnitude scaling).

### 3. Syntax
```python
sc = ax.scatter(x, y, c=z, s=sizes, cmap='viridis', alpha=0.7)
cbar = fig.colorbar(sc, ax=ax)
cbar.set_label('Color Dimension Metric')
```

### 4. Summary
Scatter plots display continuous correlation, clusters, and multi-dimensional bubble features.
