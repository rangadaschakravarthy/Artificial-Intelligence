# Theory — PCA Mathematics

### 1. Simple Definition
PCA is a technique that reduces the number of features in a dataset while keeping as much of the original variance (information) as possible.

### 2. Intuition
Imagine a 3D point cloud of data shaped like an elongated oval pancake. PCA rotates the coordinate system so the 1st axis points along the pancake's longest length, and 2nd axis points along its width, allowing us to drop the thin height axis with minimal loss!

### 3. Mathematical Definition
Given data matrix $\mathbf{X} \in \mathbb{R}^{N \times d}$: 1) Mean center $\mathbf{X}_c = \mathbf{X} - \mathbf{1}\mathbf{\mu}^T$. 2) Covariance matrix $\mathbf{\Sigma} = \frac{1}{N-1}\mathbf{X}_c^T \mathbf{X}_c \in \mathbb{R}^{d \times d}$. 3) Solve $\mathbf{\Sigma}\mathbf{v}_i = \lambda_i \mathbf{v}_i$. Sort $\lambda_1 \ge \lambda_2 \dots \ge \lambda_d$. 4) Select top $k$ eigenvectors $\mathbf{W}_k = [\mathbf{v}_1 \dots \mathbf{v}_k]$. 5) Project $\mathbf{Z} = \mathbf{X}_c \mathbf{W}_k \in \mathbb{R}^{N \times k}$.

### 4. Notation
$\mathbf{X}_c$: Mean-centered data. $\mathbf{\Sigma}$: Covariance matrix. $\mathbf{v}_1, \dots, \mathbf{v}_k$: Principal components (eigenvectors). $\mathbf{Z}$: Projected low-dimensional dataset.

### 5. Formula
$$\mathbf{\Sigma} = \frac{1}{N-1}\mathbf{X}_c^T \mathbf{X}_c$$
$$\text{Explained Variance Ratio}_i = \frac{\lambda_i}{\sum_{j=1}^d \lambda_j}$$

### 6. Symbol-by-Symbol Explanation
- $N$: Number of data samples
- $d$: Original feature count
- $k$: Reduced feature count ($k < d$)
- $\lambda_i$: Eigenvalue measuring variance along component $i$

### 7. Step-by-Step Calculation
PCA on 2D dataset with 3 samples: $x_1=[1,2]^T, x_2=[3,4]^T, x_3=[5,6]^T$:
1. Mean vector $\mathbf{\mu} = [(1+3+5)/3, (2+4+6)/3]^T = [3, 4]^T$.
2. Centered data $\mathbf{X}_c = \begin{bmatrix} 1-3 & 2-4 \\ 3-3 & 4-4 \\ 5-3 & 6-4 \end{bmatrix} = \begin{bmatrix} -2 & -2 \\ 0 & 0 \\ 2 & 2 \end{bmatrix}$.
3. Covariance matrix $\mathbf{\Sigma} = \frac{1}{2} \mathbf{X}_c^T \mathbf{X}_c = \frac{1}{2} \begin{bmatrix} 8 & 8 \\ 8 & 8 \end{bmatrix} = \begin{bmatrix} 4 & 4 \\ 4 & 4 \end{bmatrix}$.
4. Eigenvalues of $\mathbf{\Sigma}$: $\det \begin{bmatrix} 4-\lambda & 4 \\ 4 & 4-\lambda \end{bmatrix} = (4-\lambda)^2 - 16 = 0 \implies \lambda_1 = 8, \lambda_2 = 0$.
5. Total variance $= 8+0=8$. PC1 explains $8/8 = 100\%$ of variance!

### 8. Second Example
Project sample $x_3$ onto PC1 eigenvector $\mathbf{v}_1 = [1/\sqrt{2}, 1/\sqrt{2}]^T$:
$z_3 = \mathbf{x}_{c,3}^T \mathbf{v}_1 = [2, 2] \cdot [1/\sqrt{2}, 1/\sqrt{2}]^T = \frac{4}{\sqrt{2}} = 2\sqrt{2} \approx 2.828$.

### 9. Common Mistakes
Forgetting to mean-center data before PCA (causes 1st principal component to point from origin to data mean rather than along variance axis); failing to scale features when units differ.

### 10. AI Connection
Preprocessing tabular data for ML models, reducing 784D MNIST digit images to 2D for scatter plot visualization, Eigenfaces facial recognition.

### 11. Algorithm Connection
PCA, Truncated SVD, Kernel PCA, Feature Selection, Data Visualization.

### 12. Practical Interpretation
Principal Component 1 is the direction in feature space along which data points vary the most. Principal Component 2 is orthogonal to PC1 with 2nd highest variance.

### 13. Interview Insight
Q: 'Why MUST data be mean-centered before performing PCA?' A: Covariance matrix $\mathbf{X}^T \mathbf{X}$ measures scatter around the origin. Without subtracting mean $\mathbf{\mu}$, the first principal component aligns with the mean vector location rather than max variance.

### 14. Summary
PCA reduces features by projecting data onto eigenvectors of covariance matrix $\mathbf{\Sigma} = \frac{1}{N-1}\mathbf{X}_c^T \mathbf{X}_c$. Explained variance ratio $= \frac{\lambda_i}{\sum \lambda_j}$.
