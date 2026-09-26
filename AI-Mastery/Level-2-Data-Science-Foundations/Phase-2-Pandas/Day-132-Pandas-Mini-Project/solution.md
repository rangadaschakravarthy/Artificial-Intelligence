# Day 132 Solutions: Pandas Mini Project

## Level 1 — Basic
1. 1) Raw Ingestion & Audit, 2) Data Cleaning, 3) EDA, 4) Business Reporting, 5) ML Preprocessing, 6) Validation & Export.
2. `assert df.isna().sum().sum() == 0`, `assert df.duplicated().sum() == 0`, `assert len(df) > 0`.
3. `df['Date'].dt.to_period('M')`.
4. `df.to_csv('output.csv', index=False)`.
5. True. Dirty data and corrupt dtypes prevent accurate statistical correlation calculation.

## Level 2 — Coding
1.
```python
init_cnt = len(df)
df.drop_duplicates(inplace=True)
print(f"Removed {init_cnt - len(df)} duplicate rows.")
```
2.
```python
df['Amount'] = pd.to_numeric(df['Amount'].str.replace('$', '', regex=False).str.replace(',', '', regex=False), errors='coerce')
```
3.
```python
piv = df.pivot_table(index=df['Date'].dt.to_period('M'), columns='ProductLine', values='Sales', aggfunc='sum', fill_value=0)
```
4.
```python
y = (df['Spend'] > 500).astype(int)
X = pd.get_dummies(df.drop(columns=['Spend']), drop_first=True, dtype=int)
```
5.
```python
assert X.isna().sum().sum() == 0, "Nulls remain!"
assert X.select_dtypes(include='object').shape[1] == 0, "Objects remain!"
```

## Level 3 — Data Analysis
1.
```python
top5 = df.groupby('CustomerSegment')['Revenue'].sum().nlargest(5)
print(top5)
```
2.
```python
monthly_trend = df.resample('M', on='Date')['Sales'].sum()
print(monthly_trend)
```
3.
```python
ltv_summary = df.groupby('Channel').agg(Total_Rev=('Spend', 'sum'), Avg_Orders=('OrderID', 'count'))
print(ltv_summary)
```
4.
```python
corr = X.corr().abs()
high_corr = (corr > 0.85) & (corr != 1.0)
print(high_corr.sum())
```
5. Executive recommendations: 1) Focus marketing budget on top-performing acquisition channels, 2) Target high-value customer cohorts, 3) Resolve churn spike during month 3, 4) Deploy automated churn ML model.

## Level 4 — Debugging
1. Convert column to datetime first: `df['Date'] = pd.to_datetime(df['Date'])` before `.dt.to_period('M')`.
2. Reindex `X_test` columns against `X_train.columns`: `X_test = X_test.reindex(columns=X_train.columns, fill_value=0)`.
3. Process data in chunks or convert string categories to Categorical dtypes (`df['cat'] = df['cat'].astype('category')`).

## Level 5 — AI/ML Application
1.
```python
def execute_project(raw_path):
    raw = pd.read_csv(raw_path)
    # Stage 2 Clean
    df = clean(raw)
    # Stage 5 Pre-ML
    X, y = prepare_ml(df)
    # Stage 6 Assert
    assert X.isna().sum().sum() == 0
    return X, y
```
2. Structuring pipeline stages into pure python functions makes them directly importable into orchestration tools (Airflow, Dagster, Prefect).
3. `assert X.shape[0] == y.shape[0]`, `assert X.isna().sum().sum() == 0`.

## Level 6 — Interview Questions
1. Structure answer into 6 stages: Problem definition -> Data Ingestion -> Cleaning decisions -> EDA discoveries -> Business reporting insights -> ML matrix preparation.
2. Explain domain-based decisions: Dropped records with missing primary keys, imputed numeric features with median (robust to outliers), created missing indicator flags for informative missingness.
3. Transition from Pandas to PySpark DataFrames or Dask DataFrames, which mirror Pandas APIs while executing distributed parallel computations across cluster nodes.
4. Connect data findings directly to ROI, revenue growth, customer retention, and operational efficiency improvements.
5. Use `pytest` framework with synthetic mock DataFrames, asserting pipeline output schema, row counts, and data types.
