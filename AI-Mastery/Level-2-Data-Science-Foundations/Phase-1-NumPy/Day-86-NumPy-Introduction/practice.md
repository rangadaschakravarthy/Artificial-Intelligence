# Day 86 Practice Questions: NumPy Introduction

## Level 1 — Basic
1. What does the acronym NumPy stand for?
2. What is the fundamental data structure provided by NumPy?
3. How do you import NumPy using standard community convention?
4. True or False: Python lists store elements in contiguous RAM blocks.
5. What happens when you create an array with `np.array([1, 2.5, 3])`?

## Level 2 — Coding
6. Write code to create a 1D NumPy array containing numbers 5 through 15.
7. Create a 2D array of shape (3, 3) filled with floating point numbers 1.0 to 9.0.
8. Print the `ndim`, `shape`, `dtype`, and `nbytes` of array `np.array([[10, 20], [30, 40]])`.
9. Convert a Python list of strings `['1.5', '2.5', '3.5']` into a float NumPy array.
10. Check the version of your installed NumPy library using code.

## Level 3 — Data Analysis
11. You are given feature vector `x = np.array([100, 200, 300])`. Convert this vector to represent values scaled down by a factor of 100.
12. Given a 2D matrix of shape `(100, 10)`, how many total data points (size) are stored?
13. If an array has `dtype=np.float64` and `size=1000`, how many bytes of memory does it consume?
14. Inspect why `np.array([True, 1, 3.14])` produces array of floats.
15. Compare memory usage between a Python list of 1,000 integers and a NumPy int64 array.

## Level 4 — Debugging
16. Fix error: `import numpy; a = np.array([1,2])`.
17. Fix type error: `a = np.array([1, 2, 3]); a.shape()` (Why does calling `.shape()` fail?).
18. Fix issue where `np.array([1, 2, '3']) + 5` throws `TypeError`.

## Level 5 — AI/ML Application
19. How is a 2D NumPy array used to represent a dataset with 500 patient records and 20 medical lab test features?
20. Why do Deep Learning frameworks require arrays to have homogenous data types?
21. Explain how continuous memory layout accelerates matrix multiplication $C = A \cdot B$ in Linear Algebra.

## Level 6 — Interview Questions
22. Explain the role of strides in a NumPy ndarray.
23. What is type coercion/upcasting in NumPy array initialization?
24. How does NumPy bypass Python's Global Interpreter Lock (GIL)?
25. Explain the difference between C-contiguous and Fortran-contiguous array layout.
26. When would a Python list be preferred over a NumPy array?
