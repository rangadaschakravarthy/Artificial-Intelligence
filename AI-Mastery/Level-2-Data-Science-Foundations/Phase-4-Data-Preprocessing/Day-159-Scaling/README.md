# Day 159 — Scaling

## Learning Objectives
- Understand why feature scaling is required for numerical optimization and distance-based algorithms.
- Compare algorithm sensitivity to unscaled features (Gradient Descent, KNN, SVM, Neural Networks vs Decision Trees).
- Recognize the mathematical consequences of unscaled feature spaces.

## Prerequisites
- Days 86–105 (NumPy Linear Algebra)
- Level 1 Calculus: Gradient Descent

## Topics Covered
- Why Feature Scaling Matters
- Distance-based algorithm sensitivity (Euclidean distance $\| \mathbf{x}_1 - \mathbf{x}_2 \|_2$)
- Gradient Descent convergence speed (spherical vs elongated loss contours)
- Scale-invariant algorithms (Decision Trees, Random Forests, XGBoost)
- Overview of Scaling Methods: Normalization (Min-Max) vs Standardization (Z-score)

## Practical Work
- Measure gradient descent convergence iterations on scaled vs unscaled features.

## Difficulty
Intermediate
