# Day 101 — Random Number Generation

## Learning Objectives
- Master NumPy's `np.random` module and modern `Generator` API (`np.random.default_rng()`).
- Understand pseudo-random seeds (`np.random.seed` vs `Generator.seed`) for reproducibility.
- Generate Uniform, Normal, Binomial, and Poisson random distributions.

## Prerequisites
- Level 1: Probability Distributions
- Day 86: NumPy Introduction

## Topics Covered
1. Legacy `np.random` vs Modern `np.random.default_rng()` Generator API
2. Setting Random Seeds for Reproducibility (`seed`)
3. Uniform Distribution (`rng.uniform`, `rng.random`)
4. Gaussian Normal Distribution (`rng.normal`, `rng.standard_normal`)
5. Discrete Random Sampling (`rng.choice`, `rng.integers`, `rng.shuffle`)

## Why This Matters
Random number generation is used to initialize neural network weights, perform train/test splits, generate synthetic datasets, and run Monte Carlo simulations.

## Real-World Usage
Initializing neural network weight tensors with small random numbers $W \sim \mathcal{N}(0, 0.01)$ before training.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can generate uniform and normal random arrays.
- [ ] I understand how random seeds ensure experiment reproducibility.
- [ ] I know how to use `rng.choice()` for random sampling.
- [ ] I can connect random distributions to Level 1 probability distributions.

## Difficulty
Intermediate
