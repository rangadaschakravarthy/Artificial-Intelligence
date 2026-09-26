# Day 140 Theory: Subplots

### 1. What Is It?
Subplots arrange multiple individual `Axes` drawing regions inside a single parent `Figure` grid.

### 2. Syntax & Indexing
```python
# 2x2 Grid:
fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=False)

# Access individual subplots:
axes[0, 0].plot(x, y) # Top-Left
axes[0, 1].bar(cats, vals) # Top-Right
axes[1, 0].hist(data) # Bottom-Left
axes[1, 1].scatter(x, y) # Bottom-Right

fig.tight_layout()
```

### 3. Summary
`plt.subplots(r, c)` creates structured multi-chart panels, while `sharex`/`sharey` enforce consistent scaling across comparative plots.
