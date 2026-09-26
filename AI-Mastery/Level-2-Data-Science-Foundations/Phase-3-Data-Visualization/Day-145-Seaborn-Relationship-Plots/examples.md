# Day 145 Worked Examples: Seaborn Relationship Plots

## Example 1 — Practical: Pair Plot for Multi-Feature Inspection
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'F1': np.random.randn(100),
    'F2': np.random.randn(100),
    'F3': np.random.randn(100),
    'Class': np.random.choice(['Alpha', 'Beta'], 100)
})

# Add correlation
df['F2'] = df['F1'] * 0.8 + np.random.randn(100) * 0.3

g = sns.pairplot(df, hue='Class', corner=True, palette='Dark2')
g.fig.suptitle("Pairwise Feature Matrix (Corner Masked)", y=1.02)
g.savefig("pairplot_matrix.png", bbox_inches='tight')
plt.close()
print("Saved pairplot_matrix.png")
```
