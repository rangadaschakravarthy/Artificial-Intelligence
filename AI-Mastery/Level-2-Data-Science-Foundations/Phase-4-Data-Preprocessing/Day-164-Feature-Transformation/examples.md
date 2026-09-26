# Day 164 Worked Examples: Feature Transformation

## Example 1 — Practical: Equal-Width vs Equal-Frequency Binning
```python
import pandas as pd

df = pd.DataFrame({'Income': [20000, 25000, 30000, 45000, 80000, 150000, 250000]})

# Equal-width binning (3 intervals)
df['Income_Cut'] = pd.cut(df['Income'], bins=3)

# Equal-frequency quantile binning (3 quantiles)
df['Income_Qcut'] = pd.qcut(df['Income'], q=3)

print("Binned Income DataFrame:
", df[['Income', 'Income_Cut', 'Income_Qcut']])
```
