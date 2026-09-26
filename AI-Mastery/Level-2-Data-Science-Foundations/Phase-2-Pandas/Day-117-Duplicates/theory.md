# Day 117 Theory: Duplicates

### 1. What Is It?
Duplicates are identical rows or repeated key records in a DataFrame. `duplicated()` identifies duplicate rows, while `drop_duplicates()` removes them.

### 2. Why Does It Exist?
Data pipelines receive repeated API payloads, double-clicked web forms, or merged table overlaps that duplicate identical records.

### 3. Intuition
Deduplication is like removing duplicate identical photos from your smartphone gallery, keeping only one clean original copy.

### 4. Syntax
```python
import pandas as pd

df = pd.DataFrame({
    'ID': [101, 101, 102],
    'Val': ['A', 'A', 'B']
})

# Detect duplicate rows
mask = df.duplicated()

# Drop duplicates based on specific column subset
df_clean = df.drop_duplicates(subset=['ID'], keep='first')
```

### 5. Parameters
- `subset`: Column label or sequence of labels to consider for identifying duplicates.
- `keep`:
  - `'first'` (default): Mark/drop duplicates except for the first occurrence.
  - `'last'`: Mark/drop duplicates except for the last occurrence.
  - `False`: Mark/drop **ALL** occurrences of duplicate rows.
- `inplace`: If `True`, mutates original DataFrame directly.

### 6. How It Works
Pandas builds a C hash set of row tuples (or specified column subsets). As it iterates down rows, encountered hash keys present in the set are flagged as `True` duplicates.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'x': [1, 1, 2]})
print(df.drop_duplicates()) # [1, 2]
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'ID': [1, 1, 1], 'Ver': [1, 2, 3]})

# Keep latest version (last)
print(df.drop_duplicates(subset=['ID'], keep='last'))
```

### 9. Output Interpretation
`keep='last'` retains only the final row for `ID=1` (Version 3), dropping earlier versions 1 and 2.

### 10. Common Mistakes
- Forgetting `subset=` when deduplicating records where non-essential metadata columns (like timestamp) vary slightly.
- Using `keep=False` without realizing it deletes **all** duplicate records including the original copy!

### 11. Data Science Connection
Deduplicating raw web logs, customer purchase records, and merged survey tables.

### 12. AI/ML Connection
Preventing train-test data leakage where identical sample rows exist in both training and test set splits.

### 13. Interview Insight
Question: "What happens when you execute `df.drop_duplicates(keep=False)`?"
Answer: `keep=False` marks **every** occurrence of a duplicate row as `True`. Consequently, `drop_duplicates(keep=False)` removes all duplicated rows entirely, leaving zero copies of any row that had a duplicate.

### 14. Summary
Detect duplicates with `duplicated()` and remove them with `drop_duplicates()`. Use `subset` for specific column keys and `keep` to control retention.
