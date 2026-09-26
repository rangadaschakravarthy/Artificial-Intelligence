# Day 171 — Preprocessing for Machine Learning

## Learning Objectives
- Tailor specific preprocessing workflows to distinct algorithm families (Linear Models vs Tree Models vs Distance Models).
- Build model-specific feature preparation pipelines.
- Verify array compatibility for Scikit-Learn model fitting.

## Prerequisites
- Days 153–170 (Preprocessing Foundations)

## Topics Covered
- Preprocessing Requirements by Algorithm Family:
  - **Linear Models (Linear/Logistic Regression)**: Normal distribution, no multi-collinearity (`drop_first=True`), Z-score scaling.
  - **Distance-Based Models (KNN, SVM)**: Strict scaling (Min-Max or Standard), One-Hot encoding.
  - **Tree-Based Models (Random Forest, XGBoost)**: No scaling required, Ordinal/Label encoding handles non-linearities.
  - **Neural Networks**: Min-Max $[0, 1]$ or Standardization, One-Hot encoding, non-zero imputations.

## Practical Work
- Build a Python script that prepares two distinct feature matrices ($X_{	ext{linear}}$ and $X_{	ext{tree}}$) from the same raw dataset tailored for Linear Regression vs XGBoost.

## Difficulty
Intermediate / Advanced
