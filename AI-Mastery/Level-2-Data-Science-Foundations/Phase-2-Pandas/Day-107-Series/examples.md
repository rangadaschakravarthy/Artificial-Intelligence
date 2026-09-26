# Day 107 Worked Examples: Series

## Example 1 — Beginner: Creating Series from Dict & List
```python
import pandas as pd

# From List
s_list = pd.Series([10, 20, 30], index=['Row1', 'Row2', 'Row3'], name='Scores')

# From Dictionary (Keys become Index labels)
pop_dict = {'New York': 8400000, 'Los Angeles': 3900000, 'Chicago': 2700000}
s_pop = pd.Series(pop_dict, name='Population')

print("List Series:
", s_list)
print("
Population Series:
", s_pop)
```

## Example 2 — Practical: Label Alignment Feature Demo
```python
import pandas as pd

# Q1 Sales
q1 = pd.Series({'Store_A': 100, 'Store_B': 150, 'Store_C': 200})

# Q2 Sales (Store_A missing, Store_D added)
q2 = pd.Series({'Store_B': 180, 'Store_C': 220, 'Store_D': 90})

# Total Sales with Automatic Index Alignment
total_sales = q1 + q2
print("Total Sales (Auto-aligned):
", total_sales)
```

## Example 3 — Intermediate: Categorical Exploration Methods
```python
import pandas as pd

colors = pd.Series(['Red', 'Blue', 'Red', 'Green', 'Blue', 'Red', 'Yellow'])

print("Unique Colors:", colors.unique())
print("Number of Unique Colors:", colors.nunique())
print("
Value Counts (Frequencies):
", colors.value_counts())
print("
Normalized Percentages:
", colors.value_counts(normalize=True))
```

## Example 4 — Real Dataset: Summary Statistics of Feature Series
```python
import pandas as pd

# Customer Age Feature
ages = pd.Series([22, 25, 30, 35, 40, 45, 50, 85], name='Age')

print("Summary Statistics:
", ages.describe())
print("50th Percentile (Median):", ages.median())
print("Interquartile Range (IQR):", ages.quantile(0.75) - ages.quantile(0.25))
```

## Example 5 — AI/ML Application: Checking Class Balance of Target Series
```python
import pandas as pd

# Target Label Series (0 = Fraud, 1 = Legitimate)
y_target = pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 0, 1], name='Is_Legit')

class_proportions = y_target.value_counts(normalize=True) * 100

print("Target Class Proportions (%):
", class_proportions)

if class_proportions.min() < 20.0:
    print("
Warning: Class Imbalance Detected! Consider Resampling.")
```
