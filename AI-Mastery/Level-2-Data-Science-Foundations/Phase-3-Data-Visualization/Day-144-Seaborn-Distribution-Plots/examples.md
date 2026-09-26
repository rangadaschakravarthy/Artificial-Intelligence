# Day 144 Worked Examples: Seaborn Distribution Plots

## Example 1 — Practical: Jointplot with Marginal KDE Curves
```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
mean = [50, 100]
cov = [[100, 45], [45, 200]]
x, y = np.random.multivariate_normal(mean, cov, 300).T

df = pd.DataFrame({'Feature_A': x, 'Feature_B': y})

g = sns.jointplot(data=df, x='Feature_A', y='Feature_B', kind='kde', fill=True, cmap='Blues')
g.fig.suptitle("Bivariate Joint KDE with Marginal Distributions", y=1.02)
g.savefig("joint_kde.png", bbox_inches='tight')
plt.close()
print("Saved joint_kde.png")
```
