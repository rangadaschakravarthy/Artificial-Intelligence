# Day 166 Worked Examples: Feature Selection

## Example 1 — Practical: Dropping Constant Features via VarianceThreshold
```python
import pandas as pd
from sklearn.feature_selection import VarianceThreshold

df = pd.DataFrame({
    'Constant_Col': [1, 1, 1, 1, 1], # 0 Variance
    'Quasi_Constant': [0, 0, 0, 0, 1], # Low Variance
    'Feature_A': [10, 20, 15, 25, 30] # High Variance
})

selector = VarianceThreshold(threshold=0.1)
selector.fit(df)

kept_cols = df.columns[selector.get_support()]
print("Features Retained Post VarianceThreshold:", list(kept_cols))
```
