# Day 139 Worked Examples: Box Plots

## Example 1 — Practical: Comparative Box Plot with Custom Styles
```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
dept_a = np.random.normal(60, 10, 100)
dept_b = np.random.normal(75, 15, 100)
dept_c = np.random.normal(50, 5, 100)
# Add outliers
dept_b = np.append(dept_b, [130, 140, 10])

fig, ax = plt.subplots(figsize=(8, 4.5))
bp = ax.boxplot([dept_a, dept_b, dept_c], labels=['IT', 'Sales', 'HR'], patch_artist=True, notch=True)

colors = ['skyblue', 'lightgreen', 'pink']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title("Salary Distributions Across Departments")
ax.set_ylabel("Salary ($K)")
ax.grid(True, axis='y', linestyle='--', alpha=0.5)

fig.tight_layout()
fig.savefig("boxplot_dept.png", bbox_inches='tight')
plt.close(fig)
print("Saved boxplot_dept.png")
```
