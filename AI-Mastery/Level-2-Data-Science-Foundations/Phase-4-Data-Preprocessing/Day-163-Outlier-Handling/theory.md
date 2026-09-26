# Day 163 Theory: Outlier Handling

### 1. What Is It?
Outlier Handling refers to applying corrective transformations (trimming, capping, or imputing) to extreme values to prevent them from distorting statistical models.

### 2. Strategies
1. **Trimming (Dropping)**: Delete rows containing extreme outliers. (Use only when data entry corruption is proven).
2. **Winsorization (Capping)**: Cap extreme values at designated lower and upper percentile boundaries (e.g. 1st and 99th percentiles).
3. **Log Transformation**: Compress long right-tailed distributions mathematically.
4. **Imputation**: Replace extreme outliers with median values.

### 3. Syntax (Percentile Capping)
```python
lower_bound = df['Col'].quantile(0.01)
upper_bound = df['Col'].quantile(0.99)
df['Col_Capped'] = df['Col'].clip(lower=lower_bound, upper=upper_bound)
```

### 4. Summary
Winsorization (`.clip()`) bounds extreme values without reducing dataset sample size.
