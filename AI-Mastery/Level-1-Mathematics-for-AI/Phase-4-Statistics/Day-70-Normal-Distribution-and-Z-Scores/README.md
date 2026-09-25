# Day 70 — Normal Distribution and Z-Scores

## Learning Objectives
- Master Gaussian PDF $f(x) = rac{1}{\sigma \sqrt{2\pi}} e^{-rac{(x-\mu)^2}{2\sigma^2}}$.
- Master Standardization to $Z$-score $Z = rac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$.
- Apply 68-95-99.7 Empirical Rule.
- Perform outlier detection and standardization in Python.

## Prerequisites
- Days 51–52 Continuous distributions and Normal PDF.

## Topics Covered
1. Mathematical Properties of Gaussian Normal Distribution $\mathcal{N}(\mu, \sigma^2)$
2. Standard Normal Distribution $\mathcal{N}(0, 1)$
3. $Z$-Score Transformation $Z = rac{X - \mu}{\sigma}$
4. Empirical Rule (68.27% - 95.45% - 99.73%)
5. $Z$-Score Outlier Detection in ML (`StandardScaler`)

## Why This Matters for AI
$Z$-score standardization (`StandardScaler`) centers features at mean 0 with unit variance 1, preventing high-magnitude features from dominating distance calculations (k-NN, SVM, Gradient Descent).

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Convert raw $x$ to $Z$-score $Z = rac{x - \mu}{\sigma}$
- [ ] Look up standard normal probabilities $\Phi(z)$
- [ ] Apply 68-95-99.7 Empirical Rule
- [ ] Implement `StandardScaler` in Python

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
