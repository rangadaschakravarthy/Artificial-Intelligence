# Day 166 Solutions: Feature Selection

## Level 1 — Basic
1. Filter Methods, Wrapper Methods, Embedded Methods.
2. `VarianceThreshold`.
3. It reduces total feature dimension count $d$, increasing data point density in lower-dimensional vector space and preventing model overfitting.

## Level 2 — Coding
1.
```python
# p*(1-p) for p=0.99
threshold = 0.99 * (1 - 0.99)
vt = VarianceThreshold(threshold=threshold)
X_filtered = vt.fit_transform(X)
```

## Level 3 — Data Analysis
1. Filter methods are fast, model-agnostic statistical checks ($O(d)$ time). Wrapper methods evaluate feature combinations using full model training passes, producing higher accuracy for a specific model but at massive computational cost ($O(2^d)$ time).
