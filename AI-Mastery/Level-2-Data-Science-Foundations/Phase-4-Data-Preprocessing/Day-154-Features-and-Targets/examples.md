# Day 154 Worked Examples: Features and Targets

## Example 1 — Practical: Auto-Classifying Columns into Feature Types
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, 40, 35], # Continuous/Discrete
    'Education': ['Bachelors', 'PhD', 'Masters'], # Ordinal Categorical
    'City': ['NY', 'SF', 'LA'], # Nominal Categorical
    'Salary': [65000.0, 120000.0, 95000.0] # Target (Regression)
})

X = df.drop(columns=['Salary'])
y = df['Salary']

print("Features X shape:", X.shape)
print("Target y shape:  ", y.shape)
```
