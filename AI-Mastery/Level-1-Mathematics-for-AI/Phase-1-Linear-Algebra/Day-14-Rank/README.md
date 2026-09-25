# Day 14 — Rank

## Learning Objectives
- Understand Matrix Rank as the number of linearly independent rows or columns
- Distinguish between Full Rank and Rank Deficient matrices
- Calculate matrix rank using Gaussian elimination and NumPy `np.linalg.matrix_rank()`
- Connect matrix rank to feature redundancy and dimensionality reduction in ML

## Prerequisites
Day 7 — Matrices, Day 13 — Determinants

## Topics Covered
- Matrix Rank definition (Row rank = Column rank)
- Full Rank condition: $\text{Rank}(\mathbf{A}_{m \times n}) = \min(m, n)$
- Rank Deficient matrices and feature redundancy
- Rank of Matrix Product: $\text{Rank}(\mathbf{A}\mathbf{B}) \le \min(\text{Rank}(\mathbf{A}), \text{Rank}(\mathbf{B}))$
- Low-Rank Approximations (LoRA in LLMs)

## Why This Matters for AI
Rank measures true informational dimension. In Low-Rank Adaptation (LoRA) for fine-tuning LLMs, large weight updates $\Delta \mathbf{W}_{d \times d}$ are factorized into low-rank matrices $\mathbf{A}_{d \times r} \mathbf{B}_{r \times d}$ where $r \ll d$, saving 99% GPU memory.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Compute matrix rank in Python using NumPy and test low-rank matrix factorizations.

## Interview Preparation
Explain full rank vs rank deficiency and how LoRA leverages low-rank matrices in deep learning.

## Completion Checklist
- [ ] I can explain what matrix rank means
- [ ] I know the difference between full rank and rank deficiency
- [ ] I know why row rank equals column rank
- [ ] I can calculate matrix rank in Python

## Estimated Difficulty
Intermediate
