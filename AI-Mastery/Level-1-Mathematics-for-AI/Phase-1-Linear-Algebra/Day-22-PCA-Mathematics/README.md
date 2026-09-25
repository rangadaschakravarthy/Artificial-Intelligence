# Day 22 — PCA Mathematics

## Learning Objectives
- Master the mathematical steps of Principal Component Analysis (PCA)
- Perform mean-centering of feature vectors $\mathbf{X}_{centered} = \mathbf{X} - \mathbf{\mu}$
- Compute dataset Covariance Matrix $\mathbf{\Sigma} = \frac{1}{N-1} \mathbf{X}_{centered}^T \mathbf{X}_{centered}$
- Calculate Explained Variance Ratio for Principal Components
- Project high-dimensional data onto top $k$ principal components

## Prerequisites
Day 19 — Eigenvalues and Eigenvectors, Day 21 — Singular Value Decomposition

## Topics Covered
- PCA Objective: Maximize variance while minimizing reconstruction error
- Step 1: Mean Centering data
- Step 2: Covariance Matrix calculation
- Step 3: Eigendecomposition of Covariance Matrix
- Step 4: Explained Variance Ratio $\frac{\lambda_i}{\sum \lambda_j}$
- Step 5: Feature Projection onto Principal Component basis

## Why This Matters for AI
PCA is the most widely used unsupervised learning technique for dimensionality reduction, feature extraction, data visualization (2D/3D projection), and noise filtering.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Build a complete PCA algorithm from scratch in Python and compare against `sklearn.decomposition.PCA`.

## Interview Preparation
Explain step-by-step mathematical derivation of PCA, mean centering necessity, and explained variance.

## Completion Checklist
- [ ] I can state the 5 steps of PCA
- [ ] I know why data MUST be mean-centered before PCA
- [ ] I can calculate explained variance ratio
- [ ] I can build PCA from scratch in Python

## Estimated Difficulty
Advanced
