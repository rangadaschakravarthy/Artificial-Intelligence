# Day 142 Worked Examples: Seaborn Introduction

## Example 1 — Practical: Multi-Dimensional Seaborn Scatter Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'Experience': [1, 2, 4, 5, 7, 8, 10],
    'Salary': [45000, 52000, 68000, 75000, 95000, 105000, 130000],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'IT', 'Sales', 'IT'],
    'Gender': ['M', 'F', 'F', 'M', 'M', 'F', 'M']
})

sns.set_theme(style='whitegrid')
fig, ax = plt.subplots(figsize=(8, 4.5))

sns.scatterplot(
    data=df, x='Experience', y='Salary',
    hue='Department', style='Gender', s=100, ax=ax
)

ax.set_title("Salary vs Experience by Dept & Gender (Seaborn)")
fig.savefig("sns_intro.png", bbox_inches='tight')
plt.close(fig)
print("Saved sns_intro.png")
```
