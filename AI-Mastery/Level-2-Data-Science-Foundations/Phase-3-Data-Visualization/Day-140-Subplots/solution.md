# Day 140 Solutions: Subplots

## Level 1 — Basic
1. A 2D NumPy array of shape `(2, 3)` containing 6 `Axes` objects.
2. `fig.tight_layout()`.
3. `sharey=True`.

## Level 2 — Coding
1. `fig, axes = plt.subplots(1, 3, sharey=True, figsize=(12, 4))`
2. `axes[0].plot(x, y); axes[1].bar(cats, vals)`

## Level 3 — Data Analysis
1. Un-shared axis scales visually distort relative magnitudes, causing small differences on one plot to appear larger than huge differences on another.
