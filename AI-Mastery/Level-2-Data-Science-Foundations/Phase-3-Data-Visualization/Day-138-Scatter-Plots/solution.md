# Day 138 Solutions: Scatter Plots

## Level 1 — Basic
1. Continuous numerical variables.
2. Pass feature array to `c` and specify a `cmap` (e.g. `ax.scatter(x, y, c=z, cmap='viridis')`).
3. Bubble Chart.

## Level 2 — Coding
1. `ax.scatter(height, weight, alpha=0.5)`
2. `z = np.polyfit(x, y, 1); ax.plot(x, np.poly1d(z)(x), 'r--')`

## Level 3 — Data Analysis
1. Tight alignment of points along a diagonal line indicates strong correlation. Wide, cloud-like dispersion indicates weak or zero correlation.
