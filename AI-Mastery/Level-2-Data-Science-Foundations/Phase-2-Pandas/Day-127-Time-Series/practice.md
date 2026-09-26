# Day 127 Practice Questions: Time Series

## Level 1 — Basic
1. What function converts string objects to datetime objects in Pandas?
2. What missing value representation is used for datetime Series (`NaT`)?
3. How do you generate a sequence of 10 business days starting from `'2023-01-01'`?
4. True or False: Slicing a DataFrame with `df.loc['2023-05']` selects all rows in May 2023 if the index is a `DatetimeIndex`.
5. What parameter in `pd.to_datetime()` turns unparseable date strings into `NaT` instead of raising an error?

## Level 2 — Coding
1. Convert column `'Date_Text'` to `datetime64[ns]` using format `'%Y/%m/%d'`.
2. Generate a hourly date range for the month of January 2023.
3. Set a datetime column as the DataFrame index and sort the index.
4. Slice a datetime-indexed DataFrame between `'2023-03-01'` and `'2023-03-15'`.
5. Check if a DataFrame index is a valid `DatetimeIndex`.

## Level 3 — Data Analysis
1. Parse messy transactional timestamp strings and set `DatetimeIndex`.
2. Extract all sales transactions occurring in Q3 2022 using partial string slicing.
3. Filter server log records occurring specifically between 02:00 AM and 04:00 AM.
4. Verify whether any date timestamps are missing from a continuous daily sequence.
5. Filter stock price observations to business days only using `freq='B'`.

## Level 4 — Debugging
1. Fix error: `KeyError: '2023-01'` when attempting partial string date slicing on a regular string index.
2. Fix date parsing bug where `'04/01/2023'` is parsed as April 1st instead of January 4th.
3. Correct `ValueError: Unrecognized datetime string format`.

## Level 5 — AI/ML Application
1. Demonstrate building a temporal dataset with `DatetimeIndex` for time-series forecasting.
2. Why must time-series data be sorted by `DatetimeIndex` before splitting into train/test sets?
3. Create time-based sample weights based on recency.

## Level 6 — Interview Questions
1. How does Pandas represent datetime objects internally under the hood?
2. Explain the difference between `DatetimeIndex`, `PeriodIndex`, and `TimedeltaIndex`.
3. How do you handle timezone localization (`tz_localize`) and conversion (`tz_convert`) in Pandas?
4. What is the performance benefit of `DatetimeIndex` slicing vs string filtering using boolean masks?
5. How do you construct custom business day calendars in Pandas?
