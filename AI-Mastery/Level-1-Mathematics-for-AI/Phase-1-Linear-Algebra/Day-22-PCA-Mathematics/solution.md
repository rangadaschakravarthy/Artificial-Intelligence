# Solutions — PCA Mathematics

## Level 1 — Basic Understanding Solutions
### Question 1
1. 1) Mean-center data, 2) Compute Covariance Matrix $\mathbf{\Sigma}$, 3) Calculate eigenvalues and eigenvectors of $\mathbf{\Sigma}$, 4) Sort eigenvectors by eigenvalue magnitude, 5) Project data onto top $k$ eigenvectors.
### Question 2
2. To ensure that covariance measures scatter around the mean rather than distance from origin.
### Question 3
3. Eigenvalues represent the variance of the data along each corresponding principal component direction.
### Question 4
4. $(70 + 20) / 100 = 90\%$ of total dataset variance.
### Question 5
5. Yes! Principal components are eigenvectors of a real symmetric covariance matrix, making them strictly mutually orthogonal.

## Level 2 — Calculation Solutions
### Question 1
1. 

$$
\mathbf{\Sigma} = \frac{1}{2-1} \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}^T \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} = \begin{bmatrix} 1+1 & -1-1 \\ -1-1 & 1+1 \end{bmatrix} = \begin{bmatrix} 2 & -2 \\ -2 & 2 \end{bmatrix}
$$

.
### Question 2
2. 

$$
\det \begin{bmatrix} 2-\lambda & -2 \\ -2 & 2-\lambda \end{bmatrix} = (2-\lambda)^2 - 4 = 0 \implies (2-\lambda) = \pm 2 \implies \lambda_1 = 4, \lambda_2 = 0
$$

.
### Question 3
3. For \lambda_1 = 4: 

$$
\begin{bmatrix} -2 & -2 \\ -2 & -2 \end{bmatrix} \mathbf{v} = \mathbf{0} \implies v_1 + v_2 = 0
$$

. Normalized \mathbf{v}_1 = [1/\sqrt{2}, -1/\sqrt{2}]^T.
### Question 4
4. $z_1 = [3, -3] \cdot [1/\sqrt{2}, -1/\sqrt{2}]^T = \frac{3+3}{\sqrt{2}} = \frac{6}{\sqrt{2}} = 3\sqrt{2} \approx 4.242$.
### Question 5
5. Maximum 10 principal components.

## Level 3 — Conceptual Solutions
### Question 1
1. $\text{Total Var} = \sum_{i=1}^d \text{Var}(X_i) = \text{Tr}(\mathbf{\Sigma})$. Since trace equals sum of eigenvalues, $\text{Tr}(\mathbf{\Sigma}) = \sum_{i=1}^d \lambda_i$.
### Question 2
2. Objective $\mathcal{L}(\mathbf{v}, \lambda) = \mathbf{v}^T \mathbf{\Sigma} \mathbf{v} - \lambda(\mathbf{v}^T \mathbf{v} - 1)$. Taking gradient w.r.t $\mathbf{v}$: $\frac{\partial \mathcal{L}}{\partial \mathbf{v}} = 2\mathbf{\Sigma}\mathbf{v} - 2\lambda \mathbf{v} = \mathbf{0} \implies \mathbf{\Sigma}\mathbf{v} = \lambda \mathbf{v}$. Exact eigenvalue equation!
### Question 3
3. PCA maximizes total dataset variance without using class labels (unsupervised). LDA maximizes between-class variance while minimizing within-class variance using labels (supervised).
### Question 4
4. If one feature is measured in meters (values ~1) and another in millimeters (values ~1000), unscaled PCA will assign 99.9% of variance to the millimeter feature regardless of true information content.
### Question 5
5. Compute SVD on mean-centered $\mathbf{X}_c = \mathbf{U}\mathbf{\Sigma}_{svd}\mathbf{V}^T$. Columns of $\mathbf{V}$ are PCA principal components, avoiding explicit $\mathbf{X}_c^T \mathbf{X}_c$ computation.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Image $x$ is mean-centered and projected to 50D coordinate vector $\mathbf{z} = \mathbf{W}_{50}^T \mathbf{x}_c$. Compare candidate face's 50D vector against database face vectors using Euclidean distance. Nearest vector identifies person.
### Question 2
2. Select 20 PCs (capturing 95% variance). It removes 80% of feature dimensions while preserving 95% of total signal, avoiding overfitting.
### Question 3
3. Reconstruct data using top $k$ PCs: $\hat{\mathbf{X}} = \mathbf{X}_c \mathbf{W}_k \mathbf{W}_k^T + \mathbf{\mu}$. Discarded lower PCs contain high-frequency random noise, leaving a clean denoised image.

## Level 5 — Interview Questions Solutions
### Question 1
1. By Pythagorean theorem on orthogonal projection, minimizing reconstruction error $\|\mathbf{X}_c - \mathbf{X}_c \mathbf{W}_k \mathbf{W}_k^T\|_F^2$ is mathematically equivalent to maximizing projection variance $\text{Tr}(\mathbf{W}_k^T \mathbf{\Sigma} \mathbf{W}_k)$. Eckart-Young theorem guarantees optimal choice is top $k$ eigenvectors of $\mathbf{\Sigma}$.
### Question 2
2. Kernel PCA uses non-linear feature map $\phi(\mathbf{x})$ and kernel function $K_{i,j} = k(x_i, x_j) = \langle \phi(x_i), \phi(x_j) \rangle$. Eigendecomposition is computed on centered Kernel matrix $\mathbf{K}_c$, projecting data onto non-linear manifolds.
### Question 3
3. PPCA models observed data $x \sim \mathcal{N}(\mu, W W^T + \sigma^2 I)$ with Gaussian latent variable $z \sim \mathcal{N}(0, I)$, solved using Expectation-Maximization (EM) algorithm.
### Question 4
4. Mean-centering sparse matrices ($X_c = X - \mu$) destroys sparsity, filling zero entries with non-zero mean values $\mu$ and causing RAM overflow. Truncated SVD operates directly on sparse matrices without mean centering.
### Question 5
5. Incremental PCA updates principal components using mini-batch SVD updates (e.g. Memory-Mapped files or `sklearn.decomposition.IncrementalPCA`), processing massive datasets chunk-by-chunk.
