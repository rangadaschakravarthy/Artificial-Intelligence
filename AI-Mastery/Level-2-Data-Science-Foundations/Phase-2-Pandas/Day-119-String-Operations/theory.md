# Day 119 Theory: String Operations

### 1. What Is It?
Pandas string operations are vectorized text manipulation methods accessed via the `.str` accessor attribute on object/string Series.

### 2. Why Does It Exist?
Applying standard Python string methods (`str.lower()`) inside loops over Series is slow and raises errors on `NaN` entries. `.str` accessor methods apply text functions in a vectorized manner while gracefully ignoring missing `NaN` values.

### 3. Intuition
The `.str` accessor is like a text cleaning Swiss Army knife attached to a column, allowing you to clean 1,000 messy text cells simultaneously.

### 4. Syntax
```python
import pandas as pd

s = pd.Series(['  Alice  ', 'BOB ', 'charlie'])

# Clean casing and whitespace
s_clean = s.str.strip().str.title()

# Substring replacement
s_replaced = s.str.replace('A', 'Z')

# Regex pattern extraction
emails = pd.Series(['alice@gmail.com', 'bob@yahoo.com'])
domain = emails.str.extract(r'@(\w+)\.')
```

### 5. Parameters
- `pat`: Regex pattern or substring to match.
- `regex`: Boolean in `replace()` indicating if pattern is a regular expression.
- `expand`: Boolean in `split()` / `extract()`. If `True`, returns a DataFrame of split columns.

### 6. How It Works
The `.str` accessor wraps string methods into vectorized loops that check for `NaN` entries (preserving `NaN` without throwing AttributeError) and return transformed Series.

### 7. Simple Example
```python
import pandas as pd
s = pd.Series(['  apple ', 'BANANA'])
print(s.str.strip().str.lower()) # ['apple', 'banana']
```

### 8. Intermediate Example
```python
import pandas as pd
names = pd.Series(['John Smith', 'Jane Doe'])
split_df = names.str.split(' ', expand=True)
split_df.columns = ['First', 'Last']
print(split_df)
```

### 9. Output Interpretation
`expand=True` expands the split result into a 2-column DataFrame with headers `'First'` and `'Last'`.

### 10. Common Mistakes
- Forgetting the `.str` accessor prefix (`df['col'].lower()` throws `AttributeError: 'Series' object has no attribute 'lower'`).
- Forgetting `regex=False` when replacing literal special characters like `$` or `.` (`s.str.replace('$', '')` interprets `$` as end-of-string regex!).

### 11. Data Science Connection
Standardizing category labels, stripping whitespace, and parsing text features during data preparation.

### 12. AI/ML Connection
Text feature engineering: extracting email domains, parsing product codes, and cleaning text for Natural Language Processing (NLP) tokenization.

### 13. Interview Insight
Question: "Why is `s.str.lower()` preferred over `s.apply(lambda x: x.lower())`?"
Answer: `s.str.lower()` is optimized, handles missing `NaN` values automatically without crashing, and runs significantly faster than executing custom Python lambda functions over every row.

### 14. Summary
Access vectorized text methods using `.str`. Clean whitespace with `.str.strip()`, standardize casing with `.str.lower()`, and extract text with regex patterns.
