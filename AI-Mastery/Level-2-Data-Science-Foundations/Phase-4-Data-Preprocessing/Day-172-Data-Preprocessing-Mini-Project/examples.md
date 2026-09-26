# Day 172 Worked Examples: Data Preprocessing Mini Project

## Complete Workflow Code Structure Overview
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# 1. Ingest
raw_df = pd.DataFrame({...})

# 2. Separate X and y
y = raw_df['Target']
X = raw_df.drop(columns=['Target'])

# 3. Split FIRST
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# 4. Pipeline Transformer
preprocessor = ColumnTransformer(transformers=[
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('scale', StandardScaler())]), ['Age', 'Income']),
    ('cat', OneHotEncoder(drop='first', sparse_output=False), ['City'])
])

X_tr_proc = preprocessor.fit_transform(X_tr)
X_te_proc = preprocessor.transform(X_te)

# 5. Assertions
assert np.isnan(X_tr_proc).sum() == 0
print("Level 2 Complete! ML Ready Data Prepared.")
```
