# Day 122 Theory: Apply and Map

### 1. What Is It?
`.map()`, `.apply()`, and `.transform()` are element-wise or group-wise functional programming methods used to apply custom logic across Pandas structures.

### 2. Why Does It Exist?
While vectorized built-ins cover standard math, complex custom logic (conditional thresholds, multi-column formulas) requires executing user-defined functions across data.

### 3. Intuition
- **`.map()`**: A translation dictionary (e.g., replace `'M'` with `'Male'`).
- **`.apply()`**: A worker processing each row or column through a custom machine.
- **`.transform()`**: A group calculator that returns a vector matching the original table's exact shape.

### 4. Syntax
```python
# Series Map (dict lookup or func):
s.map({'Low': 1, 'Medium': 2, 'High': 3})

# DataFrame Row-wise Apply:
df.apply(lambda row: row['A'] + row['B'], axis=1)

# GroupBy Transform:
df.groupby('Dept')['Salary'].transform('mean')
```

### 5. Parameters
- `arg` (in `.map()`): Dict, Series, or function.
- `func` (in `.apply()`): Function to apply.
- `axis` (in `DataFrame.apply()`): `0` or `'index'` (apply to each column), `1` or `'columns'` (apply to each row).

### 6. How It Works
- `.map()` matches Series elements against dictionary keys or passes them to a 1D function.
- `.apply(axis=1)` passes each row as a Pandas Series to the target function.
- `GroupBy.transform()` calculates group aggregations and broadcasts the results back to original row positions.

### 7. Simple Example
```python
import pandas as pd
s = pd.Series(['a', 'b', 'c'])
print(s.map({'a': 1, 'b': 2, 'c': 3}))
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'Weight': [70, 80], 'Height': [1.75, 1.80]})
df['BMI'] = df.apply(lambda r: r['Weight'] / (r['Height'] ** 2), axis=1)
print(df)
```

### 9. Output Interpretation
`.map()` returns a Series. `DataFrame.apply()` returns a Series (if reducing) or DataFrame. `GroupBy.transform()` always returns an object matching the original input shape.

### 10. Common Mistakes
- Using `df.apply()` for basic arithmetic (e.g. `df['A'] + df['B']`), which is 100x slower than native vectorization.
- Forgetting `axis=1` when applying functions that access multiple row columns.

### 11. Data Science Connection
Feature engineering, string mapping, custom scoring models, and group-wise standardization.

### 12. AI/ML Connection
Preprocessing categorical target labels and computing group-based normalized features (e.g. z-score per category).

### 13. Interview Insight
Question: "Difference between `GroupBy.agg()` and `GroupBy.transform()`?"
Answer: `.agg()` reduces each group to a single row output. `.transform()` returns a vector of the original dataset length, placing group values at corresponding row indices.

### 14. Summary
`.map()` handles dictionary lookup transformations, `.apply()` handles custom function mapping across rows/columns, and `.transform()` performs shape-preserving group broadcasting.
