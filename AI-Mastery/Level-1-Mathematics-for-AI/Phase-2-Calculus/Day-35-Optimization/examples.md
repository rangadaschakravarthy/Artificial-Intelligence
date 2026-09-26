# Examples — Optimization

## Example 1 — Very Easy
Bowl Minimum: 

$$f(x, y) = x^2 + y^2 \implies \mathbf{H} = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \implies \lambda = [2, 2] > 0$$

 (Minimum).

## Example 2 — Beginner
Peak Maximum: 

$$f(x, y) = -(x^2 + y^2) \implies \mathbf{H} = \begin{bmatrix} -2 & 0 \\ 0 & -2 \end{bmatrix} \implies \lambda = [-2, -2] < 0$$

 (Maximum).

## Example 3 — Intermediate
Saddle Point: 

$$f(x, y) = x^2 - y^2 \implies \mathbf{H} = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix} \implies \lambda = [2, -2]$$

 (Saddle Point).

## Example 4 — AI/ML Example
Monkey Saddle: $f(x, y) = x^3 - 3x y^2$ (Hessian at origin has 0 eigenvalues).

## Example 5 — Real-World Interpretation
Newton-Raphson Step: $\mathbf{x}_{t+1} = \mathbf{x}_t - \mathbf{H}^{-1} \nabla f(\mathbf{x}_t)$.
