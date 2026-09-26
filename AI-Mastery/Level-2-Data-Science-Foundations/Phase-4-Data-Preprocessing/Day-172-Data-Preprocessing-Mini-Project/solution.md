# Day 172 Solutions: Data Preprocessing Mini Project

## Level 1 — Basic
1. Train/Test Splitting (`train_test_split()`).
2. `X_train_processed`, `X_test_processed`, `y_train`, `y_test`.

## Level 2 — Coding
1.
```python
assert np.isnan(X_train_proc).sum() == 0, "Nulls remain in X_train!"
assert X_train_proc.shape[0] == y_train.shape[0], "Row count mismatch!"
```

## Level 3 — Data Analysis
1. Level 2 transforms raw messy business data through NumPy numerical computing, Pandas data manipulation, Matplotlib/Seaborn visualization, and Scikit-Learn preprocessing into clean, standardized mathematical matrices ($X, y$), which form the required input vectors for training Level 3 Machine Learning algorithms (Linear Models, Decision Trees, Random Forests, Neural Networks).
