# Day 170 Worked Examples: Preprocessing Pipelines

## Example 1 — Practical: Full ColumnTransformer Preprocessing Pipeline
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.DataFrame({
    'Age': [25, 30, np.nan, 45, 50],
    'Income': [50000, 60000, 80000, np.nan, 120000],
    'City': ['NY', 'SF', 'NY', 'LA', np.nan],
    'Target': [0, 1, 0, 1, 0]
})

X = df.drop(columns=['Target'])
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

num_cols = ['Age', 'Income']
cat_cols = ['City']

preprocessor = ColumnTransformer(transformers=[
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('scale', StandardScaler())]), num_cols),
    ('cat', Pipeline([('imp', SimpleImputer(strategy='most_frequent')), ('ohe', OneHotEncoder(drop='first', sparse_output=False))]), cat_cols)
])

X_tr_proc = preprocessor.fit_transform(X_train)
X_te_proc = preprocessor.transform(X_test)

print("Preprocessed Train Array Shape:", X_tr_proc.shape)
```
