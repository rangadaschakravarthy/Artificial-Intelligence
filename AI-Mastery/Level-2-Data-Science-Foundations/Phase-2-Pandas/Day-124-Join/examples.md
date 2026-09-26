# Day 124 Worked Examples: Join

## Example 1 — Beginner: Basic Index Join
```python
import pandas as pd

df_left = pd.DataFrame({'A': ['A0', 'A1', 'A2']}, index=['K0', 'K1', 'K2'])
df_right = pd.DataFrame({'B': ['B0', 'B1', 'B3']}, index=['K0', 'K1', 'K3'])

# Default Left Join on Index
result = df_left.join(df_right)
print("Default Left Index Join:
", result)
```

## Example 2 — Practical: Inner Join with Column Suffixes
```python
import pandas as pd

df1 = pd.DataFrame({'Score': [85, 90]}, index=['Alice', 'Bob'])
df2 = pd.DataFrame({'Score': [88, 92]}, index=['Alice', 'Bob'])

# Provide suffixes for overlapping column names
joined_df = df1.join(df2, lsuffix='_T1', rsuffix='_T2', how='inner')
print("Joined Scores with Suffixes:
", joined_df)
```

## Example 3 — Intermediate: Column-to-Index Join using 'on'
```python
import pandas as pd

orders = pd.DataFrame({
    'OrderID': [101, 102, 103],
    'Cust_Key': ['C1', 'C2', 'C1'],
    'Amount': [250, 180, 300]
})

customers = pd.DataFrame({
    'Name': ['Acme', 'Beta'],
    'Tier': ['Gold', 'Silver']
}, index=['C1', 'C2'])

# Match orders['Cust_Key'] against customers index
merged_idx = orders.join(customers, on='Cust_Key')
print("Column-to-Index Join:
", merged_idx)
```

## Example 4 — Real Dataset: Financial Stock Price Time Series Join
```python
import pandas as pd

dates = pd.date_range('2023-01-01', periods=3)

aapl = pd.DataFrame({'AAPL': [150.0, 152.5, 151.0]}, index=dates)
goog = pd.DataFrame({'GOOG': [2800.0, 2820.0, 2815.0]}, index=dates)
msft = pd.DataFrame({'MSFT': [240.0, 242.0, 241.5]}, index=dates)

# Combine 3 stock price DataFrames in one call
portfolio = aapl.join([goog, msft])
print("Multi-Stock Portfolio Time Series:
", portfolio)
```

## Example 5 — AI/ML Application: Parallel Feature Table Alignment
```python
import pandas as pd

# Feature extraction pipelines running on index=Sample_ID
text_features = pd.DataFrame({'TFIDF_1': [0.5, 0.2], 'TFIDF_2': [0.1, 0.8]}, index=[101, 102])
num_features = pd.DataFrame({'Age': [25, 40], 'Income': [50000, 90000]}, index=[101, 102])
image_features = pd.DataFrame({'Emb_1': [0.9, 0.3]}, index=[101, 102])

# Join feature spaces into single ML feature matrix
X_matrix = num_features.join([text_features, image_features])
print("Combined Multimodal Feature Matrix:
", X_matrix)
```
