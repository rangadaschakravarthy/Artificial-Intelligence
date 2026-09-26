# Day 100 — Mathematical Functions

## Learning Objectives
- Master mathematical ufuncs (`sin`, `cos`, `exp`, `log`, `log1p`, `sqrt`, `abs`).
- Understand rounding operations (`floor`, `ceil`, `round`, `trunc`).
- Learn numerical stability functions (handling small numbers and log transformations).

## Prerequisites
- Day 96: Array Operations

## Topics Covered
1. Exponential and Logarithmic ufuncs (`np.exp`, `np.log`, `np.log10`, `np.log1p`)
2. Trigonometric functions (`np.sin`, `np.cos`, `np.tan`, `np.pi`)
3. Rounding and Truncation (`np.floor`, `np.ceil`, `np.round`, `np.trunc`)
4. Absolute values and Sign functions (`np.abs`, `np.sign`)
5. Numerical stability and Log-Sum-Exp trick

## Why This Matters
Mathematical ufuncs are the core building blocks for activation functions (Sigmoid, Softmax, Tanh) and loss functions (Cross-Entropy, Log Loss) in AI.

## Real-World Usage
Applying log transformations `np.log1p(x)` to right-skewed feature variables (e.g. house prices, income) during data preprocessing.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can apply exponential, logarithmic, and trigonometric functions to arrays.
- [ ] I know when to use `np.log1p(x)` instead of `np.log(x)` for small values.
- [ ] I can round array values using `floor`, `ceil`, and `round`.
- [ ] I can implement activation functions like Tanh and Sigmoid using ufuncs.

## Difficulty
Intermediate
