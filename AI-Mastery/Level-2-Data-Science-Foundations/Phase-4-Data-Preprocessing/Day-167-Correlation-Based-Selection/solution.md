# Day 167 Solutions: Correlation-Based Selection

## Level 1 — Basic
1. $|r| > 0.85$ (or $|r| > 0.90$).
2. Pearson Correlation Coefficient.
3. Because two features with $|r| pprox 1.0$ convey duplicate mathematical information, so dropping one retains the full underlying signal while reducing dimension count.

## Level 2 — Coding
1.
```python
top3 = df.corr()['Target'].abs().drop('Target').nlargest(3).index.tolist()
X_top3 = df[top3]
```

## Level 3 — Data Analysis
1. Pearson correlation measures ONLY linear dependency ($y = mx + b$). Mutual Information measures general dependency based on entropy, capturing non-linear relationships ($y = x^2$ or trigonometric curves) where Pearson $r pprox 0$.
