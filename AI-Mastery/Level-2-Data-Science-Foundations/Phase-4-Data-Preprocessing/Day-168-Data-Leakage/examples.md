# Day 168 Worked Examples: Data Leakage

## Example 1 — Practical: Demonstrating Correct vs Leaky Preprocessing
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Dataset
np.random.seed(42)
X = pd.DataFrame({'Feature': np.random.normal(50, 15, 100)})
y = np.random.choice([0, 1], 100)

# ---------------------------------------------------------
# WRONG WAY (Data Leakage!)
# ---------------------------------------------------------
scaler_wrong = StandardScaler()
X_scaled_wrong = scaler_wrong.fit_transform(X) # FITTED ON FULL DATASET!
X_tr_w, X_te_w, y_tr_w, y_te_w = train_test_split(X_scaled_wrong, y, test_size=0.2)

# ---------------------------------------------------------
# RIGHT WAY (Leak-Free!)
# ---------------------------------------------------------
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
scaler_right = StandardScaler()
X_tr_scaled = scaler_right.fit_transform(X_tr) # FIT ON TRAIN ONLY!
X_te_scaled = scaler_right.transform(X_te)    # TRANSFORM TEST USING TRAIN METRICS!

print("Correct Scaler Mean (from Train):", scaler_right.mean_[0])
```
