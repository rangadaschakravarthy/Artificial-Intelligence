# Day 164 Theory: Feature Transformation

### 1. What Is It?
Feature Transformation applies mathematical functions ($f(x)$) or binning discretizations to numerical variables to stabilize variance, normalize skewed distributions, or expose linear signals.

### 2. Discretization / Binning
- **`pd.cut()`**: Divides feature range into $N$ equal-width numerical intervals.
- **`pd.qcut()`**: Divides feature values into $N$ equal-frequency quantile bins (each bin contains an equal number of samples).

### 3. Syntax
```python
# Equal-Width Binning:
df['Age_Group'] = pd.cut(df['Age'], bins=3, labels=['Young', 'Middle', 'Senior'])

# Equal-Frequency Quantile Binning:
df['Income_Quartile'] = pd.qcut(df['Income'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
```

### 4. Summary
`pd.cut()` creates equal-width bins, while `pd.qcut()` creates equal-frequency quantile bins for feature discretization.
