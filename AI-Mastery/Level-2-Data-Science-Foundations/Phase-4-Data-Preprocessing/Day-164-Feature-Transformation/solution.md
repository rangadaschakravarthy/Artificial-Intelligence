# Day 164 Solutions: Feature Transformation

## Level 1 — Basic
1. `pd.cut()` divides numerical range into equal-width bin intervals. `pd.qcut()` divides observations into equal-frequency quantile bins.
2. Positive right-skewness.
3. Converting continuous continuous features into discrete ordinal interval bins.

## Level 2 — Coding
1. `df['Age_Group'] = pd.qcut(df['Age'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])`

## Level 3 — Data Analysis
1. Heavily skewed data places almost all observations inside a single bin during equal-width binning. Quantile binning ensures each bin receives an equal proportion of sample observations ($25\%$ each for quartiles).
