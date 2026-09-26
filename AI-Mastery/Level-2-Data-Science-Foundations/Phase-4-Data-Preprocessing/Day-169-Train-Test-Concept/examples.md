# Day 169 Worked Examples: Train-Test Concept

## Example 1 — Practical: Stratified Train-Test Split Verification
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Imbalanced Target (90% Class 0, 10% Class 1)
np.random.seed(42)
X = pd.DataFrame({'F1': np.random.randn(100)})
y = pd.Series([0]*90 + [1]*10)

# Stratified Split
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("Full Target Class Proportions:
", y.value_counts(normalize=True).to_dict())
print("Train Target Class Proportions:
", y_tr.value_counts(normalize=True).to_dict())
print("Test Target Class Proportions: 
", y_te.value_counts(normalize=True).to_dict())
```
