# Code — Day 286: Choosing K (Elbow Method & Silhouette Score)
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA

def demonstrate_unsupervised():
    print("--- Day 286: Choosing K (Elbow Method & Silhouette Score) Demo ---")
    
    # 1. Generate Synthetic Data
    X, _ = make_blobs(n_samples=150, n_features=4, centers=3, random_state=42)
    
    # 2. Fit K-Means & PCA
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
    pca = PCA(n_components=2).fit(X)
    X_pca = pca.transform(X)
    
    print("K-Means Inertia:", round(kmeans.inertia_, 2))
    print("PCA Explained Variance Ratios:", np.round(pca.explained_variance_ratio_, 3))
    print("Transformed PCA Shape:", X_pca.shape)

if __name__ == "__main__":
    demonstrate_unsupervised()
