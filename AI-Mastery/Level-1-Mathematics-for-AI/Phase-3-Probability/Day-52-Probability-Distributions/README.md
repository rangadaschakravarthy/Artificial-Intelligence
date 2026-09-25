# Day 52 — Probability Distributions

## Learning Objectives
- Master key discrete distributions (Bernoulli, Binomial, Poisson).
- Master key continuous distributions (Uniform, Gaussian/Normal).
- Understand distribution parameters (Mean $\mu$, Variance $\sigma^2$, Rate $\lambda$, Probability $p$).
- Implement distributions in Python using SciPy `scipy.stats`.

## Prerequisites
- Days 49–51 Random Variables, PMF, PDF, CDF.

## Topics Covered
1. Bernoulli Distribution $	ext{Bern}(p)$
2. Binomial Distribution $	ext{Bin}(n, p)$
3. Poisson Distribution $	ext{Poisson}(\lambda)$
4. Uniform Distribution $	ext{Unif}(a, b)$
5. Gaussian / Normal Distribution $\mathcal{N}(\mu, \sigma^2)$

## Why This Matters for AI
Choosing the correct probability distribution is the first step in modeling data. Binary classification targets are Bernoulli, trial successes are Binomial, count data are Poisson, weight initializations are Gaussian or Uniform.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Work through `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Know PMF/PDF formulas for Bernoulli, Binomial, Normal
- [ ] Know Mean and Variance formulas for each distribution
- [ ] Identify which distribution fits a given ML task
- [ ] Code distributions in SciPy and NumPy

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
