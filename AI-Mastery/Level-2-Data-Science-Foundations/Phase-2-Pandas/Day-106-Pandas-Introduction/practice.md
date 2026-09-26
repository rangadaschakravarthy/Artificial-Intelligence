# Day 106 Practice Questions: Pandas Introduction

## Level 1 — Basic
1. What is the standard alias used to import Pandas?
2. What are the two primary data structures in Pandas?
3. How do you check the version of installed Pandas?
4. True or False: Every column in a Pandas DataFrame has the same data type.
5. What function converts a Pandas DataFrame to a NumPy array?

## Level 2 — Coding
6. Write code to import pandas as `pd` and print its version.
7. Create a DataFrame from a dictionary with columns `'City'` and `'Population'`.
8. Check the number of rows and columns of a DataFrame using `.shape`.
9. Print column names of a DataFrame as a Python list.
10. Check the data types of all columns in a DataFrame using `.dtypes`.

## Level 3 — Data Analysis
11. Why does a Pandas DataFrame allow different data types across columns while NumPy arrays require homogeneous types?
12. Explain the difference between a 1D Pandas Series and a 2D Pandas DataFrame.
13. Predict output shape of `df` created with dictionary containing 4 keys and 10 list elements per key.
14. Predict output: `df = pd.DataFrame({'a': [1, 2]}); print(type(df['a']))`.
15. Explain memory overhead of Pandas DataFrame headers compared to raw NumPy arrays.

## Level 4 — Debugging
16. Fix error: `NameError: name 'pd' is not defined`.
17. Fix error when creating DataFrame from dictionary with mismatched list lengths: `ValueError: All arrays must be of the same length`.
18. Fix issue where DataFrame column data type converted to `object` unexpectedly due to a single string value.

## Level 5 — AI/ML Application
19. How do you extract continuous feature columns as a 2D NumPy float matrix for Scikit-Learn?
20. Why do machine learning pipelines use Pandas DataFrames during EDA and raw NumPy arrays during matrix multiplications?
21. Connect DataFrame columns to feature variables in statistical modeling.

## Level 6 — Interview Questions
22. Explain how Pandas DataFrames store heterogenous data in memory using BlockManager.
23. What is the difference between `df.values` (deprecated) and `df.to_numpy()`?
24. Explain why indexing performance in Pandas differs from raw NumPy indexing.
25. Demonstrate creating a DataFrame from a list of dictionaries vs a dictionary of lists.
26. How does Pandas handle automatic alignment of row index labels during operations?
