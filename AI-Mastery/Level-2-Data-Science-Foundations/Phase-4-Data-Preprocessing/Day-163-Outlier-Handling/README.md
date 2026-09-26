# Day 163 — Outlier Handling

## Learning Objectives
- Evaluate strategies for handling detected outliers: Removal, Capping (Winsorization), Imputation, and Transformation.
- Implement Winsorization / Percentile Capping using Pandas `.clip()`.
- Choose the appropriate outlier handling strategy based on domain context and model sensitivity.

## Prerequisites
- Day 162: Outlier Detection

## Topics Covered
- 4 Outlier Handling Strategies: Trimming (Dropping), Winsorization (Capping), Imputation, Mathematical Transformation
- Percentile Capping with `df['col'].clip(lower_percentile, upper_percentile)`
- `scipy.stats.mstats.winsorize` API
- Trade-offs: Information loss (Trimming) vs Variance reduction (Capping)
- When NOT to handle outliers (Domain context evaluation)

## Practical Work
- Implement percentile capping using `clip()` to bound extreme 1st and 99th percentile outliers.

## Difficulty
Intermediate
