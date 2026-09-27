# Examples — Day 285: K-Means Clustering

## Example 1 — Extremely Simple
2D point clustering into 2 centroids.

## Example 2 — Basic Numerical Example
Computing Support, Confidence, and Lift for transaction data:
- Total transactions = 100.
- Bread = 60, Butter = 40, Both = 30.
- $\text{Support}(\text{Bread} \to \text{Butter}) = 30/100 = 0.30$.
- $\text{Confidence} = 30/60 = 0.50$.
- $\text{Lift} = \frac{0.30}{0.60 \times 0.40} = \frac{0.30}{0.24} = 1.25$.

## Example 3 — Real Dataset Example (Iris PCA)
Reducing Iris dataset from 4 dimensions to 2 principal components while retaining 95% total variance.

## Example 4 — Machine Learning Pipeline Example
`StandardScaler` + `PCA(n_components=2)` + `KMeans(n_clusters=3)`.

## Example 5 — Real-World Scenario (Customer Segmentation)
Segmenting e-commerce users based on Recency, Frequency, and Monetary (RFM) features.

## Example 6 — Interview-Style Example
Explaining why DBSCAN finds arbitrary non-spherical cluster shapes while K-Means assumes spherical clusters.
