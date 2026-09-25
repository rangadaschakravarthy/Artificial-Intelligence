# Day 58 — Marginal Probability

## Learning Objectives
- Master Marginalization ("summing out" or "integrating out" nuisance variables).
- Derive Marginal PMF $p_X(x) = \sum_y p(x, y)$.
- Derive Marginal PDF $f_X(x) = \int_{-\infty}^{\infty} f(x, y) dy$.
- Recover 1D component distributions from multi-dimensional joint distributions.

## Prerequisites
- Day 57 Joint Probability Distributions.

## Topics Covered
1. The Principle of Marginalization
2. Marginal PMF for Discrete Random Variables
3. Marginal PDF for Continuous Random Variables
4. Law of Total Probability in Continuous Spaces
5. Latent Variable Elimination in Machine Learning

## Why This Matters for AI
Marginalization is how AI models eliminate hidden/latent variables $\mathbf{z}$ to compute observed data likelihood $p(\mathbf{x}) = \int p(\mathbf{x}, \mathbf{z}) d\mathbf{z}$.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Compute marginal row/column sums from PMF tables
- [ ] Integrate out variable $y$ to find $f_X(x) = \int f(x,y)dy$
- [ ] Compute marginal mean and variance
- [ ] Implement marginalization code in Python

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
