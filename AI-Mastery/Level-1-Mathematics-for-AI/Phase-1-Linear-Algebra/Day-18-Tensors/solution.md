# Solutions — Tensors

## Level 1 — Basic Understanding Solutions
### Question 1
1. Scalar = Rank 0, Vector = Rank 1, Matrix = Rank 2.
### Question 2
2. Total elements $= 10 \times 3 \times 32 \times 32 = 30,720$.
### Question 3
3. $B=$ Batch Size, $C=$ Channels, $H=$ Height, $W=$ Width.
### Question 4
4. Yes, because total elements match: $4 \times 6 = 24 = 2 \times 12$.
### Question 5
5. No, because total elements do not match: $4 \times 6 = 24 \neq 25 = 5 \times 5$.

## Level 2 — Calculation Solutions
### Question 1
1. Use `np.transpose(img, (2, 0, 1))` to move channel axis from index 2 to index 0.
### Question 2
2. $N = 3 \times 28 \times 28 = 2352$. Resulting 2D matrix shape is `(32, 2352)`.
### Question 3
3. `X_0 = X[0, :, :, :]` or `X[0]`.
### Question 4
4. Taking mean along axis 0 averages across rows, producing a 1D vector of shape `(50,)`.
### Question 5
5. Adds a new dimension of size 1 at a specified axis position (e.g. shape `(50,)` becomes `(1, 50)`).

## Level 3 — Conceptual Solutions
### Question 1
1. `reshape()` keeps array elements in current memory order and re-indexes dimensions. `permute()` swaps physical axis order, changing memory stride layout.
### Question 2
2. `permute()` makes tensor memory non-contiguous. `.view()` requires C-contiguous memory layout, so `.contiguous()` copies bytes into contiguous RAM.
### Question 3
3. `np.einsum('bik,bkj->bij', A, B)` performs batch matrix multiplication: sums over inner index $k$ for each batch element $b$.
### Question 4
4. 1D bias `(64,)` is aligned to channel dimension (axis 1), stretching across batch (32), height (14), and width (14) automatically.
### Question 5
5. Strides specify byte steps needed to jump 1 position along each axis. Non-unit strides allow slicing zero-copy sub-tensors.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Query tensor shape is `(8, 12, 128, 64)` (Batch=8, Heads=12, Seq_Len=128, Head_Dim=64).
### Question 2
2. Standard MatMul: `np.einsum('ik,kj->ij', A, B)`. Batch MatMul: `np.einsum('bik,bkj->bij', A, B)`.
### Question 3
3. 3D Convolutions slide a 3D kernel filter across Time ($T$), Height ($H$), and Width ($W$) dimensions simultaneously on 5D tensors `(B, C, T, H, W)`.

## Level 5 — Interview Questions Solutions
### Question 1
1. CP Decomposition expresses $3D+$ tensor $\mathcal{X}$ as a sum of rank-1 outer products of vectors: $\mathcal{X} \approx \sum_{r=1}^R \mathbf{a}_r \circ \mathbf{b}_r \circ \mathbf{c}_r$.
### Question 2
2. Tucker Decomposition factorizes a tensor into a small core tensor $\mathcal{G}$ multiplied by factor matrices along each mode: $\mathcal{X} \approx \mathcal{G} \times_1 \mathbf{A} \times_2 \mathbf{B} \times_3 \mathbf{C}$.
### Question 3
3. Tensor Trains (TT) break $D$-dimensional weight tensors into a chain of 3D core tensors $\mathbf{G}_1 \mathbf{G}_2 \dots \mathbf{G}_D$, compressing weight parameters by 90%+ with minimal accuracy loss.
### Question 4
4. Matrix rank is computed in $O(n^3)$ via SVD/Gaussian elimination. Tensor rank for order $\ge 3$ has no closed-form algorithm and is proven NP-hard.
### Question 5
5. NCHW (PyTorch default) optimizes channel-first operations. NHWC (TensorFlow default) improves GPU Tensor Core memory coalescing by keeping RGB pixel channels contiguous in memory.
