# Practice Questions — Day 292

## Basic Questions
1. Define Dimensionality Reduction Comparison.
2. What is Inertia in K-Means clustering?
3. Define Support, Confidence, and Lift.

## Conceptual Questions
4. Why is feature scaling mandatory before running K-Means or PCA?
5. Explain the Elbow Method for selecting $K$.
6. Contrast PCA vs t-SNE for dimensionality reduction.

## Calculation Questions
7. Calculate Lift for $P(A) = 0.5, P(B) = 0.4, P(A \cap B) = 0.3$.
8. Compute explained variance ratio for eigenvalues $\lambda_1 = 4.0, \lambda_2 = 1.0$.

## Implementation Questions
9. Write a NumPy function computing pairwise Euclidean distances between points and centroids.
10. Implement `sklearn.decomposition.PCA` to reduce a dataset to 2 components.

## ML Reasoning Questions
11. You have a dataset with concentric circular clusters. Should you use K-Means or DBSCAN? Explain.
12. Why should you fit `PCA` only on the training set and transform the test set?

## Dataset Questions
13. Analyze cluster counts from a dendrogram diagram.

## Interview Questions
14. Explain the Expectation-Maximization steps in K-Means.
15. Derive why the principal component direction $\mathbf{v}_1$ is the eigenvector of the sample covariance matrix $\boldsymbol{\Sigma}$ corresponding to the largest eigenvalue $\lambda_1$.
