# Practice Exercises — Tensors

## Level 1 — Basic Understanding
1. What is the rank (order) of a scalar, vector, and matrix?
2. What is the total number of elements in a tensor of shape `(10, 3, 32, 32)`?
3. What does PyTorch `(B, C, H, W)` stand for?
4. Can you reshape a tensor of shape `(4, 6)` into shape `(2, 12)`? Why?
5. Can you reshape a tensor of shape `(4, 6)` into shape `(5, 5)`? Why?

## Level 2 — Calculation
1. Convert an RGB image tensor of shape `(228, 228, 3)` (TensorFlow format) to PyTorch format `(3, 228, 228)` using NumPy `transpose`.
2. Flatten a 4D batch tensor of shape `(32, 3, 28, 28)` into a 2D matrix of shape `(32, N)`. What is $N$?
3. Extract the 1st image from a batch tensor `X` of shape `(10, 3, 64, 64)` using NumPy slicing.
4. Compute the mean across axis 0 of a tensor of shape `(100, 50)`. What is the resulting shape?
5. Explain what `np.expand_dims()` or PyTorch `unsqueeze()` does.

## Level 3 — Conceptual
1. Explain the difference between `reshape()` (which preserves total element count) and `transpose()` / `permute()` (which swaps axes).
2. Why does PyTorch require calling `.contiguous()` after `.permute()` before calling `.view()`?
3. Explain tensor contraction (Einstein Summation `einsum`) notation `np.einsum('bik,bkj->bij', A, B)`.
4. How does broadcasting operate on a 4D tensor `(32, 64, 14, 14)` and a 1D bias `(64,)`?
5. What is tensor slicing and how does stride affect memory layout?

## Level 4 — AI/ML Application
1. In a Multi-Head Attention layer with batch size 8, sequence length 128, 12 attention heads, and head dimension 64, state the shape of the 4D Query tensor.
2. Write the Einstein Summation (`einsum`) expression for matrix multiplication $\mathbf{C} = \mathbf{A}\mathbf{B}$ and batch matrix multiplication.
3. Explain how Video 3D Convolutions operate on 5D tensors `(B, C, T, H, W)`.

## Level 5 — Interview Questions
1. What is CP (Candecomp/Parafac) Tensor Decomposition? How does it generalize SVD to 3D+ tensors?
2. What is Tucker Decomposition (Higher-Order SVD - HOSVD)?
3. Explain Tensor Networks (e.g. Matrix Product States - MPS / Tensor Trains) for compressing deep neural network weight tensors.
4. Why is computing exact Tensor Rank for order $\ge 3$ tensors NP-hard, unlike matrix rank?
5. How does memory layout (NCHW vs NHWC) affect GPU CUDA Memory Coalescing and Tensor Core performance?
