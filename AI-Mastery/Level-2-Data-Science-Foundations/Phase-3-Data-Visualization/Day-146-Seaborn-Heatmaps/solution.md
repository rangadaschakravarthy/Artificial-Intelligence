# Day 146 Solutions: Seaborn Heatmaps

## Level 1 — Basic
1. `sns.heatmap()`.
2. `annot=True`.
3. `np.triu()`.

## Level 2 — Coding
1. `sns.heatmap(df.corr(), cmap='coolwarm')`
2. `sns.heatmap(df.corr(), annot=True, fmt='.2f')`

## Level 3 — Data Analysis
1. Correlation ranges from `-1` (negative) to `+1` (positive) centered around `0` (neutral). Diverging colormaps highlight both positive and negative extremes with distinct hues while keeping neutral zero values muted.
