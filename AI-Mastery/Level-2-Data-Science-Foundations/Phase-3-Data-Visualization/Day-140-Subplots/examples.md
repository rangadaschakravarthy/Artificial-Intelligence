# Day 140 Worked Examples: Subplots

## Example 1 — Practical: 2x2 Dashboard Grid
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Top-Left: Line
axes[0, 0].plot(x, np.sin(x), color='blue')
axes[0, 0].set_title("Sine Wave")

# Top-Right: Bar
axes[0, 1].bar(['A', 'B', 'C'], [10, 20, 15], color='green')
axes[0, 1].set_title("Category Bar")

# Bottom-Left: Histogram
axes[1, 0].hist(np.random.randn(500), bins=20, color='purple', alpha=0.7)
axes[1, 0].set_title("Normal Distribution")

# Bottom-Right: Scatter
axes[1, 1].scatter(x, x + np.random.randn(50), color='orange')
axes[1, 1].set_title("Scatter Correlation")

fig.tight_layout()
fig.savefig("dashboard_grid.png", bbox_inches='tight')
plt.close(fig)
print("Saved dashboard_grid.png")
```
