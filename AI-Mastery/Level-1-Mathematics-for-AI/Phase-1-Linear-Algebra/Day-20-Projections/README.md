# Day 20 — Projections

## Learning Objectives
- Understand orthogonal vector projections $\text{proj}_{\mathbf{u}}(\mathbf{v})$ geometrically and algebraically
- Construct Projection Matrices $\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$
- Master projection matrix properties: Idempotent ($\mathbf{P}^2 = \mathbf{P}$) and Symmetric ($\mathbf{P}^T = \mathbf{P}$)
- Connect orthogonal projection to Ordinary Least Squares (OLS) regression

## Prerequisites
Day 4 — Dot Product, Day 16 — Vector Spaces

## Topics Covered
- Scalar and Vector Projection onto a line
- Formula: $\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{u}||^2} \mathbf{u}$
- Projection Matrix $\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$ onto a subspace
- Idempotent Property $\mathbf{P}^2 = \mathbf{P}$
- Orthogonal Error vector $\mathbf{e} = \mathbf{b} - \mathbf{P}\mathbf{b} \perp \text{Col}(\mathbf{A})$
- Geometric derivation of Linear Regression Least Squares

## Why This Matters for AI
Linear Regression minimizes squared prediction error by orthogonally projecting feature labels $\mathbf{y}$ onto the Column Space of data matrix $\mathbf{X}$.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Construct projection matrices in NumPy and project 3D points onto 2D planes.

## Interview Preparation
Explain why projection matrices are idempotent ($\mathbf{P}^2 = \mathbf{P}$) and how least squares relates to orthogonal projection.

## Completion Checklist
- [ ] I can calculate vector projection onto a line
- [ ] I can construct projection matrix $\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$
- [ ] I know projection properties $\mathbf{P}^2 = \mathbf{P}$ and $\mathbf{P}^T = \mathbf{P}$
- [ ] I can code projections in Python

## Estimated Difficulty
Intermediate
