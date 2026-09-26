# Day 139 Solutions: Box Plots

## Level 1 — Basic
1. Minimum, Q1 (25th percentile), Median (50th percentile), Q3 (75th percentile), Maximum.
2. $	ext{IQR} = 	ext{Q3} - 	ext{Q1}$.
3. $1.5 	imes 	ext{IQR}$.

## Level 2 — Coding
1. `ax.boxplot(data, patch_artist=True)`
2. `ax.boxplot(data, showmeans=True)`

## Level 3 — Data Analysis
1. Histograms show detailed frequency density shape and modality. Box plots provide compact statistical summaries and explicit outlier detection, making them ideal for comparing multiple groups side-by-side.
