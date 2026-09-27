# Practice Solutions — Day 284

## Basic Solutions
1. Supervised Learning Algorithm Comparison analyzes unlabeled feature structures without target signals.
2. Inertia is the sum of squared distances of samples to their closest cluster centroid.
3. $\text{Support} = P(A \cap B)$, $\text{Confidence} = P(B|A)$, $\text{Lift} = \frac{P(A \cap B)}{P(A)P(B)}$.

## Conceptual Solutions
4. Features with larger numerical scales dominate Euclidean distance calculations and covariance variance calculations.
5. Elbow Method plots WCSS against $K$; the "elbow" point indicates the optimal balance between cluster compactness and parameter count.
6. PCA is linear and preserves global variance structure; t-SNE is non-linear and preserves local neighborhood distances (visualization only).

## Calculation Solutions
7. $\text{Lift} = \frac{0.3}{0.5 \times 0.4} = \frac{0.3}{0.2} = 1.5$.
8. Total variance $= 4.0 + 1.0 = 5.0$. Ratio for PC1 $= 4.0 / 5.0 = 0.80$ (80%). Ratio for PC2 $= 1.0 / 5.0 = 0.20$ (20%).

## Implementation Solutions
```python
import numpy as np
from sklearn.decomposition import PCA

# 9. Euclidean Distance Matrix
def pairwise_dist(X, centroids):
    return np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)

# 10. Sklearn PCA
X = np.random.randn(100, 5)
pca = PCA(n_components=2).fit(X)
print("Explained Variance Ratios:", pca.explained_variance_ratio_)
```

## ML Reasoning Solutions
11. Use DBSCAN. K-Means assumes spherical clusters and fails on non-convex concentric rings; DBSCAN groups by density continuity.
12. To prevent data leakage. Computing PCA on combined train+test leaks global variance statistics into the training phase.

## Dataset Questions
13. Cut the dendrogram at horizontal threshold level to count vertical line intersections.

## Interview Solutions
14. E-step: Assign each point $\mathbf{x}_i$ to nearest centroid $\boldsymbol{\mu}_k$. M-step: Recalculate centroids $\boldsymbol{\mu}_k$ as mean of assigned points. Repeat until convergence.
15. Maximizing variance $\mathbf{v}^T \boldsymbol{\Sigma} \mathbf{v}$ subject to $\|\mathbf{v}\| = 1$ leads to Lagrangian $\mathcal{L} = \mathbf{v}^T \boldsymbol{\Sigma} \mathbf{v} - \lambda(\mathbf{v}^T\mathbf{v} - 1)$. Setting derivative to zero yields $\boldsymbol{\Sigma}\mathbf{v} = \lambda \mathbf{v}$.
