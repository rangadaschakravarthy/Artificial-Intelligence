# Theory — Singular Value Decomposition

### 1. Simple Definition
SVD breaks any matrix down into 3 fundamental geometric steps: a rotation ($\mathbf{V}^T$), a scaling along coordinate axes ($\mathbf{\Sigma}$), and a second rotation ($\mathbf{U}$).

### 2. Intuition
Imagine taking a photo of a 3D object. SVD breaks down the photo creation into: rotating the object to a good angle ($\mathbf{V}^T$), scaling the dimensions ($\mathbf{\Sigma}$), and projecting/rotating onto the 2D camera sensor ($\mathbf{U}$).

### 3. Mathematical Definition
Any real matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ can be factorized as:
$$\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$$
where $\mathbf{U} \in \mathbb{R}^{m \times m}$ is an orthogonal matrix of left singular vectors (eigenvectors of $\mathbf{A}\mathbf{A}^T$), $\mathbf{V} \in \mathbb{R}^{n \times n}$ is an orthogonal matrix of right singular vectors (eigenvectors of $\mathbf{A}^T \mathbf{A}$), and $\mathbf{\Sigma} \in \mathbb{R}^{m \times n}$ is a diagonal matrix of singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$.

### 4. Notation
$\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$. Singular values $\sigma_i = \sqrt{\lambda_i(\mathbf{A}^T \mathbf{A})}$.

### 5. Formula
$$\mathbf{A} = \sum_{i=1}^r \sigma_i \mathbf{u}_i \mathbf{v}_i^T = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^T + \dots + \sigma_r \mathbf{u}_r \mathbf{v}_r^T$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{U}_{m \times m}$: Orthonormal left singular vectors
- $\mathbf{\Sigma}_{m \times n}$: Non-negative diagonal singular values
- $\mathbf{V}^T_{n \times n}$: Transposed orthonormal right singular vectors
- $r$: Rank of matrix $\mathbf{A}$

### 7. Step-by-Step Calculation
Calculate singular values of $\mathbf{A} = \begin{bmatrix} 3 & 0 \\ 0 & -2 \end{bmatrix}$:
1. $\mathbf{A}^T \mathbf{A} = \begin{bmatrix} 9 & 0 \\ 0 & 4 \end{bmatrix}$.
2. Eigenvalues of $\mathbf{A}^T \mathbf{A}$ are $\lambda_1 = 9, \lambda_2 = 4$.
3. Singular values $\sigma_1 = \sqrt{9} = 3, \sigma_2 = \sqrt{4} = 2$.
4. $\mathbf{\Sigma} = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}$.

### 8. Second Example
Low-rank approximation: Keeping only top 1 singular value $\mathbf{A}_1 = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T$ gives the best rank-1 approximation of matrix $\mathbf{A}$.

### 9. Common Mistakes
Confusing Eigendecomposition (requires square matrix) with SVD (works on ANY $m \times n$ rectangular matrix); forgetting that singular values are ALWAYS non-negative ($\sigma_i \ge 0$).

### 10. AI Connection
Latent Semantic Analysis (LSA) in NLP factorizes term-document matrices. Collaborative Filtering in Recommender Systems factorizes User-Item rating matrices. Truncated SVD compresses large neural network weight matrices.

### 11. Algorithm Connection
Principal Component Analysis (PCA), Latent Semantic Analysis (LSA), Matrix Completion, Recommender Systems, SVD-LLM.

### 12. Practical Interpretation
Truncated SVD keeps only top $k$ singular values $\sigma_1 \dots \sigma_k$, discarding noise and retaining $(90\%+)$ of data variance.

### 13. Interview Insight
Q: 'What is the main difference between Eigendecomposition and SVD?' A: Eigendecomposition $\mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^{-1}$ requires square matrices and uses same basis $\mathbf{Q}$. SVD $\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$ works on any $m \times n$ matrix and uses two distinct orthonormal bases $\mathbf{U}$ and $\mathbf{V}$.

### 14. Summary
SVD factorizes any matrix $\mathbf{A}_{m \times n} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$. Singular values $\sigma_i = \sqrt{\lambda_i(\mathbf{A}^T\mathbf{A})}$ quantify mode importance. Truncated SVD enables optimal low-rank matrix compression.
