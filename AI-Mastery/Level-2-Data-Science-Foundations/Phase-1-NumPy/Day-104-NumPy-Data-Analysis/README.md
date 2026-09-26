# Day 104 — NumPy Data Analysis

## Learning Objectives
- Perform end-to-end Exploratory Data Analysis (EDA) using NumPy.
- Compute summary statistics, correlation matrices, and percentile distributions.
- Implement data filtering, binning, and feature normalization routines.

## Prerequisites
- Day 94: Boolean and Fancy Indexing
- Day 99: Aggregation and Statistics

## Topics Covered
1. Loading and Structuring Raw Data Arrays
2. Descriptive Statistical Summaries (`mean`, `median`, `std`, `percentile`)
3. Covariance and Pearson Correlation Matrix (`np.cov`, `np.corrcoef`)
4. Data Binning and Histogram Calculations (`np.histogram`, `np.digitize`)
5. Feature Scaling and Outlier Filtering

## Why This Matters
Before building complex Pandas or ML pipelines, analyzing data distribution characteristics using NumPy provides raw computational speed and data insights.

## Real-World Usage
Computing feature correlation matrices to identify multi-collinearity between dataset variables.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can compute percentiles and interquartile ranges (IQR).
- [ ] I can compute Pearson correlation matrices using `np.corrcoef()`.
- [ ] I can bin numerical data using `np.histogram()` and `np.digitize()`.
- [ ] I can filter outliers using IQR statistical bounds.

## Difficulty
Intermediate
