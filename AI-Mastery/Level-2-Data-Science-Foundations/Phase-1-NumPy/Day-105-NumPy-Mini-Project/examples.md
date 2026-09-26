# Day 105 Worked Examples: Mini-Project Step Breakdown

## Task 1 Breakdown: NaN Imputation
```python
import numpy as np

# Feature column with NaNs
col = np.array([10.0, 20.0, np.nan, 40.0, np.nan])

# Compute median ignoring NaNs
med = np.nanmedian(col)

# Replace NaNs with median
col[np.isnan(col)] = med
print("Imputed Column:", col) # [10. 20. 20. 40. 20.]
```

## Task 2 Breakdown: Feature Standardization via Broadcasting
```python
import numpy as np

X = np.array([[100.0, 1.0], [200.0, 2.0], [300.0, 3.0]])

means = X.mean(axis=0)
stds = X.std(axis=0)

X_std = (X - means) / stds
print("Standardized Feature Matrix (Mean=0, Std=1):
", np.round(X_std, 2))
```
