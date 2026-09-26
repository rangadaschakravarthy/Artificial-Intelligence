# Day 123 Theory: Merge

### 1. What Is It?
`pd.merge()` combines two DataFrames horizontally based on matching values in specified key columns (relational database joins).

### 2. Why Does It Exist?
Data is stored relationally to eliminate redundancy. To perform modeling or analysis, data from separate tables (e.g. Users and Orders) must be joined.

### 3. Intuition
- **Inner**: Kept only if key exists in **both** tables (Intersection $\cap$).
- **Left**: Keep **all** rows from left table, matching right table records where available.
- **Right**: Keep **all** rows from right table, matching left table records where available.
- **Outer**: Keep **all** rows from both tables (Union $\cup$).

### 4. Syntax
```python
pd.merge(
    left_df, right_df,
    how='inner', # 'left', 'right', 'outer'
    on='KeyCol',  # or left_on='LKey', right_on='RKey'
    suffixes=('_left', '_right')
)
```

### 5. Parameters
- `how`: `'inner'`, `'left'`, `'right'`, `'outer'`, `'cross'`.
- `on`: Column name(s) present in both tables.
- `left_on` / `right_on`: Differing key column names in left and right tables.
- `suffixes`: Tuple of strings added to overlapping non-key column titles.
- `indicator`: If `True`, adds a column `_merge` showing key source origin (`both`, `left_only`, `right_only`).

### 6. How It Works
Pandas builds a hash index of join keys from the right DataFrame and scans the left DataFrame, matching keys and constructing merged records.

### 7. Simple Example
```python
import pandas as pd
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Score': [90, 85]})
print(pd.merge(df1, df2, on='ID'))
```

### 8. Intermediate Example
```python
import pandas as pd
users = pd.DataFrame({'UID': [101, 102, 103], 'Name': ['A', 'B', 'C']})
orders = pd.DataFrame({'User_ID': [101, 101, 104], 'Amount': [50, 75, 120]})
print(pd.merge(users, orders, left_on='UID', right_on='User_ID', how='left'))
```

### 9. Output Interpretation
The resulting DataFrame contains key columns alongside combined non-key attributes from both sources. Unmatched records in outer/left joins fill missing right attributes with `NaN`.

### 10. Common Mistakes
- Unintentional many-to-many joins resulting in combinatorial row explosions.
- Forgetting to handle column name collisions when non-key columns share titles across tables.

### 11. Data Science Connection
Assembling features from relational database schemas (SQL joins in Python).

### 12. AI/ML Connection
Enriching primary transaction entity logs with static user demographic attributes prior to ML training.

### 13. Interview Insight
Question: "What happens during a many-to-many join in `pd.merge()`?"
Answer: If key value `K` appears $N$ times in left DF and $M$ times in right DF, the merged result contains $N 	imes M$ rows for key `K`.

### 14. Summary
`pd.merge()` performs relational database join operations (Inner, Left, Right, Outer) using column keys to assemble unified analytical DataFrames.
