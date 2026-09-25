# Day 51 — Continuous Random Variables

## Learning Objectives
- Master Probability Density Functions (PDF) $f(x)$.
- Master Continuous Cumulative Distribution Functions (CDF) $F(x) = \int_{-\infty}^x f(t) dt$.
- Understand why $P(X = x) = 0$ for continuous random variables.
- Compute probabilities using definite integrals $\int_a^b f(x) dx$.

## Prerequisites
- Days 26–30 Calculus (Integrals and Derivatives).
- Days 49–50 Random Variables and PMF/CDF.

## Topics Covered
1. Probability Density Function (PDF) $f(x)$
2. Continuous Cumulative Distribution Function (CDF) $F(x)$
3. Fundamental Property $P(a \le X \le b) = \int_a^b f(x) dx$
4. PDF Validity Conditions ($f(x) \ge 0$ and $\int_{-\infty}^{\infty} f(x) dx = 1$)
5. Python Continuous Distributions with SciPy `scipy.stats`

## Why This Matters for AI
Continuous variables model neural network weights, continuous features (housing prices, temperatures), latent spaces in VAEs/GANs, and noise distributions.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Understand $f(x)$ as density, not exact probability
- [ ] Integrate PDF to find $P(a \le X \le b)$
- [ ] Relate PDF and CDF via calculus: $f(x) = F'(x)$
- [ ] Compute continuous probabilities in Python using SciPy

## Estimated Difficulty
- **Difficulty**: 4/10
- **Duration**: 2.5 Hours
