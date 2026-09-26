# Day 146 Worked Examples: Seaborn Heatmaps

## Example 1 — Practical: Masked Correlation Heatmap
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame(np.random.randn(100, 5), columns=['Age', 'Income', 'Score', 'Tenure', 'Spend'])
df['Spend'] = df['Income'] * 0.7 + np.random.randn(100) * 0.3 # Add correlation

corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='vlag', vmin=-1, vmax=1, linewidths=0.5, ax=ax)
ax.set_title("Pearson Feature Correlation Matrix")

fig.savefig("heatmap_corr.png", bbox_inches='tight')
plt.close(fig)
print("Saved heatmap_corr.png")
```
