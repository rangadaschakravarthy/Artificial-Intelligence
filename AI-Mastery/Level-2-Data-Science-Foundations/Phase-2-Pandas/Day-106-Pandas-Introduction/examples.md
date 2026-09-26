# Day 106 Worked Examples: Pandas Introduction

## Example 1 — Beginner: Creating First DataFrame
```python
import pandas as pd

# Creating a simple student dataset
student_dict = {
    'Student_ID': [101, 102, 103],
    'Name': ['Eva', 'Liam', 'Sophia'],
    'Score': [88.5, 92.0, 79.5]
}

df = pd.DataFrame(student_dict)
print("Student DataFrame:
", df)
print("Type:", type(df))
```

## Example 2 — Practical: Inspecting Underlying NumPy Arrays
```python
import pandas as pd

df = pd.DataFrame({
    'Feature_1': [1.0, 2.0, 3.0],
    'Feature_2': [10, 20, 30]
})

# Convert DataFrame columns to raw NumPy array
numpy_array = df.to_numpy()

print("Pandas DataFrame:
", df)
print("Underlying NumPy Array:
", numpy_array)
print("NumPy Array Type:", type(numpy_array))
```

## Example 3 — Intermediate: Inspecting Basic DataFrame Properties
```python
import pandas as pd

df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Monitor'],
    'Price': [1200.0, 25.5, 300.0],
    'In_Stock': [True, True, False]
})

print("Shape (rows, cols):", df.shape)
print("Total Size:", df.size)
print("Columns:", df.columns.tolist())
print("Data Types:
", df.dtypes)
```

## Example 4 — Real Dataset: Representing Customer Records
```python
import pandas as pd

customers = pd.DataFrame({
    'CustomerID': ['C01', 'C02', 'C03', 'C04'],
    'Age': [28, 42, 35, 50],
    'Annual_Income': [65000, 120000, 85000, 95000],
    'Purchased': [True, False, True, True]
})

print("Customer DataFrame:
", customers)
print("
Summary Info:")
customers.info()
```

## Example 5 — AI/ML Application: Feature Matrix X and Target Y Separation
```python
import pandas as pd

# Housing Dataset
housing = pd.DataFrame({
    'Square_Feet': [1500, 2000, 1200, 1800],
    'Bedrooms': [3, 4, 2, 3],
    'Age_Years': [10, 5, 20, 8],
    'Price_USD': [350000, 480000, 280000, 410000]
})

# Separate Feature Matrix X and Target Vector y
X = housing[['Square_Feet', 'Bedrooms', 'Age_Years']] # DataFrame (2D)
y = housing['Price_USD']                            # Series (1D)

print("Feature Matrix X shape:", X.shape)
print("Target Label y shape:  ", y.shape)
```
