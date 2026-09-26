# Practice Exercises — Singular Value Decomposition

## Level 1 — Basic Understanding
1. Write the SVD factorization formula for matrix $\mathbf{A}_{m \times n}$.
2. What are the shapes of $\mathbf{U}$, $\mathbf{\Sigma}$, and $\mathbf{V}^T$ for a $100 \times 20$ matrix?
3. Can SVD be applied to a non-square $10 \times 3$ matrix?
4. How are singular values $\sigma_i$ calculated from eigenvalues of $\mathbf{A}^T \mathbf{A}$?
5. Are singular values ever negative?

## Level 2 — Calculation
1. Find the singular values of 

$$
\mathbf{A} = \begin{bmatrix} 3 & 0 \\ 0 & 4 \end{bmatrix}
$$

.
2. Calculate \mathbf{A}^T \mathbf{A} for 

$$
\mathbf{A} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}
$$

 and find its singular values.
3. If matrix $\mathbf{A}$ has rank $r = 3$, how many non-zero singular values does it have?
4. State the Eckart-Young Theorem for low-rank matrix approximation.
5. What is Truncated SVD?

## Level 3 — Conceptual
1. Prove that the left singular vectors $\mathbf{U}$ are eigenvectors of $\mathbf{A}\mathbf{A}^T$.
2. Prove that the right singular vectors $\mathbf{V}$ are eigenvectors of $\mathbf{A}^T\mathbf{A}$.
3. Show that for a real symmetric matrix with non-negative eigenvalues, SVD is identical to Eigendecomposition.
4. Explain how Moore-Penrose Pseudoinverse is computed using SVD: $\mathbf{A}^+ = \mathbf{V} \mathbf{\Sigma}^+ \mathbf{U}^T$.
5. What is the relationship between Frobenius norm $||\mathbf{A}||_F$ and singular values $\sigma_i$?

## Level 4 — AI/ML Application
1. A grayscale image of size $1000 \times 1000$ requires 1,000,000 floats. If we compress it using Truncated SVD with $k = 50$ singular values, how many floats are stored? Compute compression ratio.
2. In Netflix Recommendation Collaborative Filtering, rating matrix $R_{10000 \times 5000}$ is factorized into $U \Sigma V^T$ with rank $k=20$. Explain how user preferences are represented.
3. Explain how Latent Semantic Analysis (LSA) uses SVD on term-document matrices to discover latent semantic topics.

## Level 5 — Interview Questions
1. Prove that $||\mathbf{A}||_2 = \sigma_1$ (Spectral norm equals dominant singular value).
2. Explain Randomized SVD algorithm for computing fast approximate SVD on massive matrices ($O(mn \log k)$).
3. How does SVD resolve total least squares (Orthogonal Distance Regression) problems?
4. Why is SVD numerically preferred over explicit $\mathbf{A}^T \mathbf{A}$ matrix squaring for computing eigenvalues?
5. Explain the connection between SVD and Principal Component Analysis (PCA) on mean-centered datasets.
