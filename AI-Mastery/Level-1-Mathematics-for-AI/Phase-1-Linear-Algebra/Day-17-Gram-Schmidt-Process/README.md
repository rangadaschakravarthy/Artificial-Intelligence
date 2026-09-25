# Day 17: Gram-Schmidt Process

## Learning Objectives
- Master the Gram-Schmidt orthogonalization algorithm to convert any set of linearly independent vectors into an orthonormal basis.
- Understand vector projections and component subtraction geometrically.
- Understand the relationship between Gram-Schmidt and QR Decomposition in numerical Linear Algebra and AI.

## Prerequisites
- Day 15: Linear Independence
- Day 16: Orthogonality & Orthonormality
- Day 20: Projections

## Key Topics
1. Projection of a vector onto a line / subspace
2. Gram-Schmidt Algorithm: Iterative orthogonalization and normalization steps
3. Modified Gram-Schmidt (MGS) for numerical precision
4. QR Decomposition connection: A = QR where Q is orthogonal and R is upper triangular

## Recommended Study Order
1. Read `theory.md` thoroughly for 14 detailed sections.
2. Review `examples.md` covering 5 practical numerical & AI scenarios.
3. Solve all 23 practice problems in `practice.md`.
4. Verify your answers against `solution.md`.
5. Run and explore `code.py` for Python implementations.

## Checklist
- [ ] Understand the formula for vector projection: proj_u(v) = ((u . v) / ||u||^2) u
- [ ] Execute Gram-Schmidt manually for 2D and 3D vector sets
- [ ] Implement classical and modified Gram-Schmidt algorithms in Python
