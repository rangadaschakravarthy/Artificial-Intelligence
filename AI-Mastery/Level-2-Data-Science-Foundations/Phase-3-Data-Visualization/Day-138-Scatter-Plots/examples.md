# Day 138 Worked Examples: Scatter Plots

## Example 1 — Practical: 4D Bubble Chart with Trendline
```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
n = 50
exp = np.random.uniform(1, 10, n)
salary = 40000 + exp * 9000 + np.random.normal(0, 5000, n)
age = np.random.uniform(22, 60, n)
rating = np.random.uniform(50, 500, n)

fig, ax = plt.subplots(figsize=(8, 4.5))
sc = ax.scatter(exp, salary, c=age, s=rating, cmap='plasma', alpha=0.7, edgecolors='black')

# Linear Trendline
z = np.polyfit(exp, salary, 1)
p = np.poly1d(z)
ax.plot(exp, p(exp), "r--", label='Linear Trend')

ax.set_title("Salary vs Experience (Color=Age, Size=Rating)")
ax.set_xlabel("Years Experience")
ax.set_ylabel("Salary ($)")
fig.colorbar(sc, ax=ax, label='Age')
ax.legend()

fig.tight_layout()
fig.savefig("scatter_bubble.png", bbox_inches='tight')
plt.close(fig)
print("Saved scatter_bubble.png")
```
