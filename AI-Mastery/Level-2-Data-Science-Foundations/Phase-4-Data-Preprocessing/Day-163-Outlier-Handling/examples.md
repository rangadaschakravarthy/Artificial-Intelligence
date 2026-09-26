# Day 163 Worked Examples: Outlier Handling

## Example 1 — Practical: Percentile Capping with clip()
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'Income': [20000, 35000, 45000, 50000, 60000, 1000000]}) # 1,000,000 is outlier

p05 = df['Income'].quantile(0.05)
p95 = df['Income'].quantile(0.95)

# Cap at 5th and 95th percentiles
df['Income_Capped'] = df['Income'].clip(lower=p05, upper=p95)

print("Percentile Capped Dataset:
", df)
```
