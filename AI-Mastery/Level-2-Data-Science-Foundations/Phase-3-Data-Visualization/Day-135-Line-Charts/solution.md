# Day 135 Solutions: Line Charts

## Level 1 — Basic
1. An ordered, continuous variable (e.g. Time, Date, Sequence).
2. `ax.fill_between()`.
3. `ax.twinx()`.

## Level 2 — Coding
1. `ax.plot(x, y, color='green', linestyle='--', marker='o')`
2. `ax.fill_between(x, y1, y2, alpha=0.3)`

## Level 3 — Data Analysis
1.
```python
fig, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(months, rev, color='blue', label='Revenue')
ax2 = ax1.twinx()
ax2.plot(months, margin, color='red', label='Margin %')
```
