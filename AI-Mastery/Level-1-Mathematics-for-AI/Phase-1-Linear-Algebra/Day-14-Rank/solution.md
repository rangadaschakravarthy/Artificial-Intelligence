# Solutions — Rank

## Level 1 — Basic Understanding Solutions
### Question 1
1. Maximum rank is $\min(5, 3) = 3$.
### Question 2
2. Row 1 is $2 \times$ Row 2 ($[2, 4] = 2[1, 2]$). There is only 1 independent row $\implies \text{Rank} = 1$.
### Question 3
3. $\text{Rank}(\mathbf{I}_n) = n$.
### Question 4
4. $\text{Rank}(\mathbf{0}) = 0$.
### Question 5
5. 'Full rank' means $\text{Rank}(\mathbf{A}) = 4$ (all 4 rows and columns are linearly independent).

## Level 2 — Calculation Solutions
### Question 1
1. Upper triangular with non-zero diagonal entries $[1, 1, 5]$. All 3 rows are independent $\implies \text{Rank} = 3$.
### Question 2
2. $\text{Rank}(\mathbf{u} \mathbf{v}^T) = 1$ (all rows are scalar multiples of $\mathbf{v}^T$).
### Question 3
3. It has exactly 8 linearly independent columns.
### Question 4
4. Since $\det(\mathbf{A}) = 0$, it is rank deficient, so $\text{Rank}(\mathbf{A}) < 3$ (either 0, 1, or 2).
### Question 5
5. Rank equals the number of non-zero diagonal elements $= 4$.

## Level 3 — Conceptual Solutions
### Question 1
1. Fundamental theorem of linear algebra states row rank equals column rank. Transposing converts rows to columns, preserving rank: $\text{Rank}(\mathbf{A}^T) = \text{Rank}(\mathbf{A})$.
### Question 2
2. For matrix $\mathbf{A}_{m \times n}$, dimension of column space (Rank) plus dimension of kernel/nullspace (Nullity) equals total domain dimension $n$.
### Question 3
3. The output column space of $\mathbf{A}\mathbf{B}$ is a subspace of the column space of $\mathbf{A}$, so its dimension cannot exceed $\text{Rank}(\mathbf{A})$. Similarly for rows of $\mathbf{B}$.
### Question 4
4. Elementary row operations preserve the span of the row space, leaving the number of linearly independent rows completely unchanged.
### Question 5
5. SVD counts the number of non-zero singular values $\sigma_i > 0$. Number of non-zero singular values equals matrix rank.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Max rank of $\Delta \mathbf{W} = \mathbf{A}\mathbf{B}$ is $\min(8, 8) = 8$. Full matrix has $2048 \times 2048 = 4,194,304$ params. LoRA params $= 2 \times 2048 \times 8 = 32,768$ params. Reduction $= 1 - (32768 / 4194304) \approx 99.22\%$ savings!
### Question 2
2. $50 - 30 = 20$ redundant features. Principal Component Analysis (PCA) or Truncated SVD can reduce dimensionality to 30 components without information loss.
### Question 3
3. Multicollinearity means feature columns are linear combinations of each other. $\mathbf{X}_{100 \times p}$ becomes rank deficient ($r < p$), making $\mathbf{X}^T \mathbf{X}$ singular and non-invertible.

## Level 5 — Interview Questions Solutions
### Question 1
1. Eckart-Young theorem states that the optimal rank-$k$ matrix $\mathbf{A}_k$ minimizing Frobenius norm error $|\mathbf{A} - \mathbf{A}_k||_F$ is obtained by truncating SVD to top $k$ singular values: $\mathbf{A}_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^T$.
### Question 2
2. Ratings matrix $R_{users \times items}$ is sparse and low-rank. Matrix factorization decomposes $R \approx U_{users \times k} V_{k \times items}^T$, uncovering $k$ latent user preference factors.
### Question 3
3. Exact algebraic rank counts strictly non-zero components. Under floating-point noise, zero singular values become small numbers (e.g. $10^{-16}$). Numerical rank counts singular values above threshold $\epsilon$.
### Question 4
4. Numerical rank threshold $\epsilon = \max(m, n) \cdot \text{eps} \cdot \sigma_1$. Singular values below $\epsilon$ are treated as zero noise.
### Question 5
5. Rank minimization $\min \text{Rank}(X)$ is non-convex NP-hard. Convex relaxation replaces rank with nuclear norm $||X||_* = \sum \sigma_i(X)$ (sum of singular values), solved via semi-definite programming.
