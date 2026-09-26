# Day 128 Theory: Datetime Operations

### 1. What Is It?
Pandas provides specialized temporal manipulation tools: the `.dt` accessor for element-wise date feature extraction, `.resample()` for frequency aggregation, and `.rolling()` for moving-window statistics.

### 2. Why Does It Exist?
Timestamps contain multiple hierarchical signals (day of week, hour of day, monthly trends). `.dt`, `.resample()`, and `.rolling()` convert raw timestamps into predictive features.

### 3. Intuition
- **`.dt`**: A calendar component extractor (pull out year, month, or day name).
- **`.resample()`**: A GroupBy specialized for time frequencies (e.g. compress hourly logs into daily summaries).
- **`.rolling()`**: A moving inspection window sliding over sequential observations.

### 4. Syntax
```python
# Extract Date Components:
df['Year'] = df['Date'].dt.year
df['Day_Name'] = df['Date'].dt.day_name()

# Resample Frequency (Daily to Monthly):
monthly_df = df.resample('M').mean()

# Rolling Window 7-Day Average:
df['SMA_7'] = df['Sales'].rolling(window=7).mean()

# Lag Feature (Shift forward 1 step):
df['Lag_1'] = df['Sales'].shift(1)
```

### 5. Parameters
- `rule` (in `.resample()`): Frequency string (`'D'`, `'W'`, `'M'`, `'Q'`, `'Y'`).
- `window` (in `.rolling()`): Integer size or time offset string (`'7D'`).
- `periods` (in `.shift()`): Number of shift steps (positive for lag, negative for lead).

### 6. How It Works
- `.dt` vectors expose C-compiled datetime properties.
- `.resample()` partitions timestamps into fixed frequency bins and aggregates values.
- `.rolling()` maintains a sliding FIFO queue of size $W$ over sequential rows.

### 7. Simple Example
```python
import pandas as pd
s = pd.to_datetime(pd.Series(['2023-01-01', '2023-01-02']))
print(s.dt.day_name())
```

### 8. Intermediate Example
```python
import pandas as pd
dates = pd.date_range('2023-01-01', periods=5, freq='D')
df = pd.DataFrame({'Sales': [10, 20, 30, 40, 50]}, index=dates)
df['SMA_3'] = df['Sales'].rolling(3).mean()
print(df)
```

### 9. Output Interpretation
`.dt` returns a Series. `.resample()` produces a resampled DataFrame indexed by new frequency points. `.rolling()` returns a Series containing window summary metrics (with leading `NaN`s for incomplete initial windows).

### 10. Common Mistakes
- Calling `.dt` properties on a column that is not `datetime64` dtype (raises `AttributeError: Can only use .dt accessor with datetimelike values`).
- Introducing target leakage when creating rolling window features by forgetting to `.shift(1)` before predicting future timestamps!

### 11. Data Science Connection
Feature engineering, time-series trend smoothing, and temporal pattern analysis.

### 12. AI/ML Connection
Creating autoregressive lag features ($y_{t-1}, y_{t-2}$) and rolling window volatility features for forecasting models (XGBoost, ARIMA).

### 13. Interview Insight
Question: "Why must you shift rolling window features when building time-series forecasting models?"
Answer: Without `.shift(1)`, `rolling(7).mean()` at time $t$ includes target value $y_t$ in its window, causing target leakage into feature matrix $X_t$.

### 14. Summary
`.dt` extracts temporal components, `.resample()` aggregates frequency intervals, `.rolling()` calculates moving averages, and `.shift()` creates lag features.
