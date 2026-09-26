# Day 160 — Normalization

## Learning Objectives
- Rescale numerical features into a bounded range $[0, 1]$ using Min-Max Normalization.
- Master `sklearn.preprocessing.MinMaxScaler`.
- Understand the sensitivity of Min-Max Normalization to extreme outliers.

## Prerequisites
- Day 159: Scaling

## Topics Covered
- Min-Max Normalization Formula: $x' = rac{x - x_{\min}}{x_{\max} - x_{\min}}$
- Arbitrary range scaling $[a, b]$ (e.g. $[-1, 1]$)
- `sklearn.preprocessing.MinMaxScaler` API (`feature_range=(0, 1)`)
- Sensitivity to extreme outliers (outliers compress remaining data into tiny sub-intervals)
- When to use Normalization (Image processing pixel intensity $[0, 255] 	o [0, 1]$, bounded algorithms)

## Practical Work
- Implement custom Min-Max Normalization in pure Python and compare outputs with Scikit-Learn `MinMaxScaler`.

## Difficulty
Intermediate
