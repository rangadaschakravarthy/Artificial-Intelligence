# Day 130 — Exploratory Data Analysis

## Learning Objectives
- Perform systematic Exploratory Data Analysis (EDA) on structured datasets.
- Analyze univariate distributions, bivariate relationships, and multivariate feature interactions.
- Compute summary statistics, correlation matrices, and distribution shapes.

## Prerequisites
- Day 111: Inspecting Datasets
- Day 121: Aggregation
- Level 1 Statistics: Covariance and Correlation

## Topics Covered
- EDA Philosophy and Objective Framework
- Univariate Analysis: Measures of Central Tendency & Dispersion (Mean, Median, Skewness, IQR)
- Categorical Frequency Analysis using `.value_counts()` and proportions
- Bivariate Analysis: Numerical vs Numerical (Correlation Matrix `df.corr()`)
- Bivariate Analysis: Categorical vs Numerical (Grouped Aggregations)
- Multivariate Feature Interaction Analysis
- Formulating analytical hypotheses from data patterns

## Why This Matters
Before building machine learning models or making business decisions, Data Scientists must discover patterns, uncover anomalies, and test hypotheses through EDA.

## Real-World Usage
Investigating customer churn logs to discover that high churn strongly correlates with short customer tenure and specific billing tiers.

## Study Order
1. Read `theory.md` for the EDA framework.
2. Review `examples.md` for statistical analysis code.
3. Run `code.py` to observe EDA output summaries.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Conduct a complete univariate and bivariate EDA report on a housing price dataset.
- Calculate Pearson correlation coefficients across numerical features.

## Interview Preparation
- What is the difference between Univariate, Bivariate, and Multivariate EDA?
- How do you detect multi-collinearity during EDA using correlation matrices?

## Completion Checklist
- [ ] I can perform univariate distribution analysis.
- [ ] I can analyze categorical frequency counts and proportions.
- [ ] I can compute correlation matrices using `df.corr()`.
- [ ] I can extract data-driven business insights.

## Difficulty
Intermediate
