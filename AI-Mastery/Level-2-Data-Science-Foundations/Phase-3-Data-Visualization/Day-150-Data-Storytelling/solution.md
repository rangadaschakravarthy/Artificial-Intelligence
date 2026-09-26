# Day 150 Solutions: Data Storytelling

## Level 1 — Basic
1. $	ext{Data-to-Ink Ratio} = 	ext{Data Ink} / 	ext{Total Ink Used to Print Graphic}$.
2. A headline title that explicitly summarizes the primary takeaway or business finding instead of just describing the axes.
3. Use neutral gray for background elements and a single high-contrast accent color to direct viewer focus to the key narrative point.

## Level 2 — Coding
1.
```python
colors = ['gray' if v < max(vals) else 'blue' for v in vals]
ax.bar(cats, vals, color=colors)
```

## Level 3 — Data Analysis
1. Strip background gridlines, remove outer spines, gray out contextual series, add an accent color to the key series, and replace vague axis title with an action headline.
