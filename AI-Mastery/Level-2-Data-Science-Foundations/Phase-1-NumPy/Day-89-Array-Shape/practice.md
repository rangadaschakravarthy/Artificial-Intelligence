# Day 89 Practice Questions: Array Shape

## Level 1 — Basic
1. What data structure type is `arr.shape`?
2. How do you find total number of elements in an array without using `len()`?
3. What happens if you pass `-1` as a dimension to `reshape()`?
4. True or False: Reshaping an array modifies its underlying total size.
5. Can an array have two `-1` dimensions in a single `reshape()` call?

## Level 2 — Coding
6. Create an array of shape `(24,)` and reshape it into a 3D tensor of shape `(2, 3, 4)`.
7. Flatten a 2D matrix of shape `(5, 5)` into a 1D vector using `reshape(-1)`.
8. Given `a = np.ones((3, 4, 5))`, calculate `np.prod(a.shape)` and verify it equals `a.size`.
9. Write a function that checks if two matrices `A` and `B` can be matrix-multiplied based on shape.
10. Transpose a 3D array of shape `(2, 3, 4)` to shape `(4, 3, 2)`.

## Level 3 — Data Analysis
11. If `A` has shape `(10, 4)` and `B` has shape `(4, 2)`, what is the shape of `A @ B`?
12. Given dataset shape `(1000, 30)`, how many samples and how many features are represented?
13. Why does `arr.reshape(3, -1)` fail when `arr.size = 10`?
14. Predict shape of `np.zeros((5, 1, 10)).squeeze()`.
15. Predict shape of `np.array([1, 2, 3]).reshape(-1, 1)`.

## Level 4 — Debugging
16. Fix error: `ValueError: cannot reshape array of size 15 into shape (4,4)`.
17. Fix error: `ValueError: can only specify one unknown dimension`.
18. Fix bug where `A @ B` fails with `ValueError: shapes (5,3) and (5,3) not aligned`.

## Level 5 — AI/ML Application
19. How do you convert a batch of 50 RGB images of size $64 	imes 64$ from `(50, 64, 64, 3)` to flat ML input `(50, 12288)`?
20. Explain why linear layer weights of shape `(In_Features, Out_Features)` require input shape `(Batch, In_Features)`.
21. Connect shape transformation to Convolutional Neural Network flattening layers.

## Level 6 — Interview Questions
22. What is the difference between `ravel()` and `flatten()` regarding shape transformation and memory?
23. How does NumPy compute pointer memory offsets from shape and stride attributes?
24. Demonstrate in-place shape mutation vs view shape returning.
25. Explain the behavior of `transpose()` vs `swapaxes()` on higher-dimensional arrays.
26. How do shape transformation operations affect memory contiguity flags?
