# Day 127 Theory: Time Series

### 1. What Is It?
Pandas time-series support centers on the `DatetimeIndex`, a highly optimized index structure for handling, slicing, and resampling timestamped observation sequences.

### 2. Why Does It Exist?
Standard object strings (`'2023-01-01'`) lack temporal awareness. `DatetimeIndex` enables time-aware math, frequency conversion, and natural date range slicing.

### 3. Intuition
Treating date strings as numbers allows filtering data between two calendar points instantly without writing complex string regex rules.

### 4. Syntax
```python
# Convert column to datetime:
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')

# Set as index:
df.set_index('Date', inplace=True)

# Generate regular date ranges:
dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
```

### 5. Parameters
- `arg`: String, list, or Series to parse into datetime.
- `format`: String specifying datetime format codes (`%Y`, `%m`, `%d`, `%H`, `%M`, `%S`).
- `errors`: `'raise'`, `'coerce'` (sets unparseable values to `NaT`), `'ignore'`.
- `freq`: Frequency string (`'D'` daily, `'M'` month-end, `'H'` hourly, `'B'` business day).

### 6. How It Works
Pandas stores timestamps internally as 64-bit integers (`datetime64[ns]`) representing nanoseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

### 7. Simple Example
```python
import pandas as pd
dates = pd.to_datetime(['2023-01-01', '2023-01-02'])
print(type(dates)) # DatetimeIndex
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=5, freq='D'),
    'Val': [10, 20, 30, 40, 50]
}).set_index('Date')
print(df.loc['2023-01-02':'2023-01-04'])
```

### 9. Output Interpretation
Index becomes a `DatetimeIndex` object. Partial string slicing returns rows falling within designated calendar ranges.

### 10. Common Mistakes
- Slicing date ranges without sorting the `DatetimeIndex` first (triggers `KeyError` or unexpected slice results).
- Mixing U.S. date format (`MM/DD/YYYY`) with international format (`DD/MM/YYYY`) without specifying `dayfirst=True` or explicit `format`.

### 11. Data Science Connection
Financial time series analysis, seasonal trend decomposition, and log analysis.

### 12. AI/ML Connection
Creating lag features, rolling windows, and time-aware validation splits for forecasting models.

### 13. Interview Insight
Question: "What is `NaT` in Pandas?"
Answer: `NaT` stands for "Not a Time", representing missing or unparseable timestamp values in datetime Series (analogous to `NaN` for numeric values).

### 14. Summary
`pd.to_datetime()` and `DatetimeIndex` provide fast, temporal-aware indexing and partial string range slicing for time series data.
