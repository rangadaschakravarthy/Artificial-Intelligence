# Practice Exercises — PCA Mathematics

## Level 1 — Basic Understanding
1. What are the 5 core mathematical steps of PCA?
2. Why must dataset features be mean-centered before PCA?
3. What do the eigenvalues of the covariance matrix represent?
4. If total eigenvalues sum to 100, and $\lambda_1 = 70, \lambda_2 = 20$, how much variance do the top 2 PCs explain?
5. Are principal component directions orthogonal to each other?

## Level 2 — Calculation
1. Given 2D centered data matrix 

$$
\mathbf{X}_c = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}
$$

, compute covariance matrix \mathbf{\Sigma}.
2. Compute eigenvalues of covariance matrix $\mathbf{\Sigma}$ from Question 1 above.
3. Find the normalized 1st principal component eigenvector $\mathbf{v}_1$.
4. Project sample $\mathbf{x}_c = [3, -3]^T$ onto PC1 eigenvector $\mathbf{v}_1$.
5. If a dataset has 10 features, what is the max number of principal components?

## Level 3 — Conceptual
1. Prove that the total variance of a dataset equals the sum of eigenvalues $\sum \text{Var}(X_i) = \sum \lambda_i$.
2. Derive why maximizing projection variance $\text{Var}(\mathbf{X}_c \mathbf{v}) = \mathbf{v}^T \mathbf{\Sigma} \mathbf{v}$ subject to $|\mathbf{v}\|_2 = 1$ leads to eigenvalue equation $\mathbf{\Sigma}\mathbf{v} = \lambda \mathbf{v}$ using Lagrange Multipliers.
3. Explain the difference between PCA (unsupervised variance maximization) and LDA (Linear Discriminant Analysis - supervised class separability).
4. Why should features be standardized (z-score scaling $\frac{x-\mu}{\sigma}$) before PCA if features have different measurement units?
5. How does SVD compute PCA without explicitly constructing covariance matrix $\mathbf{\Sigma}$?

## Level 4 — AI/ML Application
1. In Eigenfaces facial recognition, 10,000 pixel images (100x100) are reduced to $k=50$ principal components. Explain how a new face image is recognized using Euclidean distance in PCA space.
2. A dataset has 100 features. The scree plot shows cumulative explained variance: 10 PCs = 80%, 20 PCs = 95%, 50 PCs = 99%. How many PCs would you select for a downstream ML model?
3. Explain how PCA can be used for Image Noise Reduction by reconstructing images from top $k$ components.

## Level 5 — Interview Questions
1. Prove that PCA minimizes the reconstruction Error $|\mathbf{X}_c - \mathbf{X}_c \mathbf{W}_k \mathbf{W}_k^T||_F^2$.
2. What is Kernel PCA? How does it project data onto non-linear principal component manifolds using the kernel trick $\mathbf{K}_{i,j} = k(\mathbf{x}_i, \mathbf{x}_j)$?
3. Explain Probabilistic PCA (PPCA) and its formulation as a latent variable model $x = W z + \mu + \epsilon$.
4. Why does standard PCA struggle with sparse high-dimensional data (e.g. text Bag-of-Words), and why is Truncated SVD preferred?
5. How does Incremental PCA process streaming data batches that do not fit into RAM?
