# Day 165 Solutions: Log and Power Transformations

## Level 1 — Basic
1. $\ln(0)$ is mathematically undefined ($-\infty$). `np.log1p(x)` computes $\ln(1 + x)$, mapping $x = 0$ safely to $\ln(1) = 0$.
2. Box-Cox requires strictly positive values ($x > 0$).
3. Yeo-Johnson Power Transformation.

## Level 2 — Coding
1. `df['Rev_Log'] = np.log1p(df['Revenue'])`
2. `pt = PowerTransformer(method='yeo-johnson'); df['Scaled'] = pt.fit_transform(df[['Col']])`

## Level 3 — Data Analysis
1. Linear regression assumes normally distributed residuals and homoscedastic variance. Log-transforming right-skewed targets linearizes exponential trends and stabilizes error variance.
