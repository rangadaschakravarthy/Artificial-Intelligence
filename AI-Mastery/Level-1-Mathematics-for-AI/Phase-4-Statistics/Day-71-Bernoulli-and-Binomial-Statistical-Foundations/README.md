# Day 71 — Bernoulli and Binomial Statistical Foundations

## Learning Objectives
- Master Bernoulli distribution statistical parameters ($p, p(1-p)$).
- Master Binomial distribution statistical inference for proportions.
- Compute Normal Approximation to Binomial distribution ($n p \ge 10, n(1-p) \ge 10$).
- Compute confidence intervals for proportions in Python.

## Prerequisites
- Days 50, 52 Discrete probability distributions.

## Topics Covered
1. Bernoulli Statistical Model $	ext{Bern}(p)$
2. Binomial Distribution $	ext{Bin}(n, p)$ as Sum of Independent Bernoullis
3. Sample Proportion $\hat{p} = rac{X}{n}$ Statistics
4. Normal Approximation to Binomial Distribution
5. Standard Error of Proportion $SE(\hat{p}) = \sqrt{rac{p(1-p)}{n}}$

## Why This Matters for AI
Binary classification accuracy, click-through rates (CTR), conversion rates in A/B testing, and precision/recall metrics are modeled statistically using Binomial proportion inference.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Compute sample proportion $\hat{p} = rac{X}{n}$
- [ ] Compute Standard Error $SE(\hat{p}) = \sqrt{rac{\hat{p}(1-\hat{p})}{n}}$
- [ ] Check Normal approximation condition $n p \ge 10, n(1-p) \ge 10$
- [ ] Compute proportion confidence intervals in Python

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
