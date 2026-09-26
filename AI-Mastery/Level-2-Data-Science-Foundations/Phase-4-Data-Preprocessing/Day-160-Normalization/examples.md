# Day 160 Worked Examples: Normalization

## Example 1 — Practical: Custom Min-Max Scaler vs MinMaxScaler
```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Custom Implementation
def min_max_scale(series, feature_range=(0, 1)):
    a, b = feature_range
    x_min, x_max = series.min(), series.max()
    return a + ((series - x_min) * (b - a)) / (x_max - x_min)

df = pd.DataFrame({'Income': [30000, 50000, 80000, 120000]})

# Custom
df['Income_Custom'] = min_max_scale(df['Income'])

# Scikit-Learn
scaler = MinMaxScaler()
df['Income_Sklearn'] = scaler.fit_transform(df[['Income']])

print("Normalized Dataset Comparison:
", df)
```
