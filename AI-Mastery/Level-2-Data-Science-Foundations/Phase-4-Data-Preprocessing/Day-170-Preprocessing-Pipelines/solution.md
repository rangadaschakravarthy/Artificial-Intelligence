# Day 170 Solutions: Preprocessing Pipelines

## Level 1 — Basic
1. `ColumnTransformer`.
2. `fit_transform()`.
3. `transform()` (never `fit_transform` on test data!).

## Level 2 — Coding
1.
```python
num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])
```

## Level 3 — Data Analysis
1. `ColumnTransformer` encapsulates all fitting calls inside `preprocessor.fit(X_train)`. Calling `preprocessor.transform(X_test)` reuses stored parameters from training data, making manual test set contamination impossible.
