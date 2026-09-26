# Day 164 — Feature Transformation

## Learning Objectives
- Understand why mathematical feature transformations are applied to numerical variables.
- Handle skewed distributions, heteroscedasticity, and non-linear feature relationships.
- Discretize continuous features into categorical bins using `pd.cut()` and `pd.qcut()`.

## Prerequisites
- Day 153: Introduction to Data Preprocessing

## Topics Covered
- Purpose of Feature Transformations (Normality enforcement, variance stabilization)
- Skewness definition (Positive right-skew vs Negative left-skew)
- Discretization / Binning: Equal-width binning (`pd.cut()`) vs Equal-frequency quantile binning (`pd.qcut()`)
- Creating mathematical interaction terms ($x_1 \cdot x_2$, $x_1^2$)

## Practical Work
- Perform equal-frequency quantile binning (`pd.qcut()`) on income data to create 4 income quartiles.

## Difficulty
Intermediate
