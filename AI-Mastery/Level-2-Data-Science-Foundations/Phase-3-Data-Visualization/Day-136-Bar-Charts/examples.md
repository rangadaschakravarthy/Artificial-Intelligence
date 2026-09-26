# Day 136 Worked Examples: Bar Charts

## Example 1 — Practical: Grouped Bar Chart with bar_label Annotations
```python
import matplotlib.pyplot as plt
import numpy as np

categories = ['North', 'South', 'East', 'West']
q1_sales = [150, 220, 180, 200]
q2_sales = [170, 240, 210, 190]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 4.5))
rects1 = ax.bar(x - width/2, q1_sales, width, label='Q1 Sales', color='steelblue')
rects2 = ax.bar(x + width/2, q2_sales, width, label='Q2 Sales', color='coral')

ax.set_title("Regional Sales Comparison (Q1 vs Q2)")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.legend()

fig.tight_layout()
fig.savefig("grouped_bar.png", bbox_inches='tight')
plt.close(fig)
print("Saved grouped_bar.png")
```
