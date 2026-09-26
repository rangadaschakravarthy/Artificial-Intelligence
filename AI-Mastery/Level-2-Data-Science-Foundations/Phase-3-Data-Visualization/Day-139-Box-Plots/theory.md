# Day 139 Theory: Box Plots

### 1. What Is It?
A Box Plot (Box-and-Whisker Plot) graphically depicts numerical data groups through their quartiles, highlighting median values, dispersion, and statistical outliers.

### 2. Anatomy
- **Box Limits**: First Quartile (Q1, 25th percentile) to Third Quartile (Q3, 75th percentile).
- **Internal Line**: Median (Q2, 50th percentile).
- **Interquartile Range (IQR)**: $	ext{IQR} = 	ext{Q3} - 	ext{Q1}$.
- **Whiskers**: Extend to furthest data points within $[	ext{Q1} - 1.5	ext{IQR}, 	ext{Q3} + 1.5	ext{IQR}]$.
- **Fliers (Outliers)**: Points plotted individually outside whisker bounds.

### 3. Syntax
```python
bp = ax.boxplot(data_list, labels=categories, patch_artist=True, notch=True)
```

### 4. Summary
Box plots summarize statistical quartiles and flag extreme outliers visually.
