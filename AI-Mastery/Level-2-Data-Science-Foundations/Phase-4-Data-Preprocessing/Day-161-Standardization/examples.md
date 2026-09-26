# Day 161 Worked Examples: Standardization

## Example 1 — Practical: StandardScaler Implementation & Verification
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({'Salary': [45000, 60000, 80000, 110000, 150000]})

scaler = StandardScaler()
df['Salary_Standardized'] = scaler.fit_transform(df[['Salary']])

print("Standardized DataFrame:
", df)
print(f"Mean: {df['Salary_Standardized'].mean():.4f} (Expected 0.0)")
print(f"Std:  {df['Salary_Standardized'].std(ddof=0):.4f} (Expected 1.0)")
```
