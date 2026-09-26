# Day 131 Solutions: Pandas for Machine Learning

## Level 1 — Basic
1. $X$ is a 2D matrix (rows $	imes$ features). $y$ is a 1D vector (rows $	imes$ 1).
2. `pd.get_dummies()`.
3. It drops 1 binary category column to prevent multi-collinearity (Dummy Variable Trap).
4. `s.astype(int)`.
5. `.to_parquet()` (Parquet preserves dtypes like `int32`, `float64`, `datetime`).

## Level 2 — Coding
1.
```python
import pandas as pd
X = df.drop(columns=['Price'])
y = df['Price']
```
2.
```python
df_encoded = pd.get_dummies(df, columns=['Department'], drop_first=True, dtype=int)
```
3.
```python
y = (df['Churn'] == 'Yes').astype(int)
```
4.
```python
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)
```
5.
```python
pd.concat([X, y], axis=1).to_csv('processed_ml_data.csv', index=False)
```

## Level 3 — Data Analysis
1.
```python
y = (df['Churn'] == 'Yes').astype(int)
X_raw = df.drop(columns=['Churn'])
X = pd.get_dummies(X_raw, drop_first=True, dtype=int)
print("X shape:", X.shape, "y shape:", y.shape)
```
2.
```python
X_encoded = pd.get_dummies(X, columns=['CatCol'], dummy_na=True, dtype=int)
```
3.
```python
ordinal_map = {'Low': 0, 'Medium': 1, 'High': 2}
y = df['Risk_Tier'].map(ordinal_map)
```
4.
```python
# Scaling continuous + encoding categories
num_cols = X.select_dtypes(include='number').columns
X[num_cols] = (X[num_cols] - X[num_cols].mean()) / X[num_cols].std()
X = pd.get_dummies(X, drop_first=True, dtype=int)
```
5.
```python
assert X.select_dtypes(include='object').shape[1] == 0, "String columns remain!"
assert X.isna().sum().sum() == 0, "Missing values remain!"
```

## Level 4 — Debugging
1. Apply `pd.get_dummies()` to encode all non-numeric object columns to binary integers before passing $X$ to Scikit-Learn.
2. Re-align `X_test` columns against `X_train.columns`: `X_test = X_test.reindex(columns=X_train.columns, fill_value=0)`.
3. Set `drop_first=True` in `pd.get_dummies(..., drop_first=True)`.

## Level 5 — AI/ML Application
1.
```python
def prepare_ml_pipeline(raw_df, target_col):
    df = raw_df.copy().dropna(subset=[target_col])
    y = df[target_col]
    X_raw = df.drop(columns=[target_col])
    X = pd.get_dummies(X_raw, drop_first=True, dtype=int)
    num_cols = X.select_dtypes(include='number').columns
    X[num_cols] = X[num_cols].fillna(X[num_cols].median())
    return X, y
```
2. `pd.get_dummies()` processes in-memory DataFrames without saving state. Scikit-Learn `OneHotEncoder` fits on training data and transforms test data reproducibly in production pipelines.
3. Target encoding replaces categories with target mean values. Computing target encoding on the full dataset before splitting leaks test set label distributions into features.

## Level 6 — Interview Questions
1. If $K$ dummy columns are included, their sum equals the constant vector $\mathbf{1}$, making the feature matrix $X$ linearly dependent ($X^T X$ becomes singular/uninvertible). Setting `drop_first=True` resolves non-invertibility.
2. One-Hot Encoding creates binary indicator columns without implying order. Label Encoding maps categories to continuous integers (`0, 1, 2`), which can incorrectly imply ordinal ranking for nominal variables.
3. Use Frequency Encoding, Target Encoding, or Grouping rare categories into an `'Other'` bucket before encoding.
4. Save `X.columns.tolist()` feature name ordering explicitly before calling `X.values`.
5. Parquet utilizes columnar compression (smaller file size, faster I/O) and preserves schema data types natively without re-parsing CSV strings.
