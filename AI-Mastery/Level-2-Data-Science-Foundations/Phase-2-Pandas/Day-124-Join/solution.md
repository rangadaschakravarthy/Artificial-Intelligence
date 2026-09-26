# Day 124 Solutions: Join

## Level 1 — Basic
1. Row indices (index labels).
2. `how='left'`.
3. Pass `lsuffix` and/or `rsuffix` arguments (e.g. `lsuffix='_left', rsuffix='_right'`).
4. `df1.join(df2, on='User_ID')`.
5. True. `df1.join([df2, df3, df4])` is valid syntax.

## Level 2 — Coding
1.
```python
import pandas as pd
res = df1.join(df2, how='inner')
```
2.
```python
res = df1.join(df2, lsuffix='_2022', rsuffix='_2023')
```
3.
```python
res = df1.join(df2.set_index('ID'))
```
4.
```python
res = df_a.join([df_b, df_c], how='inner')
```
5.
```python
res = df1.join(df2, how='right')
```

## Level 3 — Data Analysis
1.
```python
regional_sales = north.join([south, east, west], how='outer')
print(regional_sales)
```
2.
```python
patient_record = demo_df.set_index('PatientID').join(labs_df.set_index('PatientID'), how='left')
```
3.
```python
financials = balance_sheet.join(income_stmt, how='inner')
```
4.
```python
telemetry = temp_sensor.join([pressure_sensor, vibration_sensor], how='outer')
```
5.
```python
customer_360 = demog.join([risk_scores, activity_metrics], how='left')
```

## Level 4 — Debugging
1. Specify `lsuffix` and `rsuffix`: `df1.join(df2, lsuffix='_l', rsuffix='_r')`.
2. Ensure both indices share exact data types: `df2.index = df2.index.astype(df1.index.dtype)`.
3. Verify that `on='Key'` specifies a column present in `df1` (the caller), matching `df2`'s index labels.

## Level 5 — AI/ML Application
1.
```python
X_master = feat_pipeline1.join([feat_pipeline2, feat_pipeline3], how='inner')
```
2. `.join()` explicitly verifies and aligns matching index IDs, preventing subtle feature alignment bugs caused by silent row order variations in positional concat.
3. Index joining enforces explicit entity ID matching, ensuring target label `y_i` is attached to correct feature row `X_i`.

## Level 6 — Interview Questions
1. Use `df.join()` when DataFrames already use meaningful row indices (like dates or primary entity IDs), or when joining more than two DataFrames simultaneously.
2. If index labels contain duplicates, Pandas computes the Cartesian product for those duplicate index groups.
3. $O(N + M)$ time complexity because Pandas uses fast hash map lookup over index arrays.
4. Set key columns as row indices first using `.set_index('KeyCol')`, then invoke `.join()`.
5. `.join()` matches level names or positional levels across MultiIndex hierarchies.
