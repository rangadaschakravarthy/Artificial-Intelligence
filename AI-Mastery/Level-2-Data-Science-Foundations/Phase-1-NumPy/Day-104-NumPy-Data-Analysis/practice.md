# Day 104 Practice Questions: NumPy Data Analysis

## Level 1 — Basic
1. What function calculates percentiles of a NumPy array?
2. What parameter in `np.corrcoef()` specifies that columns represent feature variables?
3. How is the Interquartile Range (IQR) defined mathematically?
4. What function computes frequency counts and bin edges for a 1D array?
5. True or False: Pearson correlation coefficient $ho$ ranges between $-1.0$ and $+1.0$.

## Level 2 — Coding
6. Calculate 10th, 50th, and 90th percentiles of array `np.arange(100)`.
7. Compute the 2x2 Pearson correlation matrix between vectors `x = [1, 2, 3, 4]` and `y = [2, 1, 4, 3]`.
8. Filter outliers from `data = np.array([10, 12, 14, 15, 100])` using the 1.5*IQR rule.
9. Bin values `[5, 15, 25, 35]` into 3 equal-width bins using `np.histogram()`.
10. Use `np.digitize()` to categorize test scores into grade bins `[0, 60, 75, 90, 100]`.

## Level 3 — Data Analysis
11. Predict the diagonal values of any Pearson correlation matrix returned by `np.corrcoef()`.
12. What does a correlation coefficient of $ho = -0.92$ between two features signify?
13. Predict output: `q50 = np.percentile(arr, 50); med = np.median(arr); print(q50 == med)`.
14. Predict output shape of `np.corrcoef(X, rowvar=False)` for feature matrix $X$ of shape `(500, 10)`.
15. Explain why extreme outliers distort feature mean and standard deviation but not the median or IQR.

## Level 4 — Debugging
16. Fix error: `ValueError: rowvar must be True or False` when computing correlation matrix.
17. Fix bug where `np.corrcoef(X)` computed a 500x500 matrix instead of intended 10x10 feature correlation matrix.
18. Fix issue where `np.histogram()` bin edges returned 6 numbers for 5 requested bins (Explain $N+1$ bin edges).

## Level 5 — AI/ML Application
19. How do you implement automated multi-collinearity feature selection using correlation matrices in NumPy?
20. Implement robust Z-score feature scaling: $	ext{Scaled} = rac{X - 	ext{median}}{	ext{IQR}}$.
21. Connect data distribution profiling (percentiles, skewness) to feature engineering transformations.

## Level 6 — Interview Questions
22. Derive Pearson correlation coefficient formula: $ho_{X,Y} = rac{\sum (x_i - ar{x})(y_i - ar{y})}{\sqrt{\sum (x_i - ar{x})^2 \sum (y_i - ar{y})^2}}$.
23. What is the difference between Pearson linear correlation and Spearman rank correlation?
24. Explain why `np.cov` divides by $N-1$ (unbiased sample covariance) by default.
25. Demonstrate how `np.percentile()` handles interpolation methods (`linear`, `lower`, `higher`, `nearest`).
26. How does memory stride layout impact high-dimensional correlation matrix calculation speed?
