# Day 168 Solutions: Data Leakage

## Level 1 — Basic
1. The introduction of test set, future, or target label information into the feature training pipeline.
2. Fit transformers ONLY on training data. Use learned parameters to transform training and test data.
3. Fitting scalers on the full dataset computes global mean $\mu$ and std $\sigma$ using test set samples, contaminating training feature distributions with test set statistics.

## Level 2 — Coding
1.
```python
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_tr_scaled = scaler.fit_transform(X_tr)
X_te_scaled = scaler.transform(X_te)
```

## Level 3 — Data Analysis
1. Target Leakage happens when a feature contains data calculated after the target event occurs (e.g. including `Days_In_ICU` as a feature to predict hospital admission). In production, this feature is unavailable at prediction time, causing model failure.
