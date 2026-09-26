# Day 129 Solutions: Data Cleaning Workflow

## Level 1 — Basic
1. 1) Raw Inspection (`.info()`, `.head()`), 2) Standardize Column Headers, 3) Deduplication.
2. `df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')`.
3. `pd.to_numeric(df['Col'], errors='coerce')`.
4. True. Working on a explicit copy preserves raw data for auditing and re-runs.
5. `assert df.isna().sum().sum() == 0, "Missing values found!"`.

## Level 2 — Coding
1.
```python
import pandas as pd
str_cols = df.select_dtypes(include='object').columns
for col in str_cols:
    df[col] = df[col].str.strip()
```
2.
```python
df['Salary'] = df['Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
```
3.
```python
df.drop_duplicates(subset=['Customer_ID'], inplace=True)
```
4.
```python
import numpy as np
df.loc[(df['Age'] < 0) | (df['Age'] > 120), 'Age'] = np.nan
```
5.
```python
assert len(df) > 0, "Cleaned DataFrame is empty!"
```

## Level 3 — Data Analysis
1.
```python
def clean_crm(raw):
    d = raw.copy()
    d.columns = d.columns.str.strip().str.lower().str.replace(' ', '_')
    d.drop_duplicates(subset=['email'], inplace=True)
    d['phone'] = d['phone'].str.replace(r'\D', '', regex=True)
    d['email'] = d['email'].str.lower()
    return d
```
2.
```python
def clean_jobs(raw):
    d = raw.copy()
    d['salary'] = pd.to_numeric(d['salary'].str.replace(r'[\$,]', '', regex=True), errors='coerce')
    d['is_remote'] = d['is_remote'].fillna(False).astype(bool)
    return d
```
3.
```python
def clean_sensors(raw):
    d = raw.copy()
    d = d.drop_duplicates(subset=['timestamp'])
    d.loc[d['pressure'] < 0, 'pressure'] = np.nan
    d['pressure'].interpolate(method='linear', inplace=True)
    return d
```
4.
```python
def clean_tx(raw):
    d = raw.copy()
    d['amount'] = pd.to_numeric(d['amount'].str.replace('$', '', regex=False), errors='coerce')
    d['date'] = pd.to_datetime(d['date'])
    return d
```
5.
```python
def validate(df):
    assert df.isna().sum().sum() == 0
    assert df.duplicated().sum() == 0
    assert len(df) > 0
    print("All assertions passed!")
```

## Level 4 — Debugging
1. Convert column to string type first before using `.str`: `df[col].astype(str).str.strip()`.
2. Explicitly create an isolated copy at the start of the function: `df = raw_df.copy()`.
3. Use `regex=False` when replacing literal characters like `$` or `,`: `.str.replace('$', '', regex=False)`.

## Level 5 — AI/ML Application
1.
```python
def pre_ml_clean(raw):
    df = raw.copy()
    df.columns = df.columns.str.strip().str.lower()
    df.drop_duplicates(inplace=True)
    df = df.dropna(subset=['target'])
    num_cols = df.select_dtypes(include=np.number).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    assert df.isna().sum().sum() == 0
    return df
```
2. Outlier removal permanently deletes observations. Removing valid extreme values distorts real-world feature variance necessary for model generalization.
3. Assertions catch data schema drifts, unexpected null spikes, or empty outputs before bad data enters ML training algorithms.

## Level 6 — Interview Questions
1. 1) Structural Audit (`.info()`, `.describe()`), 2) Header Normalization, 3) Deduplication, 4) Type Casting & Format Parsing, 5) Missing Data Handling, 6) Range & Domain Rules, 7) Output Assertions & Logging.
2. Maintain a data dictionary changelog, record before/after record counts, and write modular cleaning functions with docstrings.
3. Data cleaning fixes errors, corruptions, and missingness in raw data. Feature engineering transforms clean data into new predictive mathematical representations for modeling.
4. Assess column domain importance. If non-critical, consider dropping column. If critical, use domain-specific imputation or create an explicit missing indicator feature (`col_is_missing`).
5. Write functional, stateless cleaning pipelines with exception logging, type hinting, unit tests, and validation assertions.
