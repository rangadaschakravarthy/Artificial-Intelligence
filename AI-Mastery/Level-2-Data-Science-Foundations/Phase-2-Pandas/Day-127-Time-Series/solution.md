# Day 127 Solutions: Time Series

## Level 1 — Basic
1. `pd.to_datetime()`.
2. `NaT` (Not a Time).
3. `pd.date_range(start='2023-01-01', periods=10, freq='B')`.
4. True. Partial string indexing automatically matches all timestamps falling within May 2023.
5. `errors='coerce'`.

## Level 2 — Coding
1.
```python
import pandas as pd
df['Date_Text'] = pd.to_datetime(df['Date_Text'], format='%Y/%m/%d')
```
2.
```python
hourly = pd.date_range(start='2023-01-01', end='2023-01-31 23:00', freq='H')
```
3.
```python
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)
```
4.
```python
sliced = df.loc['2023-03-01':'2023-03-15']
```
5.
```python
is_dt = isinstance(df.index, pd.DatetimeIndex)
```

## Level 3 — Data Analysis
1.
```python
df['Timestamp'] = pd.to_datetime(df['Raw_Time'], errors='coerce')
df.set_index('Timestamp', inplace=True)
```
2.
```python
q3_sales = df.loc['2022-07':'2022-09']
```
3.
```python
early_logs = df.between_time('02:00', '04:00')
```
4.
```python
full_range = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
missing_dates = full_range.difference(df.index)
print("Missing Dates:", missing_dates)
```
5.
```python
bday_df = df[df.index.dayofweek < 5]
```

## Level 4 — Debugging
1. Convert column to datetime and set as index first: `df.index = pd.to_datetime(df.index)`.
2. Pass explicit format string `format='%d/%m/%Y'` or set `dayfirst=True`.
3. Set `errors='coerce'` to replace corrupted datetime string elements with `NaT`.

## Level 5 — AI/ML Application
1.
```python
ts_df = pd.DataFrame({'Target': y_series}, index=pd.date_range('2023-01-01', periods=len(y_series), freq='D'))
```
2. Time-series data exhibits temporal dependency (autocorrelation). Random splitting causes future data leakage into past training sets.
3.
```python
days_diff = (df.index.max() - df.index).days
weights = 1.0 / (1.0 + days_diff)
```

## Level 6 — Interview Questions
1. As 64-bit integers (`datetime64[ns]`) counting nanoseconds elapsed since January 1, 1970 UTC epoch.
2. `DatetimeIndex` represents specific points in time. `PeriodIndex` represents time spans (e.g. Month of June 2023). `TimedeltaIndex` represents durations or differences between timestamps.
3. Localize naive datetime to UTC via `.tz_localize('UTC')`, then convert timezone via `.tz_convert('America/New_York')`.
4. `DatetimeIndex` partial string slicing uses fast integer range binary searches ($O(\log N)$) rather than scanning every string element ($O(N)$).
5. Use `pandas.tseries.holiday.AbstractHolidayCalendar` to define custom business holiday calendars.
