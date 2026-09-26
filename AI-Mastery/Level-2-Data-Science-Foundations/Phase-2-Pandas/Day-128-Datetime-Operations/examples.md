# Day 128 Worked Examples: Datetime Operations

## Example 1 — Beginner: Extracting Date Components with .dt
```python
import pandas as pd

df = pd.DataFrame({'Date': pd.date_range('2023-05-01', periods=3, freq='D')})

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day_Name'] = df['Date'].dt.day_name()
df['Is_Weekend'] = df['Date'].dt.dayofweek >= 5

print("Extracted Temporal Features:
", df)
```

## Example 2 — Practical: Resampling Daily Data to Monthly Aggregates
```python
import pandas as pd

daily_dates = pd.date_range('2023-01-01', periods=60, freq='D')
df = pd.DataFrame({'Sales': range(100, 160)}, index=daily_dates)

# Downsample daily sales to Monthly sum
monthly_sales = df.resample('M').sum()
print("Monthly Aggregated Sales:
", monthly_sales)
```

## Example 3 — Intermediate: Rolling 7-Day Moving Average
```python
import pandas as pd

dates = pd.date_range('2023-01-01', periods=10, freq='D')
df = pd.DataFrame({'Price': [10, 12, 11, 15, 14, 18, 20, 19, 22, 25]}, index=dates)

# 3-Day Simple Moving Average (SMA)
df['SMA_3'] = df['Price'].rolling(window=3).mean()
print("Stock Price with 3-Day SMA:
", df)
```

## Example 4 — Real Dataset: E-Commerce Hourly Order Resampling
```python
import pandas as pd

hourly_dates = pd.date_range('2023-06-01 00:00', periods=48, freq='H')
orders = pd.DataFrame({'Order_Count': [5, 2, 1, 0, 1, 4, 12, 25] * 6}, index=hourly_dates)

# Resample to 6-Hour intervals computing total orders and max orders
resampled = orders.resample('6H').agg({'Order_Count': ['sum', 'max']})
print("6-Hour Resampled Order Metrics:
", resampled)
```

## Example 5 — AI/ML Application: Autoregressive Lag Feature Engineering
```python
import pandas as pd

dates = pd.date_range('2023-01-01', periods=5, freq='D')
df = pd.DataFrame({'Demand': [100, 115, 108, 130, 125]}, index=dates)

# Create Lag 1 (yesterday demand) and Lag 2 (2 days ago demand)
df['Demand_Lag_1'] = df['Demand'].shift(1)
df['Demand_Lag_2'] = df['Demand'].shift(2)

print("Time-Series Machine Learning Feature Matrix:
", df)
```
