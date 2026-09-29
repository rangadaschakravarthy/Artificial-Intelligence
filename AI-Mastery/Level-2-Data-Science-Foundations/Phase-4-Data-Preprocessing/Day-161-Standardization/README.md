# Day 161 — Standardization

## Learning Objectives
- Rescale continuous numerical features to zero mean ($\mu = 0$) and unit variance ($\sigma = 1$) using Z-Score Standardization.
- Master `sklearn.preprocessing.StandardScaler`.
- Compare Standardization vs Normalization.

## Prerequisites
- Day 159: Scaling
- Day 160: Normalization
- Level 1 Statistics: Gaussian Distribution & Z-Scores

## Topics Covered
- Standardization Z-score formula: $z = \frac{x - \mu}{\sigma}$
- Properties of standardized features: Mean = 0, Standard Deviation = 1
- `sklearn.preprocessing.StandardScaler` API
- Robustness to outliers compared to Min-Max Normalization
- Normalization vs Standardization comparison guide

## Practical Work
- Compare scaling outputs of `StandardScaler` vs `MinMaxScaler` on a dataset containing extreme outliers.

## Difficulty
Intermediate
