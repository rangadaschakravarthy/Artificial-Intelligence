# Day 165 Worked Examples: Log and Power Transformations

## Example 1 — Practical: Skewness Reduction via np.log1p
```python
import numpy as np
import pandas as pd

np.random.seed(42)
# Heavily right-skewed exponential distribution
income = np.random.exponential(scale=50000, size=500)

df = pd.DataFrame({'Income': income})
df['Income_Log'] = np.log1p(df['Income'])

print(f"Raw Income Skewness:   {df['Income'].skew():.3f}")
print(f"Log1p Income Skewness: {df['Income_Log'].skew():.3f}")
```
