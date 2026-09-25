# Day 59 — Probability for Machine Learning

## Learning Objectives
- Connect probability concepts to core machine learning paradigms.
- Master Maximum Likelihood Estimation (MLE) and Maximum A Posteriori (MAP).
- Understand how Cross-Entropy Loss derives from Negative Log-Likelihood (NLL).
- Map probabilistic output confidence to model calibration.

## Prerequisites
- Days 44–58 Probability theory foundations.

## Topics Covered
1. Maximum Likelihood Estimation (MLE)
2. Maximum A Posteriori (MAP) Estimation
3. Deriving Loss Functions from Probabilistic Principles (MSE, Binary Cross-Entropy)
4. Model Calibration and Expected Calibration Error (ECE)
5. Generative vs Discriminative Probabilistic Models

## Why This Matters for AI
Every major machine learning loss function (MSE, Cross-Entropy, Focal Loss) is directly derived by minimizing Negative Log-Likelihood under specific probabilistic noise assumptions.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Derive MLE for Gaussian likelihood -> MSE loss
- [ ] Derive MLE for Bernoulli likelihood -> Binary Cross-Entropy loss
- [ ] Differentiate Discriminative $P(Y|X)$ vs Generative $P(X,Y)$
- [ ] Code MLE estimation in Python

## Estimated Difficulty
- **Difficulty**: 4/10
- **Duration**: 2.5 Hours
