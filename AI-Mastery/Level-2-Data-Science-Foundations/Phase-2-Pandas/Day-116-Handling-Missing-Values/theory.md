# Day 116 Theory: Handling Missing Values

### 1. What Is It?
Handling missing values is the data cleaning step where missing `NaN` entries are either removed (`dropna()`) or filled with estimated values (`fillna()`).

### 2. Why Does It Exist?
Dropping missing rows reduces sample size and introduces bias if missingness is non-random. Imputation preserves row samples while filling blanks with statistically sound estimates.

### 3. Intuition
- **Dropping (`dropna`)**: Throwing away incomplete survey papers.
- **Mean/Median Imputation**: Filling a blank test score with the class average.
- **Forward Fill (`ffill`)**: Assuming yesterday's recorded weather temperature continued until the new reading today.

### 4. Syntax
```python
import pandas as pd

df = pd.DataFrame({'Age': [25, None, 35], 'Dept': ['IT', 'IT', 'HR']})

# Drop rows with any NaN in specific columns
df_dropped = df.dropna(subset=['Age'])

# Fill with median
df['Age_filled'] = df['Age'].fillna(df['Age'].median())

# Forward fill
df['Age_ffill'] = df['Age'].ffill()

# Group-based median imputation
df['Age_group_filled'] = df.groupby('Dept')['Age'].transform(lambda x: x.fillna(x.median()))
```

### 5. Parameters
- `how`: `'any'` (drop if any NaN present) or `'all'` (drop only if all values NaN).
- `thresh`: Minimum number of non-NaN values required to retain row/column.
- `subset`: List of column names to check for missingness.

### 6. How It Works
`fillna()` generates a boolean mask `isna()`, replacing `True` mask locations with specified scalar constants, Series values, or propagated array elements.

### 7. Simple Example
```python
import pandas as pd
s = pd.Series([10, None, 30])
print(s.fillna(s.mean())) # [10. 20. 30.]
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'Cat': ['A', 'A', 'B', 'B'], 'Val': [10, None, 100, None]})
df['Val_imp'] = df.groupby('Cat')['Val'].transform(lambda g: g.fillna(g.mean()))
print(df)
```

### 9. Output Interpretation
`groupby('Cat')` imputes Category A missing value with A's mean (10.0) and Category B missing value with B's mean (100.0).

### 10. Common Mistakes
- Using mean imputation on highly skewed columns containing extreme outliers (Use **median** instead!).
- Imputing training and test sets together, causing data leakage (Fit imputation statistics **only** on training data!).

### 11. Data Science Connection
Cleaning messy DataFrames before EDA and feature modeling.

### 12. AI/ML Connection
Imputing feature columns $X$ prior to model training (`SimpleImputer` in Scikit-Learn).

### 13. Interview Insight
Question: "When should you use Median imputation instead of Mean imputation?"
Answer: Use Median imputation when feature distributions are skewed or contain extreme outliers. The mean is pulled by outliers, whereas the median provides a robust central estimate.

### 14. Summary
Drop missing values with `dropna(subset=...)` or impute with `fillna()`. Use median for numerical skewed data, mode for categorical data, and `ffill` for time series.
