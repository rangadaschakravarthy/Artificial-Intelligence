# Examples — PCA Mathematics

## Example 1 — Very Easy
Mean Centering: Data $[10, 20], [30, 40] \implies \mu = [20, 30] \implies$ Centered $[-10, -10], [10, 10]$.

## Example 2 — Beginner
2D Covariance Matrix: 

$$
\mathbf{\Sigma} = \begin{bmatrix} \text{Var}(X) & \text{Cov}(X,Y) \\ \text{Cov}(Y,X) & \text{Var}(Y) \end{bmatrix}
$$

.

## Example 3 — Intermediate
Explained Variance: $\lambda_1 = 15, \lambda_2 = 5 \implies$ PC1 explains $15/(15+5) = 75\%$, PC2 explains $25\%$.

## Example 4 — AI/ML Example
2D Data Visualization: Projecting 50D gene expression data onto top 2 principal components.

## Example 5 — Real-World Interpretation
SVD-PCA Equivalence: PCA principal components equal right singular vectors $V$ of mean-centered matrix.
