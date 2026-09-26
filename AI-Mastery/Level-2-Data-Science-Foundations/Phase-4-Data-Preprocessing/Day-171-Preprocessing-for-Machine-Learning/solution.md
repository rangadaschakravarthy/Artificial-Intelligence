# Day 171 Solutions: Preprocessing for Machine Learning

## Level 1 — Basic
1. No. Decision Trees are scale-invariant.
2. Linear Models (Linear Regression, Logistic Regression).
3. `MinMaxScaler` (scaling pixel range $[0, 255]$ into $[0, 1]$).

## Level 2 — Coding
1. Refer to Day 171 Example 1 code implementation.

## Level 3 — Data Analysis
1. Random Forests use axis-aligned decision split thresholds ($x_i \ge c$) evaluated on individual features independently, making them scale-invariant and immune to monotonic magnitude outliers. Logistic Regression computes linear weighted dot products ($w^T x + b$), where unscaled outliers distort gradient updates and weight coefficients.
