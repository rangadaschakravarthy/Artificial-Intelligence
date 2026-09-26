# Day 125 Worked Examples: Concatenation

## Example 1 — Beginner: Vertical Concatenation with ignore_index
```python
import pandas as pd

batch1 = pd.DataFrame({'User': ['Alice', 'Bob'], 'Score': [85, 90]})
batch2 = pd.DataFrame({'User': ['Charlie', 'David'], 'Score': [78, 92]})

stacked_df = pd.concat([batch1, batch2], axis=0, ignore_index=True)
print("Vertically Stacked DataFrame:
", stacked_df)
```

## Example 2 — Practical: Handling Column Mismatches (join='outer' vs 'inner')
```python
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})
df2 = pd.DataFrame({'B': [30, 40], 'C': [100, 200]})

outer_concat = pd.concat([df1, df2], join='outer', ignore_index=True)
inner_concat = pd.concat([df1, df2], join='inner', ignore_index=True)

print("Outer Join Concat (Preserves all columns):
", outer_concat)
print("
Inner Join Concat (Shared columns only):
", inner_concat)
```

## Example 3 — Intermediate: Horizontal Concatenation (axis=1)
```python
import pandas as pd

demographics = pd.DataFrame({'Age': [25, 40], 'Gender': ['F', 'M']}, index=[101, 102])
financials = pd.DataFrame({'Income': [60000, 95000]}, index=[101, 102])

wide_df = pd.concat([demographics, financials], axis=1)
print("Horizontal Concatenation:
", wide_df)
```

## Example 4 — Real Dataset: Batch File Loading Pipeline Pattern
```python
import pandas as pd

# Simulating reading monthly files
months = ['Jan', 'Feb', 'Mar']
data_list = []

for m in months:
    # Simulated DF for month
    temp_df = pd.DataFrame({'Month': [m, m], 'Sales': [1000, 1500]})
    data_list.append(temp_df)

# Single concatenation step
yearly_sales = pd.concat(data_list, ignore_index=True)
print("Combined Yearly Sales Data:
", yearly_sales)
```

## Example 5 — AI/ML Application: Label-Feature Horizontal Stitching
```python
import pandas as pd
import numpy as np

# Engineered Feature Matrix X (2D)
X_features = pd.DataFrame({'F1': [0.1, 0.4, 0.8], 'F2': [1.2, 0.9, 0.3]})
# Target Vector y (Series)
y_target = pd.Series([0, 1, 0], name='Target')

# Combine X and y into single dataset for exploratory analysis
full_ml_df = pd.concat([X_features, y_target], axis=1)
print("Combined ML Feature & Target Table:
", full_ml_df)
```
