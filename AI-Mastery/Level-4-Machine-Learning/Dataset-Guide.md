# Dataset Guide for Machine Learning Engineering

## Educational & Benchmark Datasets

| Dataset | Type | Task | Sample Count ($n$) | Feature Count ($d$) | Primary Challenge |
| ------- | ---- | ---- | ------------------ | ------------------ | ----------------- |
| **Housing Prices** | Tabular | Regression | 506 / 20,640 | 13 / 8 | Multicollinearity, non-linear relationships |
| **Iris Species** | Tabular | Classification | 150 | 4 | Multiclass separation benchmark |
| **Customer Churn** | Tabular | Classification | 7,043 | 20 | Class imbalance, mixed numerical/categorical |
| **Mall Customers** | Tabular | Clustering | 200 | 4 | Optimal cluster selection ($K$), visualization |
| **Market Basket** | Transaction | Association | 15,000 | Variable | Sparse transaction matrix, candidate itemset mining |
| **GridWorld** | Synthetic | Reinforcement | Discrete $N \times M$ | State coordinates | Temporal difference learning, policy iteration |

## Synthetic Dataset Generation in scikit-learn
```python
from sklearn.datasets import make_regression, make_classification, make_blobs

# 1. Regression
X_reg, y_reg = make_regression(n_samples=500, n_features=10, noise=1.5, random_state=42)

# 2. Classification
X_cls, y_cls = make_classification(n_samples=500, n_features=5, n_classes=2, random_state=42)

# 3. Clustering
X_cls, _ = make_blobs(n_samples=300, n_features=2, centers=4, cluster_std=1.0, random_state=42)
```
