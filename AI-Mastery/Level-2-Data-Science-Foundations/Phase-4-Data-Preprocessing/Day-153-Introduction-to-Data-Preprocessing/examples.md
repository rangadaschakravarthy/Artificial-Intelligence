# Day 153 Worked Examples: Introduction to Data Preprocessing

## Example 1 — Practical: Simple Manual Preprocessing Pipeline
```python
import pandas as pd
import numpy as np

# Raw Data
df = pd.DataFrame({
    'Age': [25, 30, 45, 35],
    'Salary': [50000, 60000, 90000, 75000],
    'City': ['NY', 'SF', 'NY', 'SF']
})

# 1. Separate Features
X = df.copy()

# 2. One-Hot Encode Categorical Column
X_encoded = pd.get_dummies(X, columns=['City'], drop_first=True, dtype=float)

# 3. Standardization Scaling: (x - mean) / std
num_cols = ['Age', 'Salary']
X_encoded[num_cols] = (X_encoded[num_cols] - X_encoded[num_cols].mean()) / X_encoded[num_cols].std()

print("Preprocessed Numerical Matrix X:
", X_encoded)
```
