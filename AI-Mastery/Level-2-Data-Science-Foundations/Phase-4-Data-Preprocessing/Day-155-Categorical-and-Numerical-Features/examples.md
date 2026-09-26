# Day 155 Worked Examples: Categorical and Numerical Features

## Example 1 — Practical: Automated Feature Type Splitter
```python
import pandas as pd

def audit_and_split_features(df, cat_threshold=10):
    num_cols = []
    low_card_cats = []
    high_card_cats = []
    
    for col in df.columns:
        if df[col].dtype in ['object', 'category']:
            if df[col].nunique() <= cat_threshold:
                low_card_cats.append(col)
            else:
                high_card_cats.append(col)
        else:
            num_cols.append(col)
            
    return num_cols, low_card_cats, high_card_cats

df = pd.DataFrame({
    'Age': [25, 30, 35],
    'Score': [88.5, 92.0, 79.5],
    'Tier': ['Low', 'High', 'Low'],
    'UserID': ['U101', 'U102', 'U103']
})

nums, low_cats, high_cats = audit_and_split_features(df, cat_threshold=2)
print("Numeric Columns:           ", nums)
print("Low-Cardinality Categories: ", low_cats)
print("High-Cardinality Categories:", high_cats)
```
