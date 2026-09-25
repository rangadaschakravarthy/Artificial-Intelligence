# Day 60 — Naive Bayes Algorithm Mathematics

## Learning Objectives
- Master mathematical formulation of Gaussian, Multinomial, and Bernoulli Naive Bayes.
- Understand Laplace Smoothing (Add-one smoothing) to resolve zero-probability problem.
- Master Log-Sum-Exp trick for numerical stability during probability multiplication.
- Implement Naive Bayes from scratch in pure Python and NumPy.

## Prerequisites
- Days 48 Bayes' Theorem.
- Day 56 Conditional Independence.

## Topics Covered
1. Complete Mathematical Formulation of Naive Bayes
2. Gaussian Naive Bayes (Continuous Features)
3. Multinomial Naive Bayes (Text / Word Counts)
4. Bernoulli Naive Bayes (Binary Word Presence)
5. Laplace Smoothing and Log-Domain Computation

## Why This Matters for AI
Naive Bayes is a foundational baseline algorithm for text classification, spam filtering, and high-dimensional categorical data processing.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Implement Gaussian PDF likelihood evaluation
- [ ] Apply Laplace smoothing $rac{x_i + lpha}{N + lpha K}$
- [ ] Perform prediction in log-space $rg\max_c [\ln P(y) + \sum \ln P(x_i|y)]$
- [ ] Code Naive Bayes from scratch in Python

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
