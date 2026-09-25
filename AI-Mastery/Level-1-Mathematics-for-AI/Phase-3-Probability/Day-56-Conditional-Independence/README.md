# Day 56 — Conditional Independence

## Learning Objectives
- Master Conditional Independence $(X \perp \!\!\! \perp Y \mid Z)$.
- Understand how conditioning on $Z$ can create or destroy independence between $X$ and $Y$.
- Master Naive Bayes conditional independence assumption $P(X_1, \dots, X_d \mid Y) = \prod_{i=1}^d P(X_i \mid Y)$.
- Understand Graphical Models (Bayesian Networks) and d-separation intuition.

## Prerequisites
- Days 47 Conditional Probability.
- Day 55 Independence.

## Topics Covered
1. Definition of Conditional Independence $(X \perp \!\!\! \perp Y \mid Z)$
2. Formula $P(X, Y \mid Z) = P(X \mid Z) P(Y \mid Z)$
3. Naive Bayes Classifier Assumption
4. Common Cause vs Common Effect (Collider) Patterns
5. Probabilistic Graphical Models Foundations

## Why This Matters for AI
Conditional independence simplifies complex joint probability distributions over thousands of variables into manageable factorized models (Naive Bayes, Markov Random Fields, Bayesian Networks).

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Write $P(X, Y | Z) = P(X|Z) P(Y|Z)$
- [ ] State Naive Bayes assumption
- [ ] Differentiate marginal independence from conditional independence
- [ ] Code Naive Bayes likelihood factorization in Python

## Estimated Difficulty
- **Difficulty**: 4/10
- **Duration**: 2.5 Hours
