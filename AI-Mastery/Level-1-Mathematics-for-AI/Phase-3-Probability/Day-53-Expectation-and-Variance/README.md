# Day 53 — Expectation and Variance

## Learning Objectives
- Master Expected Value $E[X]$ for discrete and continuous random variables.
- Master Variance $	ext{Var}(X) = E[(X - \mu)^2]$ and Standard Deviation $\sigma$.
- Master Linearity of Expectation $E[aX + bY + c] = a E[X] + b E[Y] + c$.
- Understand Variance rules $	ext{Var}(aX + b) = a^2 	ext{Var}(X)$.
- Calculate Expectation and Variance in Python.

## Prerequisites
- Days 49–52 Random variables and probability distributions.

## Topics Covered
1. Expected Value $E[X]$ (First Moment)
2. Variance $	ext{Var}(X)$ (Second Central Moment)
3. Standard Deviation $\sigma = \sqrt{	ext{Var}(X)}$
4. Linearity of Expectation (Holds for dependent and independent RVs!)
5. Variance Rules and Covariance interaction

## Why This Matters for AI
Model loss functions optimize expected risk $E_{X,Y}[L(y, f(x))]$. Variance measures overfitting, instability, and prediction uncertainty in AI.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Work through `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Compute $E[X]$ for discrete and continuous distributions
- [ ] Compute $	ext{Var}(X) = E[X^2] - (E[X])^2$
- [ ] Apply Linearity of Expectation $E[aX + b] = a E[X] + b$
- [ ] Apply Variance scaling $	ext{Var}(aX + b) = a^2 	ext{Var}(X)$

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
