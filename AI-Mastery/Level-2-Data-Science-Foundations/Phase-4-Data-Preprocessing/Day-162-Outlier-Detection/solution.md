# Day 162 Solutions: Outlier Detection

## Level 1 — Basic
1. $	ext{IQR} = Q_3 - Q_1$ (75th percentile minus 25th percentile).
2. $	ext{Lower} = Q_1 - 1.5	ext{IQR}$, $	ext{Upper} = Q_3 + 1.5	ext{IQR}$.
3. $|Z| > 3.0$ (or $|Z| > 2.5$).

## Level 2 — Coding
1.
```python
from scipy import stats
z_scores = np.abs(stats.zscore(df['Col']))
outlier_mask = z_scores > 3.0
```

## Level 3 — Data Analysis
1. Deleting genuine high-value VIP customer observations strips essential real-world variance from the dataset. The model will fail to generalize to high-value transactions in production.
