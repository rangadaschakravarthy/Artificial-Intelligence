# Day 13 — Determinants

## Learning Objectives
- Understand the determinant $\det(\mathbf{A})$ as the geometric volume scaling factor of a matrix transformation
- Calculate $2 \times 2$ and $3 \times 3$ determinants manually
- Master key determinant properties: $\det(\mathbf{A}\mathbf{B}) = \det(\mathbf{A})\det(\mathbf{B})$, $\det(\mathbf{A}^T) = \det(\mathbf{A})$
- Determine matrix invertibility using $\det(\mathbf{A}) \neq 0$

## Prerequisites
Day 7 — Matrices, Day 9 — Matrix Multiplication

## Topics Covered
- Geometric intuition of Determinant (Area / Volume expansion ratio)
- $2 \times 2$ Determinant formula: $ad - bc$
- $3 \times 3$ Determinant Cofactor Expansion Rule
- Properties of Determinants (Multiplicative, Transpose, Row Swapping)
- Zero determinant and dimensional collapse

## Why This Matters for AI
Determinants measure space scaling. In change-of-variable calculus for probability density functions (Normalizing Flows in Generative AI), Jacobian determinants maintain probability mass conservation.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Calculate determinants in Python using `np.linalg.det()` and visualize 2D transformation area.

## Interview Preparation
Explain geometric meaning of determinant and why $\det(\mathbf{A}) = 0$ means non-invertible.

## Completion Checklist
- [ ] I can calculate a 2x2 determinant manually
- [ ] I can compute a 3x3 determinant using cofactor expansion
- [ ] I know geometric meaning of determinant
- [ ] I can calculate determinants in Python

## Estimated Difficulty
Intermediate
