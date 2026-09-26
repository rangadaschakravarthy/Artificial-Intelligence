# Practice Exercises — Rank

## Level 1 — Basic Understanding
1. What is the maximum possible rank of a $5 \times 3$ matrix?
2. Find the rank of 

$$
\mathbf{A} = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}
$$

.
3. What is the rank of an $n \times n$ identity matrix $\mathbf{I}_n$?
4. What is the rank of a zero matrix $\mathbf{0}_{4 \times 4}$?
5. What does 'full rank' mean for a $4 \times 4$ matrix?

## Level 2 — Calculation
1. Determine the rank of 

$$
\mathbf{B} = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 5 \end{bmatrix}
$$

.
2. Given \mathbf{u} = [1, 2]^T and \mathbf{v} = [3, 4]^T, what is the rank of outer product 

$$
\mathbf{u} \mathbf{v}^T = \begin{bmatrix} 3 & 4 \\ 6 & 8 \end{bmatrix}
$$

?
3. If $\mathbf{A}$ has shape $100 \times 10$ and $\text{Rank}(\mathbf{A}) = 8$, how many linearly independent columns does it have?
4. If $\mathbf{A}$ is a $3 \times 3$ matrix with $\det(\mathbf{A}) = 0$, what can you say about its rank?
5. What is the rank of a diagonal matrix with 4 non-zero and 2 zero entries on the main diagonal?

## Level 3 — Conceptual
1. Prove that $\text{Rank}(\mathbf{A}^T) = \text{Rank}(\mathbf{A})$.
2. Explain the Rank-Nullity Theorem: $\text{Rank}(\mathbf{A}) + \text{Nullity}(\mathbf{A}) = n$.
3. Show that $\text{Rank}(\mathbf{A}\mathbf{B}) \le \min(\text{Rank}(\mathbf{A}), \text{Rank}(\mathbf{B}))$.
4. Why does adding a scalar multiple of one row to another leave matrix rank unchanged?
5. How does SVD (Singular Value Decomposition) determine the numerical rank of a matrix?

## Level 4 — AI/ML Application
1. In LoRA, a weight update $\Delta \mathbf{W}$ of shape $2048 \times 2048$ is decomposed into $\mathbf{A}_{2048 \times 8} \mathbf{B}_{8 \times 2048}$. What is the maximum rank of $\Delta \mathbf{W}$? Compute parameter reduction percentage.
2. A dataset feature matrix $\mathbf{X}_{1000 \times 50}$ has rank 30. How many features are redundant? What ML technique can remove them?
3. Explain why multicollinearity in linear regression leads to rank deficiency in $\mathbf{X}^T \mathbf{X}$.

## Level 5 — Interview Questions
1. State and prove the Eckart-Young-Mirsky Theorem for best low-rank matrix approximation using SVD.
2. Explain how matrix rank is used in Collaborative Filtering for recommendation systems (Matrix Factorization).
3. What is the difference between exact algebraic rank and numerical rank under floating-point noise?
4. How does SVD thresholding $(\sigma_i > \epsilon)$ determine effective matrix rank?
5. Why is finding the minimum rank matrix completion under sparse observations NP-hard, and how does nuclear norm relaxation solve it?
