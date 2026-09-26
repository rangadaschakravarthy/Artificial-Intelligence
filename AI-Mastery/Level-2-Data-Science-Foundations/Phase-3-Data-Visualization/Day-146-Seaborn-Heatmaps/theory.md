# Day 146 Theory: Seaborn Heatmaps

### 1. What Is It?
A Heatmap represents values in a 2D matrix as colors, providing an immediate visual summary of numerical magnitude across row/column categories.

### 2. Syntax & Upper Triangle Masking
```python
corr = df.corr(numeric_only=True)
mask = np.triu(np.ones_like(corr, dtype=bool))

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(
    corr, mask=mask, annot=True, fmt='.2f',
    cmap='coolwarm', vmin=-1, vmax=1,
    linewidths=0.5, ax=ax
)
```

### 3. Summary
Heatmaps turn numeric correlation matrices and pivot tables into intuitive color-coded grids.
