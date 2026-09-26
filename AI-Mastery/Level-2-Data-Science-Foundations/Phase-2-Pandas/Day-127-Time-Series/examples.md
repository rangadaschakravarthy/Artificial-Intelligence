# Day 127 Worked Examples: Time Series

## Example 1 — Beginner: Parsing Dates with pd.to_datetime
```python
import pandas as pd

raw_dates = ['2023-01-15', '2023/02/20', 'March 5, 2023']
dt_series = pd.to_datetime(raw_dates)
print("Parsed Datetime Series:
", dt_series)
print("Dtype:", dt_series.dtype)
```

## Example 2 — Practical: Generating Date Ranges with pd.date_range
```python
import pandas as pd

# Daily frequency
daily_dates = pd.date_range(start='2023-01-01', end='2023-01-05', freq='D')

# Business day frequency (skips weekends)
bday_dates = pd.date_range(start='2023-01-01', periods=5, freq='B')

print("Daily Dates:", daily_dates)
print("Business Dates:", bday_dates)
```

## Example 3 — Intermediate: Partial String Slicing on DatetimeIndex
```python
import pandas as pd

dates = pd.date_range('2022-11-01', periods=90, freq='D')
df = pd.DataFrame({'Sales': range(90)}, index=dates)

# Partial string slicing for entire month
december_sales = df.loc['2022-12']
print("December 2022 Sales Head:
", december_sales.head())
```

## Example 4 — Real Dataset: Parsing European Format Dates
```python
import pandas as pd

# European format: DD/MM/YYYY
euro_df = pd.DataFrame({
    'Date_Str': ['31/12/2022', '01/01/2023', '15/02/2023'],
    'Metric': [100, 110, 120]
})

euro_df['Date'] = pd.to_datetime(euro_df['Date_Str'], format='%d/%m/%Y')
euro_df.set_index('Date', inplace=True)
print("Parsed European Date Index DataFrame:
", euro_df)
```

## Example 5 — AI/ML Application: Temporal Sequence Indexing
```python
import pandas as pd

# Sensor log dataset indexed by timestamp
timestamps = pd.date_range('2023-05-01 00:00', periods=5, freq='1H')
sensor_df = pd.DataFrame({
    'Temp_C': [21.5, 22.0, 22.8, 23.5, 21.9],
    'Pressure_bar': [1.01, 1.02, 1.01, 1.00, 1.01]
}, index=timestamps)

print("Sensor Time Series Matrix:
", sensor_df)
```
