# Day 161 Solutions: Standardization

## Level 1 — Basic
1. Mean $\mu = 0$, Standard Deviation $\sigma = 1$.
2. $z = rac{x - \mu}{\sigma}$.
3. No. Standardized values are unbounded and typically fall between $-3$ and $+3$ for Gaussian distributions.

## Level 2 — Coding
1. `scaler = StandardScaler(); df[num_cols] = scaler.fit_transform(df[num_cols])`

## Level 3 — Data Analysis
1. PCA seeks orthogonal direction vectors maximizing variance. Unstandardized features with large variances dominate principal component eigenvectors regardless of feature signal.
