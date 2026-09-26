# Day 137 Worked Examples: Histograms

## Example 1 — Practical: Normalized Histogram with Overlay PDF
```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

np.random.seed(42)
data = np.random.normal(loc=100, scale=15, size=1000)

fig, ax = plt.subplots(figsize=(8, 4.5))
count, bins, ignored = ax.hist(data, bins=30, density=True, alpha=0.6, color='steelblue', edgecolor='black')

# Gaussian PDF overlay
x = np.linspace(bins.min(), bins.max(), 100)
pdf = norm.pdf(x, loc=100, scale=15)
ax.plot(x, pdf, 'r-', linewidth=2, label='Normal PDF')

ax.set_title("Customer Spend Distribution (Density Normalized)")
ax.set_xlabel("Spend Amount ($)")
ax.set_ylabel("Probability Density")
ax.legend()

fig.tight_layout()
fig.savefig("hist_density.png", bbox_inches='tight')
plt.close(fig)
print("Saved hist_density.png")
```
