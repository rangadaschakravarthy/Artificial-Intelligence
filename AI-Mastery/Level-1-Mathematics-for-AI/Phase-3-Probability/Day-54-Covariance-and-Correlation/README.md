# Day 54 — Covariance and Correlation

## Learning Objectives
- Master Covariance $	ext{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$.
- Master Pearson Correlation Coefficient $
ho_{X,Y} = \frac{	ext{Cov}(X, Y)}{\sigma_X \sigma_Y}$.
- Understand range of correlation $[-1, 1]$ and linear association.
- Identify multi-collinear features in machine learning datasets.
- Compute covariance matrices and correlation matrices in Python.

## Prerequisites
- Days 49–53 Expectation and Variance.

## Topics Covered
1. Definition of Covariance $	ext{Cov}(X, Y)$
2. Pearson Correlation Coefficient $
ho_{X,Y}$
3. Difference between Covariance (scale-dependent) and Correlation (scale-invariant)
4. Covariance Matrix $oldsymbol{\Sigma}$ for Multi-dimensional Random Vectors
5. Feature Selection and Multicollinearity in Machine Learning

## Why This Matters for AI
Covariance and correlation matrices form the backbone of Principal Component Analysis (PCA), Feature Selection, Mahalanobis distance, and Gaussian Mixture Models (GMMs).

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Calculate $	ext{Cov}(X, Y) = E[XY] - E[X]E[Y]$
- [ ] Compute $
ho_{X,Y} = \frac{	ext{Cov}(X, Y)}{\sigma_X \sigma_Y}$
- [ ] Understand $-1 \le 
ho_{X,Y} \le 1$
- [ ] Compute covariance matrix using `np.cov` and `np.corrcoef`

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
