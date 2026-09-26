# Day 170 Theory: Preprocessing Pipelines

### 1. What Is It?
A Preprocessing Pipeline combines multiple data transformation steps into a single scikit-learn estimator object, guaranteeing leak-free training and production deployment.

### 2. Architecture
```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(drop='first', sparse_output=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)
])

# Fit ONLY on train:
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)
```

### 3. Summary
`ColumnTransformer` applies separate preprocessing pipelines to numerical and categorical features safely without data leakage.
