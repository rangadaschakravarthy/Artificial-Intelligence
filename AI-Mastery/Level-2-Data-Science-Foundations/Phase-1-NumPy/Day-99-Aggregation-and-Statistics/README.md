# Day 99 — Aggregation and Statistics

## Learning Objectives
- Master summary statistical aggregations (`sum`, `mean`, `median`, `std`, `var`, `min`, `max`).
- Understand positional index aggregations (`argmin`, `argmax`, `argsort`).
- Apply axis reductions to summarize high-dimensional datasets.

## Prerequisites
- Level 1: Statistics (Mean, Variance, Standard Deviation)
- Day 88: Array Dimensions

## Topics Covered
1. Core Statistical Aggregators (`np.mean`, `np.median`, `np.std`, `np.var`)
2. Extremum aggregations (`np.min`, `np.max`, `np.ptp` range)
3. Positional index location (`np.argmin`, `np.argmax`, `np.argsort`)
4. Cumulative aggregations (`np.cumsum`, `np.cumprod`)
5. NaN-robust statistical aggregators (`np.nanmean`, `np.nanstd`, `np.nanmedian`)

## Why This Matters
Statistical aggregation is essential for data profiling, feature extraction, anomaly detection, and classification decision rules.

## Real-World Usage
Finding the predicted class index using `argmax` on neural network output probability distributions.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can compute mean, median, variance, and standard deviation along specific axes.
- [ ] I can find maximum value index locations using `argmax()`.
- [ ] I know how to use NaN-robust aggregators like `np.nanmean()`.
- [ ] I can connect statistical aggregations to Level 1 statistics.

## Difficulty
Intermediate
