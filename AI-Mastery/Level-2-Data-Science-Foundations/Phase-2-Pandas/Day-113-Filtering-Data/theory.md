# Day 113 Theory: Filtering Data

### 1. What Is It?
Data filtering is the process of selecting a subset of DataFrame rows that satisfy specific logical conditions or query constraints.

### 2. Why Does It Exist?
Datasets contain diverse observations. Filtering isolates specific sub-cohorts, strips corrupted entries, and focuses analysis on target categories.

### 3. Intuition
Filtering acts like a coffee filter or sieve that passes through only the dataset rows that meet your custom search rules.

### 4. Syntax
```python
import pandas as pd

df = pd.DataFrame({'Age': [20, 30, 40], 'City': ['NY', 'LA', 'NY']})

# Single Condition
sub1 = df[df['Age'] > 25]

# Multiple Conditions (AND &)
sub2 = df[(df['Age'] > 25) & (df['City'] == 'NY')]

# Membership isin()
sub3 = df[df['City'].isin(['NY', 'SF'])]

# Range between()
sub4 = df[df['Age'].between(25, 35)]

# Query string
sub5 = df.query("Age > 25 and City == 'NY'")
```

### 5. Parameters
- `isin(values)`: Iterable of values to match.
- `between(left, right)`: Inclusive bounds $[left, right]$.
- `query(expr)`: String boolean expression evaluated using `numexpr`.

### 6. How It Works
Pandas evaluates expressions into 1D boolean Series masks, passing the boolean array down to C-level row index filters to extract matching rows.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'Score': [50, 75, 90]})
print(df[df['Score'] >= 75])
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'State': ['CA', 'NY', 'TX', 'FL']})
print(df[df['State'].isin(['CA', 'NY'])])
```

### 9. Output Interpretation
`.isin(['CA', 'NY'])` generates a boolean mask `[True, True, False, False]`, returning rows for CA and NY.

### 10. Common Mistakes
- Using Python `and` / `or` keywords instead of bitwise `&` / `|`.
- Omitting parentheses around multiple conditions (`df[df['A'] > 1 & df['B'] < 5]` fails due to operator precedence!).

### 11. Data Science Connection
Segmenting customer demographics, filtering active users, and auditing subset statistics.

### 12. AI/ML Connection
Filtering out missing or corrupt rows before model training and extracting specific sub-group test evaluation sets.

### 13. Interview Insight
Question: "What is the advantage of using `df.query()` over standard boolean masking `df[(cond1) & (cond2)]`?"
Answer: `df.query()` accepts clean readable SQL-like string expressions (e.g. `"Age > 25 and City == 'NY'"`), eliminates repetitive `df[...]` references, and uses `numexpr` under the hood for faster memory-efficient evaluation on large DataFrames.

### 14. Summary
Filter rows using boolean masks `df[cond]`, `isin()`, `between()`, or `df.query()`. Always enclose multiple conditions in parentheses.
