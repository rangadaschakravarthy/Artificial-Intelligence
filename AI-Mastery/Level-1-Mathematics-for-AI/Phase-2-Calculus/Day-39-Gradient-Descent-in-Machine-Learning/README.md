# Day 39 — Gradient Descent in Machine Learning

## Learning Objectives
- Apply Gradient Descent to Linear Regression and Logistic Regression models
- Understand Feature Scaling / Normalization impact on Loss Surface Conditioning
- Derive update equations for weights and bias parameters
- Analyze learning curves and training convergence diagnostics

## Prerequisites
Day 37 — Gradient Descent, Day 38 — Learning Rate

## Topics Covered
- Gradient Descent for Linear Regression (MSE Gradient)
- Gradient Descent for Logistic Regression (Binary Cross-Entropy Gradient)
- Impact of Feature Scaling (Standardization $z = \frac{x-\mu}{\sigma}$) on loss conditioning
- Ill-conditioned loss surfaces (elongated ellipses vs spherical bowls)
- Diagnosing training divergence, underfitting, and overfitting

## Why This Matters for AI
Feature normalization transforms squashed elliptical loss surfaces into symmetric round bowls, allowing Gradient Descent to converge up to 100x faster without oscillating.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Build Linear and Logistic Regression using SGD in Python with and without Feature Standardization.

## Interview Preparation
Explain why feature scaling makes Gradient Descent converge much faster.

## Completion Checklist
- [ ] I can derive SGD updates for Linear & Logistic Regression
- [ ] I understand feature scaling impact on loss contours
- [ ] I know how to standardize features $z = (x - \mu) / \sigma$
- [ ] I can implement scaled SGD in Python

## Estimated Difficulty
Intermediate
