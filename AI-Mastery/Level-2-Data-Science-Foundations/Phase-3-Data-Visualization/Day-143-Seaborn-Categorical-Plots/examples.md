# Day 143 Worked Examples: Seaborn Categorical Plots

## Example 1 — Practical: Violin Plot with Split Hue
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'Department': ['IT']*50 + ['Sales']*50,
    'Gender': np.random.choice(['M', 'F'], 100),
    'Salary': np.concatenate([np.random.normal(90, 10, 50), np.random.normal(70, 15, 50)])
})

fig, ax = plt.subplots(figsize=(8, 4.5))
sns.violinplot(data=df, x='Department', y='Salary', hue='Gender', split=True, inner='quartile', palette='Set2', ax=ax)

ax.set_title("Salary Distribution by Department & Gender (Split Violin)")
fig.savefig("violin_split.png", bbox_inches='tight')
plt.close(fig)
print("Saved violin_split.png")
```
