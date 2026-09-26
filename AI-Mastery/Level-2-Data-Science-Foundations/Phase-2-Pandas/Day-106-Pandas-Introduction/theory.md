# Day 106 Theory: Pandas Introduction

### 1. What Is It?
Pandas is a fast, powerful, and flexible open-source Python library built on top of NumPy, designed specifically for tabular data manipulation and analysis.

### 2. Why Does It Exist?
While NumPy provides fast homogeneous N-dimensional arrays, raw NumPy arrays lack column names, row index labels, automated missing data handling, and mixed-type tabular alignment. Pandas provides labelled 2D tables (`DataFrames`) containing mixed types (floats, ints, strings, datetimes).

### 3. Intuition
If NumPy is a high-performance raw C array grid, Pandas is Microsoft Excel on supercomputers—offering labelled headers, row names, SQL-like merging, and robust data cleaning.

### 4. Syntax
```python
import pandas as pd
import numpy as np

# Creating a basic DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [70000.0, 85000.0, 95000.0]
}
df = pd.DataFrame(data)
```

### 5. Parameters
- `data`: Dictionary, 2D ndarray, Series, or list of records.
- `index`: Index (row labels) override.
- `columns`: Column header labels override.

### 6. How It Works
A Pandas `DataFrame` is an ordered collection of 1D `Series` columns aligned on a common `Index` object. Each column `Series` wraps an underlying contiguous 1D NumPy `ndarray`.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({
    'Metric': ['ROC-AUC', 'Accuracy'],
    'Score': [0.94, 0.88]
})
print("DataFrame Shape:", df.shape)
print("Column Types:
", df.dtypes)
```

### 9. Output Interpretation
`df.shape` returns `(2, 2)` representing 2 rows (metrics) and 2 columns (labels & values). `df.dtypes` shows `object` for strings and `float64` for numerical scores.

### 10. Common Mistakes
- Importing without standard alias `import pandas as pd`.
- Thinking Pandas replaces NumPy (Pandas relies directly on NumPy for numerical computations!).

### 11. Data Science Connection
Exploratory Data Analysis (EDA), feature engineering, data cleaning pipelines, and SQL/database integration.

### 12. AI/ML Connection
Preparing feature matrix $X$ (DataFrame columns) and target label vector $y$ (Series) for Scikit-Learn models (`model.fit(X, y)`).

### 13. Interview Insight
Question: "How does Pandas interface with NumPy internally?"
Answer: Each column in a Pandas DataFrame stores its data as a 1D NumPy `ndarray`. When calling `.values` or `.to_numpy()`, Pandas returns the underlying NumPy memory buffers directly.

### 14. Summary
Pandas brings labelled tabular data structures (`Series` and `DataFrame`) to Python, leveraging NumPy array performance under the hood.
