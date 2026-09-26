# Day 143 Theory: Seaborn Categorical Plots

### 1. What Is It?
Seaborn Categorical Plots visualize relationships between continuous numerical metrics and one or more discrete categorical variables.

### 2. Plot Types
- **`countplot()`**: Counts observations per category.
- **`barplot()`**: Computes group means with error bars.
- **`boxplot()`**: Displays 5-number quartile summaries.
- **`violinplot()`**: Combines a box plot with a Kernel Density Estimate (KDE) curve.
- **`swarmplot()`**: Plots every individual observation point without overlap.

### 3. Syntax
```python
sns.violinplot(data=df, x='Category', y='Metric', hue='Group', split=True, inner='quartile')
sns.stripplot(data=df, x='Category', y='Metric', color='black', alpha=0.3, jitter=True)
```

### 4. Summary
Violin plots show distribution shape and density, while swarm plots display raw individual points.
