# Day 12 — Matrix Inverse

## Learning Objectives
- Understand the inverse of a square matrix $\mathbf{A}^{-1}$ such that $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$
- Distinguish between invertible (non-singular) and non-invertible (singular) matrices
- Calculate the inverse of a $2 \times 2$ matrix manually using formula
- Solve linear systems $\mathbf{A}\mathbf{x} = \mathbf{b} \implies \mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$

## Prerequisites
Day 9 — Matrix Multiplication, Day 11 — Identity Matrix

## Topics Covered
- Matrix Inverse definition: $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$
- Invertibility condition ($\det(\mathbf{A}) \neq 0$)
- Formula for 2 \times 2 inverse: 

$$
\mathbf{A}^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
$$

- Properties of Inverses: $(\mathbf{A}^{-1})^{-1} = \mathbf{A}$, $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$
- Solving linear systems $\mathbf{A}\mathbf{x} = \mathbf{b}$

## Why This Matters for AI
Matrix inversion is used to compute exact closed-form linear regression parameters $\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ and in Gaussian Process inference.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Compute matrix inverses using NumPy `np.linalg.inv()` and solve linear equations using `np.linalg.solve()`.

## Interview Preparation
Explain why singular matrices cannot be inverted and why `solve()` is preferred over explicit `inv()` in production code.

## Completion Checklist
- [ ] I can calculate a 2x2 matrix inverse manually
- [ ] I know the condition for invertibility ($\det 
\neq 0$)
- [ ] I know the product inverse rule $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$
- [ ] I can solve linear systems in Python

## Estimated Difficulty
Intermediate
