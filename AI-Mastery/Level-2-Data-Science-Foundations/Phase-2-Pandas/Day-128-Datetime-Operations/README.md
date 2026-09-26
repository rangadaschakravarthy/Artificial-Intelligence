# Day 128 — Datetime Operations

## Learning Objectives
- Access temporal components (year, month, day, dayofweek, hour) using the `.dt` accessor.
- Perform time-series resampling and frequency conversion using `.resample()`.
- Calculate moving statistics using rolling window accessor `.rolling()`.

## Prerequisites
- Day 120: GroupBy
- Day 127: Time Series

## Topics Covered
- Pandas `.dt` accessor property attributes (`dt.year`, `dt.month`, `dt.day`, `dt.day_name()`, `dt.hour`)
- Downsampling and upsampling time series using `.resample()`
- Aggregation rules in `.resample('M')`, `.resample('W')`, `.resample('D')`
- Rolling window calculations using `.rolling(window=7).mean()`
- Shifting data forward/backward using `.shift(1)` for lag feature generation

## Why This Matters
Raw timestamps are rarely fed directly into algorithms. Extracting temporal features and calculating rolling averages are essential feature engineering techniques.

## Real-World Usage
Extracting `'DayOfWeek'` to model weekend retail sales spikes and computing 30-day rolling moving averages (SMA) for stock trend smoothing.

## Study Order
1. Read `theory.md` for `.dt`, `.resample()`, and `.rolling()`.
2. Study `examples.md` for rolling calculations.
3. Run `code.py` to inspect feature outputs.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Extract calendar components from a purchase date column.
- Calculate 7-day rolling average revenue and 1-day lag features for time series prediction.

## Interview Preparation
- What is the difference between `.resample()` and `.groupby()` in Pandas?
- What does `.shift(1)` do, and how is it used to engineer time-series lag features?

## Completion Checklist
- [ ] I can extract temporal properties using `df['date'].dt`.
- [ ] I can downsample time series data using `.resample()`.
- [ ] I can compute rolling window metrics using `.rolling()`.
- [ ] I can create lag features using `.shift()`.

## Difficulty
Intermediate
