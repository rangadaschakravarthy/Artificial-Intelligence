# Day 135 Theory: Line Charts

### 1. What Is It?
A Line Chart displays data points connected by straight line segments, visualizing continuous change over an ordered independent variable (typically time).

### 2. When to Use
- Tracking metrics over time (sales trends, stock prices).
- Visualizing continuous functions or mathematical models.
- Comparing multiple continuous time-series series.

### 3. Key Syntax
```python
# Multi-line with shaded confidence interval:
ax.plot(x, y_mean, color='blue', label='Mean')
ax.fill_between(x, y_lower, y_upper, color='blue', alpha=0.2, label='95% CI')

# Dual Y-Axis:
ax2 = ax.twinx()
ax2.plot(x, secondary_y, color='red')
```

### 4. Summary
Line charts represent continuous trends, while `fill_between()` adds confidence intervals and `twinx()` accommodates multi-scale metrics.
