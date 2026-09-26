# Day 136 Theory: Bar Charts

### 1. What Is It?
Bar charts represent discrete categorical variables as rectangular bars with lengths proportional to the values they represent.

### 2. Key Syntax
```python
# Vertical Bar:
bars = ax.bar(categories, values, color='skyblue', width=0.6)
ax.bar_label(bars, fmt='%.1f')

# Grouped Bar (X offset):
x = np.arange(len(cats))
width = 0.35
ax.bar(x - width/2, group1, width, label='G1')
ax.bar(x + width/2, group2, width, label='G2')

# Stacked Bar:
ax.bar(cats, group1, label='G1')
ax.bar(cats, group2, bottom=group1, label='G2')
```

### 3. Summary
Bar charts display categorical comparisons, grouped bars facilitate side-by-side sub-category evaluation, and stacked bars show composition.
