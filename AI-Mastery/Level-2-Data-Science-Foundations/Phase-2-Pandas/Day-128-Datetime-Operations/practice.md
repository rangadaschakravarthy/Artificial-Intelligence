# Day 128 Practice Questions: Datetime Operations

## Level 1 — Basic
1. What Pandas accessor property extracts date components from a datetime Series?
2. What function converts daily data into monthly aggregated sums?
3. How do you create a 7-day rolling moving average on a Series?
4. What does the `.shift(1)` method do to Series rows?
5. How do you extract the day name (e.g., `'Monday'`) from a datetime column?

## Level 2 — Coding
1. Extract `Year`, `Month`, `Day`, and `Hour` as separate integer columns from `df['Timestamp']`.
2. Downsample an hourly dataset to daily mean values using `.resample('D')`.
3. Compute a 30-day rolling standard deviation on stock return data.
4. Shift column `'Price'` forward by 2 periods to create `Price_Lag_2`.
5. Compute percentage change over time using `df['Price'].pct_change()`.

## Level 3 — Data Analysis
1. Analyze website traffic peaks by extracting hour of day (`dt.hour`) and grouping by hour.
2. Smooth volatile daily IoT sensor readings using a 7-day rolling median.
3. Resample high-frequency 1-minute stock price ticks into 15-minute OHLC (Open, High, Low, Close) bars.
4. Compare weekday vs weekend sales volume using `dt.dayofweek`.
5. Engineer 1-day, 7-day, and 30-day lag features for time-series forecasting.

## Level 4 — Debugging
1. Fix error: `AttributeError: Can only use .dt accessor with datetimelike values`.
2. Fix target leakage bug where rolling average feature includes the target value of the prediction day.
3. Correct `TypeError: 'TypeError: Only valid with DatetimeIndex'` when calling `.resample()`.

## Level 5 — AI/ML Application
1. Demonstrate engineering a complete temporal feature set (`hour`, `dayofweek`, `is_month_end`, `lag_1`, `rolling_7_mean`) for demand forecasting ML models.
2. How does `.resample()` help standardize irregular sensor polling frequencies for ML input alignment?
3. Explain why `min_periods` parameter in `.rolling()` is useful for handling early missing window values.

## Level 6 — Interview Questions
1. Compare `.resample()` vs `df.groupby(pd.Grouper(freq='M'))`.
2. Explain the difference between Exponential Moving Average (EMA) and Simple Moving Average (SMA) in Pandas.
3. How do you perform rolling calculations with a time-based window (e.g. `.rolling('7D')`) vs row-count window (`.rolling(7)`)?
4. What is the difference between downsampling and upsampling in `.resample()`?
5. How does `.resample()` handle interpolation during upsampling?
