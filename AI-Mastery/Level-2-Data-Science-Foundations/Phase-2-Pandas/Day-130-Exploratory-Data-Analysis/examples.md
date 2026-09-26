# Day 130 Worked Examples: Exploratory Data Analysis

## Example 1 — Beginner: Univariate Analysis of Continuous & Categorical Data
```python
import pandas as pd

df = pd.DataFrame({
    'Age': [22, 25, 29, 34, 45, 50, 85],
    'Department': ['IT', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'IT']
})

# Numerical Univariate Metrics
print("Age Summary Statistics:
", df['Age'].describe())
print("Age Skewness:", df['Age'].skew())

# Categorical Univariate Metrics
print("
Department Frequency Proportions:
", df['Department'].value_counts(normalize=True))
```

## Example 2 — Practical: Bivariate Correlation Analysis
```python
import pandas as pd

df = pd.DataFrame({
    'Experience_Yrs': [1, 3, 5, 7, 10],
    'Salary': [50000, 65000, 85000, 105000, 140000],
    'Commute_Min': [45, 20, 35, 15, 50]
})

# Compute Pearson Correlation Matrix
corr = df.corr()
print("Pearson Correlation Matrix:
", corr)
print("
Correlation with Salary:
", corr['Salary'].sort_values(ascending=False))
```

## Example 3 — Intermediate: Bivariate Group Comparison (Categorical vs Numerical)
```python
import pandas as pd

df = pd.DataFrame({
    'Plan_Type': ['Basic', 'Basic', 'Premium', 'Premium', 'Basic', 'Premium'],
    'Monthly_Spend': [29.99, 35.00, 89.99, 120.00, 25.00, 95.00],
    'Support_Calls': [4, 5, 1, 0, 6, 2]
})

group_summary = df.groupby('Plan_Type').agg(
    Avg_Spend=('Monthly_Spend', 'mean'),
    Std_Spend=('Monthly_Spend', 'std'),
    Avg_Calls=('Support_Calls', 'mean')
)
print("Plan Type Bivariate Group Summary:
", group_summary)
```

## Example 4 — Real Dataset: Housing Price Feature EDA
```python
import pandas as pd

housing = pd.DataFrame({
    'Bedrooms': [2, 3, 3, 4, 5],
    'SqFt': [1200, 1800, 2100, 2800, 3500],
    'Age_Yrs': [30, 15, 20, 5, 2],
    'Price': [250000, 380000, 420000, 590000, 850000]
})

print("Housing Feature Correlation Matrix:
", housing.corr()['Price'])
```

## Example 5 — AI/ML Application: Detecting Collinearity for Feature Selection
```python
import pandas as pd

# Feature Matrix containing highly collinear features (Temp_C and Temp_F)
features = pd.DataFrame({
    'Temp_C': [20, 25, 30, 35],
    'Temp_F': [68, 77, 86, 95],
    'Humidity': [50, 55, 60, 65],
    'Energy_Demand': [100, 130, 170, 210]
})

corr_matrix = features.corr()
print("Correlation Matrix:
", corr_matrix)

# Identify features with correlation > 0.95 (collinear pairs)
high_corr = (corr_matrix.abs() > 0.95) & (corr_matrix != 1.0)
print("
High Collinearity Detected (>0.95):
", high_corr)
```
