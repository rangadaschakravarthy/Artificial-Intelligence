# Day 135 Worked Examples: Line Charts

## Example 1 — Practical: Shaded Confidence Interval with fill_between
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 30)
y_mean = 2 * x + 5
y_std = np.random.uniform(1, 3, size=len(x))

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y_mean, color='navy', label='Mean Projection')
ax.fill_between(x, y_mean - y_std, y_mean + y_std, color='blue', alpha=0.2, label='Uncertainty')
ax.set_title("Trend Projection with Shaded Bounds")
ax.legend()
fig.savefig("line_ci.png", bbox_inches='tight')
plt.close(fig)
print("Saved line_ci.png")
```
