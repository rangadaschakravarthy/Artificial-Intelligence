# Examples — Jacobians

## Example 1 — Very Easy
Polar Coordinate Transformation: 

$$
x = r \cos(\theta), y = r \sin(\theta) \implies \mathbf{J} = \begin{bmatrix} \cos(\theta) & -r \sin(\theta) \\ \sin(\theta) & r \cos(\theta) \end{bmatrix}
$$

. Determinant = r.

## Example 2 — Beginner
2D to 2D Jacobian: 

$$
\mathbf{f}(x, y) = [x^2, xy]^T \implies \mathbf{J} = \begin{bmatrix} 2x & 0 \\ y & x \end{bmatrix}
$$

.

## Example 3 — Intermediate
Linear Map Jacobian: $\mathbf{f}(\mathbf{x}) = \mathbf{W}\mathbf{x} \implies \mathbf{J} = \mathbf{W}$.

## Example 4 — AI/ML Example
Triangular Coupling Layer: RealNVP architecture triangular Jacobian.

## Example 5 — Real-World Interpretation
PyTorch Jacobian Computation: Using `torch.autograd.functional.jacobian()`.
