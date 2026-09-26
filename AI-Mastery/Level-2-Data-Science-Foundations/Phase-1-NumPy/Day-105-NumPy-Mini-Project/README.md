# Day 105 — NumPy Mini-Project: Numerical Analysis Engine

## Project Overview
In this Capstone Mini-Project for Phase 1, you will build an end-to-end **Numerical Data Analysis & Preprocessing Engine** in pure NumPy.

## Learning Objectives
- Combine array creation, indexing, slicing, broadcasting, and vectorization into a cohesive pipeline.
- Perform statistical data profiling, outlier detection, and feature standardization.
- Implement closed-form Linear Regression modeling and evaluation metrics from scratch.

## Project Tasks
1. **Data Ingestion & Inspection**: Generate a synthetic raw dataset tensor with features, targets, missing values (`NaN`), and outliers.
2. **Data Cleaning & Imputation**: Identify missing `NaN` values and impute them using column medians.
3. **Outlier Filtering**: Detect and clip extreme feature outliers using 1.5*IQR statistical bounds.
4. **Feature Standardization**: Apply Z-score standardization ($\mu=0, \sigma=1$) via array broadcasting.
5. **Machine Learning Model**: Train a closed-form Linear Regression model $w = (X^T X)^{-1} X^T y$ and evaluate MSE loss.

## Recommended Study Order
1. Read `theory.md` for pipeline design principles.
2. Review `examples.md` for task step breakdowns.
3. Complete `practice.md` extension challenges.
4. Verify using `solution.md`.
5. Execute and inspect `code.py`.

## Completion Checklist
- [ ] I can clean and impute missing data in NumPy.
- [ ] I can build a statistical preprocessing pipeline.
- [ ] I can solve linear models using matrix equations.
- [ ] I have completed Phase 1 — NumPy!

## Difficulty
Intermediate / Advanced
