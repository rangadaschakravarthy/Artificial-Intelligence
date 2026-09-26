# Day 155 Practice Questions: Categorical and Numerical Features

## Level 1 — Basic
1. Which Pandas function selects columns based on data type (`select_dtypes` or `filter`)?
2. Why should numeric ZIP codes (`90210`, `10001`) NOT be treated as continuous numerical features?
3. What is cardinality in the context of categorical variables?

## Level 2 — Coding
1. Select all numeric columns using `df.select_dtypes(include=[np.number]).columns`.
2. Convert object column `'Status'` to pandas `'category'` dtype.

## Level 3 — Data Analysis
1. Why does One-Hot Encoding high-cardinality categorical features (e.g., 5,000 unique URLs) cause memory issues?
