# Day 114 Theory: Sorting Data

### 1. What Is It?
Sorting rearranges the row order of a DataFrame or Series based on numerical, string, or datetime values in specified columns or index labels.

### 2. Why Does It Exist?
Unordered datasets make identifying top/bottom performers, ranking items, and reading sequential time-series patterns difficult.

### 3. Intuition
Sorting is like arranging a deck of numbered cards in numerical order from smallest to largest or alphabetizing a list of student names.

### 4. Syntax
```python
import pandas as pd

df = pd.DataFrame({'Age': [30, 20], 'Score': [90, 80]})

# Sort by single column ascending
df_sorted1 = df.sort_values(by='Age')

# Sort by multiple columns with mixed directions
df_sorted2 = df.sort_values(by=['Age', 'Score'], ascending=[True, False])

# Sort by row Index labels
df_sorted_idx = df.sort_index(ascending=True)
```

### 5. Parameters
- `by`: Column name or list of column names to sort by.
- `ascending`: Boolean or list of booleans specifying direction for each column (`True` for A-Z / 0-9, `False` for Z-A / 9-0).
- `na_position`: `'last'` (default) or `'first'` specifying where `NaN` values are placed.
- `kind`: Algorithm selection (`'quicksort'`, `'mergesort'`, `'heapsort'`).

### 6. How It Works
Pandas computes an `argsort` index permutation array on the target column, then re-indexes the DataFrame rows using fast C block reordering.

### 7. Simple Example
```python
import pandas as pd
s = pd.Series([30, 10, 20])
print(s.sort_values()) # 10, 20, 30
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'Dept': ['IT', 'HR', 'IT'], 'Salary': [90k, 60k, 110k]})
print(df.sort_values(by=['Dept', 'Salary'], ascending=[True, False]))
```

### 9. Output Interpretation
Sorts primarily by `'Dept'` alphabetically (HR first, IT second). Within `'IT'`, sorts by `'Salary'` descending (110k then 90k).

### 10. Common Mistakes
- Forgetting that `sort_values()` returns a new DataFrame copy (Must assign `df = df.sort_values(...)` or use `inplace=True`).
- Forgetting to reset index after sorting, leaving scrambled index labels (e.g. 3, 0, 2, 1).

### 11. Data Science Connection
Extracting Top-N and Bottom-N records and preparing clean sorted charts for visualization.

### 12. AI/ML Connection
Sorting timestamp columns prior to creating time-series rolling features to prevent temporal data leakage.

### 13. Interview Insight
Question: "What is the difference between `sort_values()` and `nlargest()` in Pandas?"
Answer: `sort_values()` sorts the entire DataFrame ($O(N \log N)$ complexity). `nlargest(k, 'col')` uses a min-heap under the hood ($O(N \log k)$ complexity), making it significantly faster for extracting top $k$ items when $k \ll N$.

### 14. Summary
Sort DataFrames using `sort_values(by=..., ascending=...)` and index using `sort_index()`. Always reset index if consecutive order is required.
