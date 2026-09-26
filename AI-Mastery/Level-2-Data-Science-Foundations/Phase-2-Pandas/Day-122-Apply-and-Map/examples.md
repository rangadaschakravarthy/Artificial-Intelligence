# Day 122 Worked Examples: Apply and Map

## Example 1 — Beginner: Series.map with Dictionary
```python
import pandas as pd

gender_series = pd.Series(['M', 'F', 'F', 'M', 'O'])
mapping = {'M': 'Male', 'F': 'Female', 'O': 'Other'}

mapped_series = gender_series.map(mapping)
print("Mapped Gender Series:
", mapped_series)
```

## Example 2 — Practical: DataFrame.apply across Rows (axis=1)
```python
import pandas as pd

df = pd.DataFrame({
    'Exam1': [85, 90, 78],
    'Exam2': [88, 92, 80],
    'Exam3': [90, 85, 82]
})

# Compute weighted average grade per student
df['Final_Grade'] = df.apply(
    lambda r: (r['Exam1'] * 0.3) + (r['Exam2'] * 0.3) + (r['Exam3'] * 0.4),
    axis=1
)
print("DataFrame with Final Grades:
", df)
```

## Example 3 — Intermediate: GroupBy transform for Group Mean Centering
```python
import pandas as pd

df = pd.DataFrame({
    'Dept': ['HR', 'HR', 'IT', 'IT', 'IT'],
    'Salary': [50000, 60000, 90000, 110000, 95000]
})

# Calculate department mean salary broadcasted to original rows
df['Dept_Mean_Salary'] = df.groupby('Dept')['Salary'].transform('mean')
df['Salary_Diff_From_Dept_Mean'] = df['Salary'] - df['Dept_Mean_Salary']
print("Group Centered Salaries:
", df)
```

## Example 4 — Real Dataset: Categorizing Customer Risk Levels
```python
import pandas as pd

customers = pd.DataFrame({
    'Age': [22, 45, 68, 34, 19],
    'Balance': [150, 12000, 45000, 3200, 50]
})

def evaluate_risk(row):
    if row['Age'] < 25 and row['Balance'] < 500:
        return 'High Risk'
    elif row['Balance'] > 10000:
        return 'Low Risk'
    else:
        return 'Moderate Risk'

customers['Risk_Tier'] = customers.apply(evaluate_risk, axis=1)
print("Customer Risk Categorization:
", customers)
```

## Example 5 — AI/ML Application: Group-wise Standardization Preprocessing
```python
import pandas as pd

df_ml = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Feature_Val': [10.0, 12.0, 14.0, 100.0, 200.0, 300.0]
})

# Standardize feature within each category: z = (x - mean) / std
group_mean = df_ml.groupby('Category')['Feature_Val'].transform('mean')
group_std = df_ml.groupby('Category')['Feature_Val'].transform('std')

df_ml['Scaled_Feature'] = (df_ml['Feature_Val'] - group_mean) / group_std
print("Group-Standardized ML Features:
", df_ml)
```
