# Day 144 Solutions: Seaborn Distribution Plots

## Level 1 — Basic
1. Kernel Density Estimate.
2. `sns.ecdfplot()`.
3. `sns.jointplot()`.

## Level 2 — Coding
1. `sns.histplot(data=df, x='Metric', kde=True)`
2. `sns.jointplot(data=df, x='X', y='Y', kind='hex')`

## Level 3 — Data Analysis
1. ECDF represents every actual data point without smoothing parameters. KDE relies on bandwidth parameters which can over-smooth or introduce artificial density modes on small sample sizes.
