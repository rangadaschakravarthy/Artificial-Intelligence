# Day 87 Practice Questions: NumPy Arrays

## Level 1 — Basic
1. What is a 0D array in NumPy called?
2. What property tells you the number of dimensions of an array?
3. How do you create an explicit copy of a NumPy array?
4. What does `np.shares_memory(a, b)` return?
5. How many dimensions does an RGB image tensor have?

## Level 2 — Coding
6. Create a 3D array of shape `(2, 3, 4)` filled with integers from 0 to 23.
7. Check if `b = a[::2]` shares memory with array `a`.
8. Create a 2D float64 array of shape `(4, 2)` and display its strides.
9. Write code to verify if an array is C-contiguous using `.flags`.
10. Construct a 0D scalar array holding value `3.14159` and print its `ndim`.

## Level 3 — Data Analysis
11. Given a 3D array representing 10 audio clips of length 1,000 samples across 2 channels, write down its shape.
12. Explain what happens to memory strides when a 2D matrix of shape `(5, 10)` is transposed to `(10, 5)`.
13. If array `a` has shape `(10, 20)` and dtype `int32`, calculate its row stride in bytes.
14. Explain why slice operations `a[0:5]` are $O(1)$ time complexity operations.
15. Predict output: `a = np.array([1,2,3]); b = a[:]; b[0]=10; print(a[0])`.

## Level 4 — Debugging
16. Fix error: `np.array([ [1, 2], [3, 4, 5] ])` — why does this create a object-dtype array?
17. Fix bug where updating sliced array unintentionally mutates training data.
18. Fix issue where transposing non-contiguous array causes error in C-library calls.

## Level 5 — AI/ML Application
19. How are 4D tensors `(Batch_Size, Channels, Height, Width)` structured for CNN models?
20. Why does zero-copy slicing enable real-time video batch streaming in PyTorch/NumPy pipelines?
21. Connect array strides to matrix transposition efficiency.

## Level 6 — Interview Questions
22. Explain how `ndarray` strides calculate element byte memory addresses.
23. Why does NumPy default to C-contiguous row-major storage ordering?
24. What is the difference between `np.may_share_memory()` and `np.shares_memory()`?
25. How can you force an array view to become C-contiguous in memory?
26. How do memory flags affect performance during Matrix Multiplication?
