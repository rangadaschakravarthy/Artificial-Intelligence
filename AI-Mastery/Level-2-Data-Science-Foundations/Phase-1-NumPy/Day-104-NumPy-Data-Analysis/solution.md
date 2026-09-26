# Day 104 Solutions: NumPy Data Analysis

## Level 1 — Basic
1. `np.percentile()` (or `np.quantile()`).
2. `rowvar=False`
3. $	ext{IQR} = Q3 - Q1 = 	ext{Percentile}(75) - 	ext{Percentile}(25)$.
4. `np.histogram()`
5. True ($-1.0 \le ho \le +1.0$).

## Level 2 — Coding
6. `p10, p50, p90 = np.percentile(np.arange(100), [10, 50, 90])` -> `(9.9, 49.5, 89.1)`.
7. `corr = np.corrcoef(x, y)` -> `[[1.0, 0.6], [0.6, 1.0]]`.
8. 
```python
q25, q75 = np.percentile(data, [25, 75])
iqr = q75 - q25
clean = data[(data >= q25 - 1.5*iqr) & (data <= q75 + 1.5*iqr)]
```
9. `counts, edges = np.histogram([5, 15, 25, 35], bins=3)`
10. `bin_indices = np.digitize(scores, bins=[0, 60, 75, 90, 100])`

## Level 3 — Data Analysis
11. Diagonal values are always `1.0` (Self-correlation of a feature with itself is perfectly 1.0).
12. Strong negative linear relationship (As feature X increases, feature Y decreases proportionally).
13. `True` (The 50th percentile is identical to the median).
14. `(10, 10)` (Pairwise correlations between 10 features).
15. Mean and std use every value in computation (squared for std), so extreme values pull them heavily. Median and IQR are rank-order statistics dependent on middle position, ignoring tail extremes.

## Level 4 — Debugging
16. Pass boolean flag: `rowvar=False` (or `rowvar=True`).
17. By default, `np.corrcoef(X)` assumes rows are variables. Pass `rowvar=False` so columns are treated as variables.
18. $N$ histogram bins require $N+1$ boundary bin edges (including start of first bin and end of last bin).

## Level 5 — AI/ML Application
19. 
```python
corr = np.abs(np.corrcoef(X, rowvar=False))
np.fill_diagonal(corr, 0)
drop_cols = [j for i, j in zip(*np.where(corr > 0.95)) if i < j]
X_clean = np.delete(X, drop_cols, axis=1)
```
20. `q25, q75 = np.percentile(X, [25, 75], axis=0); iqr = q75 - q25; X_robust = (X - np.median(X, axis=0)) / iqr`
21. Skewed percentile distributions signal the need for log/power transforms to make feature distributions symmetric for ML models.

## Level 6 — Interview Solutions
22. Pearson correlation is the normalized covariance: $ho_{X,Y} = rac{	ext{Cov}(X,Y)}{\sigma_X \sigma_Y} = rac{\sum (x_i - ar{x})(y_i - ar{y})}{\sqrt{\sum (x_i - ar{x})^2 \sum (y_i - ar{y})^2}}$.
23. Pearson measures linear relationships between continuous variables. Spearman measures monotonic relationships between ranked values (robust to non-linear monotonic trends).
24. `np.cov` computes sample covariance matrix, applying Bessel's correction ($N-1$ denominator) to provide an unbiased estimator of population covariance.
25. When percentile falls between data points $i$ and $i+1$, interpolation method specifies value choice: `linear` (weighted average), `lower` ($i$), `higher` ($i+1$), `nearest` (closest index).
26. Computing covariance $X^T X$ for $X$ of shape $(N, D)$ requires contiguous column memory access. C-contiguous layout optimizes row-column dot products in L1 CPU cache.
