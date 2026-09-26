# Day 165 Practice Questions: Log and Power Transformations

## Level 1 — Basic
1. Why is `np.log1p(x)` preferred over `np.log(x)` for feature data containing zeros?
2. What constraint does Box-Cox transformation impose on feature values ($x > 0$)?
3. What power transformation method handles zero and negative numbers?

## Level 2 — Coding
1. Apply `np.log1p()` to right-skewed column `'Revenue'`.
2. Apply `PowerTransformer(method='yeo-johnson')`.

## Level 3 — Data Analysis
1. How does log-transforming right-skewed target variables improve linear regression model performance?
