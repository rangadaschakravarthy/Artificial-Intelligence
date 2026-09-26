# Theory — Eigenvalues and Eigenvectors

### 1. Simple Definition
An eigenvector of a matrix is a special vector that does NOT change its direction when multiplied by the matrix—it is only scaled. The scaling factor is called the eigenvalue.

### 2. Intuition
Imagine stretching a rubber sheet. Most points get pulled sideways and change direction. But points along the main stretch axes only move further out along the exact same straight line! Those stretch axes are eigenvectors, and the stretch factors are eigenvalues.

### 3. Mathematical Definition
For square matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$, a non-zero vector $\mathbf{v} \neq \mathbf{0}$ is an eigenvector if:
$$\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$$
where scalar $\lambda \in \mathbb{C}$ is the corresponding eigenvalue. Eigenvalues are roots of characteristic polynomial $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$.

### 4. Notation
$\mathbf{v}$ for eigenvector, $\lambda$ for eigenvalue. Diagonal matrix of eigenvalues $\mathbf{\Lambda} = \text{diag}(\lambda_1, \dots, \lambda_n)$.

### 5. Formula
$$\det(\mathbf{A} - \lambda \mathbf{I}) = 0 \implies \text{Solve for } \lambda$$
$$(\mathbf{A} - \lambda_i \mathbf{I})\mathbf{v}_i = \mathbf{0} \implies \text{Solve for } \mathbf{v}_i$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{A}$: Square $n \times n$ matrix
- $\mathbf{v}$: Eigenvector (non-zero)
- $\lambda$: Eigenvalue scalar
- $\mathbf{I}$: Identity matrix

### 7. Step-by-Step Calculation
Find eigenvalues of 

$$\mathbf{A} = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$$

:
1. 

$$\det(\mathbf{A} - \lambda \mathbf{I}) = \det \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} = (4-\lambda)(3-\lambda) - 2 = 0$$

.
2. $\lambda^2 - 7\lambda + 12 - 2 = \lambda^2 - 7\lambda + 10 = 0$.
3. Factor: $(\lambda - 5)(\lambda - 2) = 0 \implies \lambda_1 = 5, \lambda_2 = 2$.
4. Find eigenvector for \lambda_1 = 5: 

$$(\mathbf{A} - 5\mathbf{I})\mathbf{v} = \begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies -v_1 + v_2 = 0 \implies \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

.

### 8. Second Example
Find eigenvector for \lambda_2 = 2: 

$$(\mathbf{A} - 2\mathbf{I})\mathbf{v} = \begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies 2v_1 + v_2 = 0 \implies \mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$$

.

### 9. Common Mistakes
Assuming eigenvectors can be the zero vector $\mathbf{0}$ (eigenvectors MUST be non-zero!); forgetting that eigenvalues can be complex numbers for non-symmetric matrices.

### 10. AI Connection
Principal Component Analysis (PCA): Eigenvectors of dataset covariance matrix $\mathbf{\Sigma}$ represent directions of maximum variance. Spectral Graph Convolution (GCNs): Graph Laplacian eigenvectors define graph frequency domain.

### 11. Algorithm Connection
PCA, PageRank (Google), Spectral Clustering, Graph Neural Networks (GCN), Markov Chains.

### 12. Practical Interpretation
Spectral Theorem: Every real symmetric matrix $\mathbf{A} = \mathbf{A}^T$ has strictly real eigenvalues and mutually orthogonal eigenvectors: $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^T$.

### 13. Interview Insight
Q: 'How are trace and determinant related to eigenvalues?' A: Trace equals sum of eigenvalues $\text{Tr}(\mathbf{A}) = \sum \lambda_i$. Determinant equals product of eigenvalues $\det(\mathbf{A}) = \prod \lambda_i$.

### 14. Summary
Eigenvalue equation $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$. Eigenvectors are invariant directional axes under matrix scaling $\lambda$. For real symmetric matrices, eigenvectors are mutually orthogonal.
