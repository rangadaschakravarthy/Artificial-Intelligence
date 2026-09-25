# Day 5 — Norms and Distances

## Learning Objectives
- Understand vector norms as measures of vector length or size
- Calculate L1 Norm (Manhattan), L2 Norm (Euclidean), and Infinity Norm
- Calculate Euclidean distance and Manhattan distance between vectors
- Understand L1 and L2 regularization in machine learning (Lasso vs Ridge)

## Prerequisites
Day 4 — Dot Product

## Topics Covered
- Concept of Vector Norms ($p$-norm generalization)
- L1 Norm ($||v||_1$, Taxicab / Manhattan)
- L2 Norm ($||v||_2$, Euclidean length)
- Infinity Norm ($||v||_\infty$, Maximum component)
- Euclidean vs Manhattan distance metrics
- Regularization penalty terms (Lasso & Ridge)

## Why This Matters for AI
Norms measure model loss error, constrain neural network weights to prevent overfitting (regularization), and measure distance between data points in k-NN and clustering algorithms.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Implement manual and NumPy L1, L2, $L_\infty$ norms and distance metrics.

## Interview Preparation
Explain difference between L1 and L2 norms and their effects on sparsity.

## Completion Checklist
- [ ] I can calculate L1, L2, and Infinity norms
- [ ] I can calculate Euclidean and Manhattan distances
- [ ] I understand why L1 norm creates sparse weights
- [ ] I can compute norms using NumPy

## Estimated Difficulty
Beginner
