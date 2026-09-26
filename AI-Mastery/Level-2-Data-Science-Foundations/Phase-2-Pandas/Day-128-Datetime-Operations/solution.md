# Day 128 Solutions: Datetime Operations

## Level 1 — Basic
1. `.dt` property accessor.
2. `.resample('M').sum()`.
3. `df['Col'].rolling(window=7).mean()`.
4. It shifts values down by 1 row, moving past observation $t-1$ into current row position $t$.
5. `df['Date'].dt.day_name()`.

## Level 2 — Coding
1.
```python
import pandas as pd
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month
df['Day'] = df['Timestamp'].dt.day
df['Hour'] = df['Timestamp'].dt.hour
```
2.
```python
daily_mean = df.resample('D').mean()
```
3.
```python
df['Vol_30'] = df['Return'].rolling(30).std()
```
4.
```python
df['Price_Lag_2'] = df['Price'].shift(2)
```
5.
```python
df['Pct_Change'] = df['Price'].pct_change()
```

## Level 3 — Data Analysis
1.
```python
df['Hour'] = df['Timestamp'].dt.hour
hourly_traffic = df.groupby('Hour')['Visits'].sum()
print(hourly_traffic)
```
2.
```python
df['Smoothed_Temp'] = df['Temp'].rolling(7, min_periods=1).median()
```
3.
```python
ohlc = df['Price'].resample('15Min').ohlc()
print(ohlc)
```
4.
```python
df['Is_Weekend'] = df.index.dayofweek >= 5
print(df.groupby('Is_Weekend')['Sales'].mean())
```
5.
```python
df['Lag_1'] = df['Target'].shift(1)
df['Lag_7'] = df['Target'].shift(7)
df['Lag_30'] = df['Target'].shift(30)
```

## Level 4 — Debugging
1. Convert column to datetime first: `df['Date'] = pd.to_datetime(df['Date'])` before calling `.dt`.
2. Shift rolling feature output by 1 step: `df['Roll_7'] = df['Target'].shift(1).rolling(7).mean()`.
3. Set datetime column as DataFrame index before calling `.resample()` or pass `on='Date'` parameter: `df.resample('D', on='Date').mean()`.

## Level 5 — AI/ML Application
1.
```python
df['Hour'] = df.index.hour
df['DayOfWeek'] = df.index.dayofweek
df['Is_Month_End'] = df.index.is_month_end.astype(int)
df['Lag_1'] = df['Target'].shift(1)
df['Roll_7_Mean'] = df['Target'].shift(1).rolling(7).mean()
```
2. Resampling downsamples irregular sensor timestamp bursts into regular 1-minute or 1-hour uniform time steps, filling gaps with interpolation.
3. `min_periods=1` allows `.rolling()` to return calculated averages for early rows before full window size $W$ is reached, avoiding unnecessary leading `NaN`s.

## Level 6 — Interview Questions
1. They are logically identical. `df.resample('M')` is shorthand for `df.groupby(pd.Grouper(freq='M'))`.
2. SMA applies equal weights across all $W$ window values (`df['val'].rolling(W).mean()`). EMA applies exponentially decreasing weights to older observations (`df['val'].ewm(span=W).mean()`).
3. Row-count `.rolling(7)` requires fixed row counts regardless of time gaps. Time-based `.rolling('7D')` looks back exactly 7 calendar days regardless of missing weekend rows.
4. Downsampling reduces data frequency (e.g. Daily to Monthly, requires aggregation). Upsampling increases data frequency (e.g. Monthly to Daily, requires interpolation like `.ffill()`).
5. Upsampling creates empty intermediate timestamps which are filled using interpolation methods (`.ffill()`, `.bfill()`, `.interpolate()`).
