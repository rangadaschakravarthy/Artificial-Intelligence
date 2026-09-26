# Day 122 Solutions: Apply and Map

## Level 1 — Basic
1. `Series.map()`.
2. `axis=1` applies the function row-by-row (passing each row as a Series to the function).
3. It returns a vector matching the exact number of rows in `df`.
4. Unmapped keys are replaced with `NaN`.
5. `s.apply(lambda x: x * 2)`.

## Level 2 — Coding
1.
```python
import pandas as pd
df['Points'] = df['Grade'].map({'A': 4.0, 'B': 3.0, 'C': 2.0})
```
2.
```python
df['Full_Name'] = df.apply(lambda r: f"{r['First_Name']} {r['Last_Name']}", axis=1)
```
3.
```python
df['City_Avg_Temp'] = df.groupby('City')['Temperature'].transform('mean')
```
4.
```python
df_rounded = df.apply(lambda col: col.round(2) if col.dtype in ['float64', 'float32'] else col)
```
5.
```python
df['Is_High_Earner'] = df.apply(lambda r: 1 if r['Income'] > 100000 and r['Age'] > 30 else 0, axis=1)
```

## Level 3 — Data Analysis
1.
```python
df['Regional_Total'] = df.groupby('Region')['Sales'].transform('sum')
df['Sales_Pct'] = (df['Sales'] / df['Regional_Total']) * 100
```
2.
```python
min_sal = df.groupby('Dept')['Salary'].transform('min')
max_sal = df.groupby('Dept')['Salary'].transform('max')
df['Salary_Norm'] = (df['Salary'] - min_sal) / (max_sal - min_sal)
```
3.
```python
def calc_tax(r):
    rate = 0.08 if r['State'] == 'CA' else 0.05
    return r['Income'] * rate

df['Tax'] = df.apply(calc_tax, axis=1)
```
4.
```python
def price_tier(p):
    if p < 50: return 'Budget'
    elif p < 200: return 'Mid-Range'
    else: return 'Premium'

df['Tier'] = df['Price'].apply(price_tier)
```
5.
```python
df['Quarter'] = pd.to_datetime(df['Date']).apply(lambda d: f"Q{d.quarter}-{d.year}")
```

## Level 4 — Debugging
1. Specify `axis=1` when executing functions operating across row columns: `df.apply(..., axis=1)`.
2. Use `.map()` with a fallback function or use `.replace()` which leaves unmentioned keys unchanged: `s.replace({'Y': 1})`.
3. Replace slow `df.apply(..., axis=1)` with vectorized column multiplication: `df['Total'] = df['A'] * df['B']`.

## Level 5 — AI/ML Application
1.
```python
mean_g = df.groupby('Entity')['Val'].transform('mean')
std_g = df.groupby('Entity')['Val'].transform('std')
df['Z_Score'] = (df['Val'] - mean_g) / std_g
```
2.
```python
label_dict = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
df['Target'] = df['Species'].map(label_dict)
```
3. `GroupBy.transform()` computes metrics strictly partitioned within designated grouping boundaries, keeping sub-cohort statistics localized.

## Level 6 — Interview Questions
1. Vectorized NumPy (Fastest, ~1x) > `Series.map()` (~5x) > `DataFrame.apply(axis=1)` (Slowest, ~100x due to row Series construction overhead).
2. `.applymap()` (or `DataFrame.map()` in Pandas 2.1+) applies a function to every individual scalar element in a DataFrame. `.apply()` applies functions to whole 1D vectors (columns or rows).
3. If the custom function returns a Series, `.apply()` combines the returned Series into a new DataFrame.
4. Use libraries like `Swifter` or `Dask` which partition DataFrame rows across available CPU cores (`df.swifter.apply(...)`).
5. Choose `.replace()` when you only want to substitute specific keys while retaining existing values for all unmentioned keys. `.map()` replaces unmentioned keys with `NaN`.
