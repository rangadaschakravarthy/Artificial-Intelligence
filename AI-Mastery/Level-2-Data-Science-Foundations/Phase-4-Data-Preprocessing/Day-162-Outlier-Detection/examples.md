# Day 162 Worked Examples: Outlier Detection

## Example 1 — Practical: Outlier Detection via IQR Function
```python
import numpy as np
import pandas as pd

def detect_outliers_iqr(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    return outliers, lower_bound, upper_bound

df = pd.DataFrame({'Val': [10, 12, 11, 13, 12, 14, 100, 11]}) # 100 is outlier
outliers, lb, ub = detect_outliers_iqr(df, 'Val')

print(f"Bounds: [{lb}, {ub}]")
print("Detected Outliers:
", outliers)
```
