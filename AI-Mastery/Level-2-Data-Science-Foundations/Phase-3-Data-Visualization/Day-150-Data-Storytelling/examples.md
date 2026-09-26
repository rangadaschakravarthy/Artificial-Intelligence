# Day 150 Worked Examples: Data Storytelling

## Example 1 — Practical: Strategic Accent Color & Action Title
```python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 105, 150, 110, 115]

# Gray baseline, Red highlight for March peak
colors = ['#d3d3d3', '#d3d3d3', '#d62728', '#d3d3d3', '#d3d3d3']

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(months, sales, color=colors)

# Action Title
ax.set_title("March Marketing Campaign Drove 40% Sales Spike", fontsize=13, fontweight='bold', pad=15)
ax.set_ylabel("Sales ($K)")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.bar_label(bars, padding=3)

fig.tight_layout()
fig.savefig("data_storytelling.png", bbox_inches='tight')
plt.close(fig)
print("Saved data_storytelling.png")
```
