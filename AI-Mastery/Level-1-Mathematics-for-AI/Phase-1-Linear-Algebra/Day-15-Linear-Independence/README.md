# Day 15 — Linear Independence

## Learning Objectives
- Understand Linear Independence vs Linear Dependence of vectors
- Formulate the linear combination condition: $c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = \mathbf{0} \implies c_i = 0$
- Test vector set independence using Determinants, Gaussian Elimination, and Rank
- Recognize feature redundancy in machine learning datasets

## Prerequisites
Day 3 — Vector Operations, Day 14 — Rank

## Topics Covered
- Linear Combination definition
- Definition of Linear Independence
- Definition of Linear Dependence (At least one vector is a combination of others)
- Testing Independence via Matrix Determinant $\det([v_1 \dots v_k]) \neq 0$
- Feature redundancy and collinearity in AI

## Why This Matters for AI
Linearly dependent feature vectors add no new information to ML models while increasing computation and causing unstable regression coefficients (multicollinearity).

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Check vector independence in Python by building a matrix and calculating determinant and rank.

## Interview Preparation
Explain linear independence definition and how to test if 3 vectors are independent.

## Completion Checklist
- [ ] I can state the formal definition of linear independence
- [ ] I can test if 2D or 3D vectors are independent manually
- [ ] I understand why dependent features harm regression models
- [ ] I can verify independence in Python using rank

## Estimated Difficulty
Intermediate
