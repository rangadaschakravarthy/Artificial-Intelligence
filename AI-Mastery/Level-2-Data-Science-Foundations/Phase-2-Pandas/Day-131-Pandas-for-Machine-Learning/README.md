# Day 131 — Pandas for Machine Learning

## Learning Objectives
- Prepare ML feature matrices ($X$) and target vectors ($y$) using Pandas.
- Convert categorical string features to numeric format using `pd.get_dummies()`.
- Structure clean train/validation/test dataset splits preserving tabular integrity.

## Prerequisites
- Day 112: Selecting Data
- Day 118: Data Type Conversion
- Day 129: Data Cleaning Workflow

## Topics Covered
- Feature Matrix ($X$) vs Target Vector ($y$) separation
- Categorical One-Hot Encoding with `pd.get_dummies()`
- `dummy_na` and `drop_first=True` parameters
- Handling unknown categorical levels
- Structuring pandas DataFrames for Scikit-Learn input compatibility
- Exporting ML-ready datasets to clean CSV / Parquet formats

## Why This Matters
Machine learning algorithms accept only numeric matrices. Pandas serves as the primary bridge converting messy raw DataFrames into clean mathematical arrays.

## Real-World Usage
Preparing customer demographic tables into One-Hot Encoded feature arrays $X$ for Scikit-Learn Random Forest churn classifiers.

## Study Order
1. Read `theory.md` for ML dataset preparation rules.
2. Review `examples.md` for `get_dummies()` patterns.
3. Run `code.py` to inspect ML matrices.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Separate a raw dataset into feature matrix $X$ and label vector $y$.
- One-Hot Encode categorical attributes using `pd.get_dummies(drop_first=True)`.

## Interview Preparation
- Why is `drop_first=True` used in One-Hot Encoding (Dummy Variable Trap)?
- How do you ensure training and test DataFrames maintain identical feature columns after `pd.get_dummies()`?

## Completion Checklist
- [ ] I can separate DataFrames into $X$ and $y$.
- [ ] I can perform One-Hot Encoding using `pd.get_dummies()`.
- [ ] I understand the Dummy Variable Trap (`drop_first=True`).
- [ ] I can export ML-ready datasets cleanly.

## Difficulty
Intermediate
