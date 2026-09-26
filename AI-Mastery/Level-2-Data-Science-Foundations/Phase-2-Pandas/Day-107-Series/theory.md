# Day 107 Theory: Series

### 1. What Is It?
A Pandas `Series` is a 1D labeled array capable of holding any data type (integers, floats, strings, objects). It consists of data values backed by a NumPy 1D array paired with an `Index` array of labels.

### 2. Why Does It Exist?
Pure 1D NumPy arrays rely solely on 0-based integer positions (`0, 1, 2`). A Series allows elements to be indexed by custom meaningful labels (e.g. `'2026-01-01'`, `'AAPL'`, `'User_101'`).

### 3. Intuition
Think of a Series as a single column in an Excel sheet where every row has a specific custom row label on the far left.

### 4. Syntax
```python
import pandas as pd

# Series with default range index (0, 1, 2)
s1 = pd.Series([10, 20, 30])

# Series with custom string index
s2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'], name='Sales')
```

### 5. Parameters
- `data`: Array-like, Iterable, Dict, or Scalar value.
- `index`: Array-like of custom row labels.
- `name`: String name assigned to the Series.

### 6. How It Works
When operating on two Series (e.g. `s1 + s2`), Pandas performs automatic **label alignment**. It matches items sharing identical index labels. Non-matching index labels produce `NaN`.

### 7. Simple Example
```python
import pandas as pd
s = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
print("Label 'y':", s['y']) # 20
```

### 8. Intermediate Example
```python
import pandas as pd
s1 = pd.Series([10, 20], index=['a', 'b'])
s2 = pd.Series([30, 40], index=['b', 'c'])
print(s1 + s2) # 'a': NaN, 'b': 50.0, 'c': NaN
```

### 9. Output Interpretation
`s1 + s2` aligns label `'b'` ($20 + 30 = 50.0$). Labels `'a'` and `'c'` do not exist in both Series, producing `NaN`.

### 10. Common Mistakes
- Confusing positional indexing `s.iloc[0]` with label indexing `s.loc['a']`.
- Expecting integer-indexed Series `index=[1, 2, 3]` to behave identically to default 0-based positional indices.

### 11. Data Science Connection
Series methods (`value_counts()`, `describe()`, `isna()`) provide instant single-feature profiling during Exploratory Data Analysis.

### 12. AI/ML Connection
Target label vectors $y$ are passed to ML models as 1D Series. Categorical target distribution balance is checked via `y.value_counts(normalize=True)`.

### 13. Interview Insight
Question: "What happens during arithmetic operations between two Pandas Series with different index orders?"
Answer: Pandas aligns the Series by index **label**, not by positional order. It matches values corresponding to identical labels, performing the operation seamlessly regardless of order, and inserts `NaN` for non-overlapping labels.

### 14. Summary
A `Series` is a 1D array with custom index labels. Operations align data automatically by label.
