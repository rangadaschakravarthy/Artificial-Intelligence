# Day 127 — Time Series

## Learning Objectives
- Parse, index, and query temporal data using Pandas `DatetimeIndex`.
- Master `pd.to_datetime()` for flexible date parsing.
- Slice time-series DataFrames using natural date string indexing.

## Prerequisites
- Day 107: Series
- Day 109: Index and Columns

## Topics Covered
- `pd.to_datetime()` and `format` specifiers
- Setting `DatetimeIndex` on DataFrames
- Partial string indexing (e.g. `'2023'`, `'2023-05'`)
- Date range generation with `pd.date_range()`
- Handling timezone localization and conversion

## Why This Matters
Financial data, IoT sensor telemetry, web traffic, and economic indicators are all timestamped time-series sequences.

## Real-World Usage
Analyzing stock market tick logs, tracking hourly server CPU usage spikes, and analyzing monthly sales seasonality.

## Study Order
1. Read `theory.md` for DatetimeIndex fundamentals.
2. Examine `examples.md` for date indexing patterns.
3. Run `code.py` to see temporal slicing in action.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Convert raw messy string dates into `DatetimeIndex`.
- Slice a multi-year sales dataset to extract Q4 2022 records using partial string indexing.

## Interview Preparation
- What is a `DatetimeIndex` in Pandas, and why is it faster than standard object indexing for date filtering?
- How do you parse custom string date formats like `'31/12/2023'` using `pd.to_datetime()`?

## Completion Checklist
- [ ] I can parse date strings using `pd.to_datetime()`.
- [ ] I can create date sequences using `pd.date_range()`.
- [ ] I can set and use a `DatetimeIndex`.
- [ ] I can perform partial string date slicing.

## Difficulty
Intermediate
