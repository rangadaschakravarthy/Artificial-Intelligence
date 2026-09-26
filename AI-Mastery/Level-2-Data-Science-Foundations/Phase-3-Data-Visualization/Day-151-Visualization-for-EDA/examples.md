# Day 151 Worked Examples: Visualization for EDA

## Example 1 — Practical: Visualizing Missing Data Patterns
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, np.nan, 4, 5],
    'C': [1, 2, 3, 4, 5]
})

fig, ax = plt.subplots(figsize=(6, 3))
sns.heatmap(df.isnull(), cbar=False, cmap='binary', ax=ax)
ax.set_title("Missing Data Null Matrix Plot")

fig.savefig("missing_null_matrix.png", bbox_inches='tight')
plt.close(fig)
print("Saved missing_null_matrix.png")
```
