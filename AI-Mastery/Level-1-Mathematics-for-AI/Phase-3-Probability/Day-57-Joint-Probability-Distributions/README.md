# Day 57 — Joint Probability Distributions

## Learning Objectives
- Master Joint PMFs $p(x, y)$ and Joint PDFs $f(x, y)$.
- Compute Joint CDFs $F(x, y) = P(X \le x, Y \le y)$.
- Verify Joint PDF normalization $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) dx dy = 1$.
- Evaluate multi-variable probabilities over 2D spatial regions.

## Prerequisites
- Days 49–51 Discrete and Continuous Random Variables.
- Day 31 Partial Derivatives and Double Integrals.

## Topics Covered
1. Joint PMF for Discrete Random Vectors
2. Joint PDF for Continuous Random Vectors
3. Joint Cumulative Distribution Function (CDF)
4. Double Integration over 2D Regions
5. Multivariate Probability Distributions in AI

## Why This Matters for AI
Machine learning works on multidimensional random vectors $\mathbf{X} = [X_1, X_2, \dots, X_d]^T$. Understanding joint distributions $f(\mathbf{x})$ is required for generative modeling, density estimation, and clustering.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Work through `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Construct 2D Joint PMF tables
- [ ] Verify double integral $\int \int f(x,y) dx dy = 1$
- [ ] Compute region probabilities $P((X,Y) \in R)$
- [ ] Model 2D Gaussian joint distributions in SciPy

## Estimated Difficulty
- **Difficulty**: 4/10
- **Duration**: 2.5 Hours
