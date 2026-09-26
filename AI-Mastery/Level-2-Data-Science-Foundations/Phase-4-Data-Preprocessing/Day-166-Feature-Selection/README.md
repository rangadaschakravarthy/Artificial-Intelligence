# Day 166 — Feature Selection

## Learning Objectives
- Understand the rationale and benefits of Feature Selection (Curse of Dimensionality, Overfitting, Training Speed).
- Categorize Feature Selection techniques into Filter, Wrapper, and Embedded methods.
- Eliminate zero-variance and low-variance constant features using `VarianceThreshold`.

## Prerequisites
- Day 153: Introduction to Data Preprocessing

## Topics Covered
- Rationale: Why more features are not always better (Curse of Dimensionality)
- 3 Categories of Feature Selection: Filter, Wrapper, Embedded
- Variance-based selection using `sklearn.feature_selection.VarianceThreshold`
- Identifying and dropping quasi-constant features (e.g. $> 99\%$ identical values)
- Feature Selection vs Dimensionality Reduction (PCA)

## Practical Work
- Use `VarianceThreshold` to automatically detect and drop constant features from a dataset.

## Difficulty
Intermediate
