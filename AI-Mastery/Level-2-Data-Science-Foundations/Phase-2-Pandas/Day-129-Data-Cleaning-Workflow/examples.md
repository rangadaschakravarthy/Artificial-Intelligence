# Day 129 Worked Examples: Data Cleaning Workflow

## Example 1 — Beginner: Cleaning Dirty Column Names & String Whitespace
```python
import pandas as pd

raw = pd.DataFrame({
    ' First Name ': [' John ', ' Jane '],
    '  LAST NAME': ['Doe  ', '  Smith'],
    'Age ': [' 30 ', ' 25 ']
})

df = raw.copy()
# Standardize column headers: lowercase, strip, snake_case
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Strip whitespace from string columns
for col in ['first_name', 'last_name']:
    df[col] = df[col].str.strip()

df['age'] = df['age'].str.strip().astype(int)
print("Cleaned DataFrame:
", df)
```

## Example 2 — Practical: Parsing Dirty Currency Strings & Missing Imputation
```python
import pandas as pd
import numpy as np

dirty_data = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price_Raw': ['$1,200.50', '$25.00', 'N/A', '$300.00'],
    'Stock': [10, np.nan, 15, 20]
})

df = dirty_data.copy()
# Clean currency strings to float
df['price'] = (
    df['Price_Raw']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .replace('N/A', np.nan)
    .astype(float)
)
# Impute missing price with median and stock with 0
df['price'].fillna(df['price'].median(), inplace=True)
df['stock'] = df['Stock'].fillna(0).astype(int)

df.drop(columns=['Price_Raw', 'Stock'], inplace=True)
print("Cleaned Pricing Table:
", df)
```

## Example 3 — Intermediate: Modular Cleaning Pipeline Function
```python
import pandas as pd
import numpy as np

def clean_employee_data(raw_df):
    df = raw_df.copy()
    
    # 1. Headers
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # 2. Deduplicate
    df.drop_duplicates(inplace=True)
    
    # 3. Clean Text
    df['name'] = df['name'].str.strip().str.title()
    
    # 4. Range Validation
    df.loc[(df['age'] < 18) | (df['age'] > 100), 'age'] = np.nan
    df['age'].fillna(df['age'].median(), inplace=True)
    
    # 5. Type Casting
    df['age'] = df['age'].astype(int)
    
    return df

raw_emp = pd.DataFrame({
    ' Name ': [' alice ', ' bob ', ' alice ', ' charlie '],
    ' Age ': [25, 150, 25, -5]
})

clean_emp = clean_employee_data(raw_emp)
print("Cleaned Employee Dataset via Function:
", clean_emp)
```

## Example 4 — Real Dataset: E-Commerce Order Log Pipeline
```python
import pandas as pd
import numpy as np

raw_orders = pd.DataFrame({
    'Order_ID': [101, 102, 102, 103, 104],
    'Customer': ['Alice', 'Bob', 'Bob', 'Charlie', 'David'],
    'Amount': ['150.00', '200.50', '200.50', 'INVALID', '99.99'],
    'Order_Date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-04']
})

def pipeline(df):
    d = df.copy()
    d = d.drop_duplicates(subset=['Order_ID'])
    d['Amount'] = pd.to_numeric(d['Amount'], errors='coerce')
    d['Amount'].fillna(d['Amount'].median(), inplace=True)
    d['Order_Date'] = pd.to_datetime(d['Order_Date'])
    return d

clean_df = pipeline(raw_orders)
print("Cleaned E-Commerce Order Log:
", clean_df)
```

## Example 5 — AI/ML Application: Pre-ML Data Cleaning & Validation Assertions
```python
import pandas as pd
import numpy as np

def prep_ml_dataset(df):
    clean = df.copy()
    # Remove null targets
    clean = clean.dropna(subset=['Target'])
    # Impute numeric features
    num_cols = clean.select_dtypes(include=[np.number]).columns
    clean[num_cols] = clean[num_cols].fillna(clean[num_cols].median())
    
    # Validation Assertions
    assert clean.isna().sum().sum() == 0, "Error: Null values remain!"
    assert clean.duplicated().sum() == 0, "Error: Duplicate rows remain!"
    
    return clean

raw_ml = pd.DataFrame({
    'Feature_1': [1.0, np.nan, 3.0, 4.0],
    'Target': [0, 1, 0, np.nan]
})

processed = prep_ml_dataset(raw_ml)
print("Validated ML-Ready Dataset:
", processed)
```
