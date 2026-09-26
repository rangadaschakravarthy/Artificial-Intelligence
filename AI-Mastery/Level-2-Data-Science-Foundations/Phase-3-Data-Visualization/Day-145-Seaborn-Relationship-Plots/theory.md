# Day 145 Theory: Seaborn Relationship Plots

### 1. What Is It?
Seaborn Relationship Plots visualize continuous mathematical associations and regression trends across pairs of variables, faceted by categorical sub-groups.

### 2. Key Functions
- **`pairplot()`**: Draws a matrix of pairwise scatter plots for all numerical columns in a DataFrame, with histograms on the diagonal.
- **`lmplot()`**: Combines scatter plots with linear regression fit lines and 95% confidence intervals, supporting grid faceting (`col`, `row`).
- **`regplot()`**: Low-level axes-level regression plot.

### 3. Syntax
```python
# Pair Plot:
sns.pairplot(df, hue='Species', corner=True, palette='viridis')

# Faceted Regression Plot:
sns.lmplot(data=df, x='Feature_X', y='Target', hue='Category', col='Region')
```

### 4. Summary
`pairplot()` explores all pairwise feature combinations, while `lmplot()` fits linear regression trends across faceted categorical subsets.
