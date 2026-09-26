# Day 92 Practice Questions: Indexing

## Level 1 — Basic
1. What index accesses the first element of a 1D array?
2. What index accesses the last element of an array?
3. How do you access row 2, column 3 in a 2D matrix `m`?
4. True or False: `arr[0][1]` is faster than `arr[0, 1]` in NumPy.
5. What error is raised when indexing past array boundaries?

## Level 2 — Coding
6. Given matrix `m = np.arange(1, 10).reshape(3, 3)`, extract the center value `5`.
7. Change the bottom-right value of `m` to `-1`.
8. Given 3D tensor of shape `(2, 3, 4)`, access the element at index `[0, 2, 3]`.
9. Write code to print the first and last element of 1D array `a` using a single list of indices.
10. Given 2D array `data`, extract element at last row and first column using negative indexing.

## Level 3 — Data Analysis
11. If `matrix` has shape `(5, 5)`, what are valid index ranges for row and column?
12. Explain the difference in execution between `m[1, 2]` and `m[1][2]`.
13. Predict output: `a = np.array([10, 20, 30]); a[-3]`.
14. Predict output: `m = np.ones((2, 2)); m[1, 0] = 5; print(m[1, 1])`.
15. Predict output: `t = np.zeros((2, 2, 2)); print(t[1, 1, 1])`.

## Level 4 — Debugging
16. Fix error: `IndexError: index 3 is out of bounds for axis 0 with size 3`.
17. Fix bug where mutating `arr[0][1] = 99` fails to update original array in custom subclass.
18. Fix syntax error: `matrix[1; 2]` (Why does semicolon fail?).

## Level 5 — AI/ML Application
19. How do you extract single target label $y_i$ from dataset matrix `data[i, -1]`?
20. In reinforcement learning, how to access current state Q-value `Q_table[state_idx, action_idx]`?
21. Connect multi-axis indexing to pixel retrieval in image processing.

## Level 6 — Interview Questions
22. How does stride arithmetic execute `arr[i, j]` pointer calculation in C?
23. Why is integer indexing returning a scalar/array copy while slicing returns a view?
24. Explain index out of bounds checking in NumPy vs raw C pointers.
25. Demonstrate multi-dimensional tuple indexing programmatically: `idx = (1, 2); arr[idx]`.
26. How does memory layout affect cache efficiency during row vs column indexing loops?
