# Practice Exercises — Eigenvalues and Eigenvectors

## Level 1 — Basic Understanding
1. Write the eigenvalue equation $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$.
2. What is the characteristic equation used to solve for eigenvalues?
3. Find eigenvalues of diagonal matrix 

$$\mathbf{D} = \begin{bmatrix} 8 & 0 \\ 0 & 3 \end{bmatrix}$$

.
4. If $\lambda_1 = 4$ and $\lambda_2 = 6$ for a $2 \times 2$ matrix, what is $\text{Tr}(\mathbf{A})$ and $\det(\mathbf{A})$?
5. Can an eigenvector be the zero vector $\mathbf{0}$?

## Level 2 — Calculation
1. Compute eigenvalues of 

$$\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

.
2. Find the normalized eigenvectors corresponding to eigenvalues computed above.
3. Verify that \text{Tr}(\mathbf{A}) = \lambda_1 + \lambda_2 and \det(\mathbf{A}) = \lambda_1 \lambda_2 for 

$$\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

.
4. If $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$, show that $\mathbf{A}^2 \mathbf{v} = \lambda^2 \mathbf{v}$.
5. What are the eigenvalues of $\mathbf{A}^{-1}$ in terms of $\lambda_i$?

## Level 3 — Conceptual
1. State the Spectral Theorem for real symmetric matrices.
2. Prove that eigenvalues of a real symmetric matrix $\mathbf{A} = \mathbf{A}^T$ are always real numbers.
3. Prove that eigenvectors corresponding to distinct eigenvalues of a symmetric matrix are mutually orthogonal.
4. What does a zero eigenvalue $\lambda = 0$ imply about matrix rank and determinant?
5. What is the Power Iteration algorithm for finding dominant eigenvalue?

## Level 4 — AI/ML Application
1. In PCA, dataset covariance matrix is 

$$\mathbf{\Sigma} = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$$

. Compute eigenvalues \lambda_1, \lambda_2. What percentage of total variance is explained by the 1st principal component?
2. Google's PageRank models web browsing as Markov chain $\mathbf{p}_{t+1} = \mathbf{M} \mathbf{p}_t$. Why does steady-state stationarity require $\mathbf{M}\mathbf{p} = 1 \cdot \mathbf{p}$?
3. Explain how Spectral Graph Convolutions use the Graph Laplacian matrix $L = D - A$ eigenvalues to perform convolutions on non-Euclidean graph networks.

## Level 5 — Interview Questions
1. Prove Eigendecomposition formula $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^{-1}$.
2. Explain Positive Semi-Definite (PSD) matrix definition: $\mathbf{x}^T \mathbf{A} \mathbf{x} \ge 0 \iff \lambda_i \ge 0 \quad \forall i$.
3. Why do non-symmetric matrices sometimes lack a full set of $n$ linearly independent eigenvectors (Defective matrices / Jordan Normal Form)?
4. What is the Rayleigh Quotient $R(\mathbf{A}, \mathbf{x}) = \frac{\mathbf{x}^T \mathbf{A} \mathbf{x}}{\mathbf{x}^T \mathbf{x}}$ and how does it maximize variance in PCA?
5. Explain Gershgorin Circle Theorem for bounding eigenvalue locations in complex plane.
