# Day 153 Solutions: Introduction to Data Preprocessing

## Level 1 — Basic
1. To transform continuous and categorical variables into clean, standardized numerical matrices optimized for ML algorithm training.
2. Data cleaning fixes errors, corruptions, and missing values. Preprocessing transforms clean data into standardized numerical formats (encoding, scaling, transformations).
3. Mean ($\mu$) and Standard Deviation ($\sigma$).

## Level 2 — Coding
1. `df[num_cols] = (df[num_cols] - df[num_cols].mean()) / df[num_cols].std()`

## Level 3 — Data Analysis
1. Unscaled features with large numerical magnitudes (e.g. Salary in tens of thousands) dominate distance calculations over features with small scales (e.g. Age in tens), biasing distance metrics entirely toward large-scale features.
