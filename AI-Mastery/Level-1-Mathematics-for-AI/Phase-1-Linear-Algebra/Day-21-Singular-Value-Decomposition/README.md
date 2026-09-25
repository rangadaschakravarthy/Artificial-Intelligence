# Day 21 — Singular Value Decomposition

## Learning Objectives
- Master Singular Value Decomposition (SVD) formula $\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$ for any rectangular matrix
- Understand Left Singular Vectors $\mathbf{U}$, Singular Values $\mathbf{\Sigma}$, and Right Singular Vectors $\mathbf{V}$
- Calculate SVD step-by-step using $\mathbf{A}^T \mathbf{A}$ and $\mathbf{A} \mathbf{A}^T$
- Apply Truncated SVD for image compression and recommendation system matrix factorization

## Prerequisites
Day 10 — Transpose, Day 19 — Eigenvalues and Eigenvectors

## Topics Covered
- SVD Theorem for rectangular matrices $\mathbf{A}_{m \times n}$
- Formula: $\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$
- Singular values $\sigma_i = \sqrt{\lambda_i(\mathbf{A}^T \mathbf{A})}$
- Full SVD vs Truncated (Reduced) SVD
- Low-Rank Approximation (Eckart-Young Theorem)

## Why This Matters for AI
SVD works on ANY rectangular matrix, making it the workhorse of dimensionality reduction (Truncated SVD), Latent Semantic Analysis (LSA in NLP), Collaborative Filtering (Netflix recommendation), and Pseudoinverses.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Compute full and truncated SVD in Python using `np.linalg.svd()` and perform image compression.

## Interview Preparation
Explain SVD vs Eigendecomposition, singular values, and Truncated SVD image compression.

## Completion Checklist
- [ ] I can state the SVD formula $A = U \Sigma V^T$
- [ ] I know how singular values $\sigma_i$ relate to eigenvalues of $A^T A$
- [ ] I can perform Low-Rank Matrix Approximation using SVD
- [ ] I can compute SVD in Python

## Estimated Difficulty
Advanced
