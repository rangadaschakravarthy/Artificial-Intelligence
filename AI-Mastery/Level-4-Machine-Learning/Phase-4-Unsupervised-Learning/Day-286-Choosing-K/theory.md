# Theory — Day 286: Choosing K (Elbow Method & Silhouette Score)

### 6.1 Definition
Choosing K (Elbow Method & Silhouette Score) is an essential component of Machine Learning engineering. Selecting optimal cluster count $K$ via WCSS elbow plots, silhouette coefficient $s(i) = \frac{b(i)-a(i)}{\max(a(i), b(i))}$, and domain constraints.

### 6.2 Intuition
Think of this technique as organizing data into natural groups (Clustering), compressing complex high-dimensional information into key axes (Dimensionality Reduction), or discovering hidden shopping habits (Association Rules).

### 6.3 Why It Exists
Unlabeled datasets dominate real-world applications. Unsupervised algorithms reveal underlying dataset geometry, reduce memory storage requirements, and uncover actionable patterns without ground-truth labels.

### 6.4 Real-World Analogy
- **K-Means**: Placing 3 customer service centers to minimize total travel distance for all regional residents.
- **PCA**: Taking a 2D photograph of a 3D statue from the angle that captures the maximum variance/detail.
- **Apriori**: Discovering that customers who purchase bread and peanut butter also buy jelly 80% of the time.

### 6.5 Formal Definition
Let $\mathbf{X} \in \mathbb{R}^{n \times d}$ represent an unlabeled feature matrix.

### 6.6 Mathematical Representation
- **K-Means Inertia (WCSS)**:
  

$$
\text{Inertia} = \sum_{k=1}^K \sum_{\mathbf{x}_i \in C_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|^2
$$

- **Silhouette Coefficient**:
  

$$
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$

- **PCA Covariance Matrix & Eigen-Decomposition**:
  

$$
\boldsymbol{\Sigma} = \frac{1}{n-1} \mathbf{X}^T \mathbf{X}, \quad \boldsymbol{\Sigma} \mathbf{v}_j = \lambda_j \mathbf{v}_j
$$

- **Association Metrics**:
  

$$
\text{Support}(X \to Y) = P(X \cup Y), \quad \text{Confidence}(X \to Y) = \frac{P(X \cup Y)}{P(X)}, \quad \text{Lift}(X \to Y) = \frac{P(X \cup Y)}{P(X)P(Y)}
$$

### 6.7 Worked Example
Calculating Silhouette Score or PCA Explained Variance Ratio.

### 6.8 ML Example
Clustering customer transaction histories into 4 distinct marketing personas.

### 6.9 Python Example
Scratch NumPy implementation of K-Means or PCA.

### 6.10 scikit-learn Example
`from sklearn.cluster import KMeans, DBSCAN` / `from sklearn.decomposition import PCA`.

### 6.11 Common Mistakes
- Applying K-Means without scaling features (larger scale features dominate distance calculations).
- Using t-SNE for feature reduction in a downstream ML pipeline (t-SNE is strictly for visualization!).

### 6.12 Strengths
Operates on unlabeled data, reveals hidden structures, compresses feature dimensionality.

### 6.13 Weaknesses
Sensitivity to initial centroid placement (K-Means), linear reduction limits (PCA), hyperparameter sensitivity.

### 6.14 Real-World Applications
Customer segmentation, anomaly detection, image compression, market basket analysis.

### 6.15 Interview Insight
Be ready to derive PCA as variance maximization or explain the exact steps of the K-Means Expectation-Maximization loop.

### 6.16 Summary
Choosing K (Elbow Method & Silhouette Score) unlocks valuable structural patterns, dimensionality compression, and association rules from raw unannotated datasets.
