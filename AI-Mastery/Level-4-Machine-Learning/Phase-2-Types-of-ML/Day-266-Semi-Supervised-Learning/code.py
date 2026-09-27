# Code — Day 266: Semi-Supervised Learning
import numpy as np
from sklearn.datasets import make_classification, make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

def demonstrate_paradigm():
    print("--- Day 266: Semi-Supervised Learning Paradigm Demo ---")
    
    # 1. Supervised Data Setup
    X_sup, y_sup = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
    clf = LogisticRegression().fit(X_sup, y_sup)
    print("Supervised Model Accuracy:", np.round(clf.score(X_sup, y_sup), 3))
    
    # 2. Unsupervised Clustering Setup
    X_unsup, _ = make_blobs(n_samples=100, centers=3, random_state=42)
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X_unsup)
    print("Unsupervised Cluster Centers:\n", np.round(kmeans.cluster_centers_, 2))

if __name__ == "__main__":
    demonstrate_paradigm()
