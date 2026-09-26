# Day 118 Theory: Data Type Conversion

### 1. What Is It?
Data type conversion is the process of casting DataFrame columns from one data type representation (`object`, `float64`, `int64`) to another (`int32`, `float32`, `datetime64`, `category`).

### 2. Why Does It Exist?
CSV parsers often misinterpret clean numbers as strings (`object`) when corrupt text entries exist. Machine learning algorithms require clean numeric or categorical code types.

### 3. Intuition
Type conversion is like converting handwritten notes into standardized computer text. "100" as a string image cannot be multiplied; converting it to integer `100` unlocks math calculations.

### 4. Syntax
```python
import pandas as pd

df = pd.DataFrame({
    'Age': ['25', '30', 'INVALID'],
    'Date': ['2026-01-01', '2026-01-02', '2026-01-03'],
    'State': ['NY', 'CA', 'NY']
})

# Robust numeric conversion (coerce turns 'INVALID' to NaN)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Datetime conversion
df['Date'] = pd.to_datetime(df['Date'])

# Categorical conversion
df['State'] = df['State'].astype('category')
```

### 5. Parameters
- `errors`: `'raise'` (default), `'ignore'`, or `'coerce'` (converts unparseable invalid entries into `NaN`).
- `downcast`: `'integer'`, `'float'` in `pd.to_numeric` to automatically pick smallest byte size.

### 6. How It Works
- `pd.to_numeric` calls C-level string parsers.
- `astype('category')` replaces repetitive string memory heaps with an integer code array mapped to a single categories lookup array.

### 7. Simple Example
```python
import pandas as pd
s = pd.Series(['1.5', '2.5'])
print(s.astype(float).sum()) # 4.0
```

### 8. Intermediate Example
```python
import pandas as pd
s_obj = pd.Series(['Apple', 'Banana', 'Apple'] * 1000) # Object strings
s_cat = s_obj.astype('category')                      # Categorical
print("Object Memory:     ", s_obj.memory_usage(deep=True), "bytes")
print("Categorical Memory:", s_cat.memory_usage(deep=True), "bytes")
```

### 9. Output Interpretation
Categorical encoding reduces memory footprint drastically (e.g. from 60KB down to 3KB).

### 10. Common Mistakes
- Calling `.astype(int)` directly on a column containing `NaN` values (Standard `int64` cannot hold `NaN`; use `pd.to_numeric` or nullable `Int64`!).
- Calling `.astype(float)` on dirty columns containing text strings (Raises `ValueError`; use `errors='coerce'`).

### 11. Data Science Connection
Pipeline preprocessing: converting dates, cleaning numbers, and optimizing memory prior to EDA.

### 12. AI/ML Connection
Converting target labels and categorical features into numerical/category codes before training algorithms.

### 13. Interview Insight
Question: "How does converting string columns to the `category` data type optimize memory?"
Answer: String object columns store 64-bit pointers to individual Python string objects scattered in memory. `category` dtype creates a single array of unique strings and represents column rows as compact 8-bit integer codes pointing to the category dictionary.

### 14. Summary
Convert dtypes using `.astype()`, `pd.to_numeric(errors='coerce')`, and `pd.to_datetime()`. Use `category` for low-cardinality string columns.
