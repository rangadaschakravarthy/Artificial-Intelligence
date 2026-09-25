# Examples — Gradients

## Example 1 — Very Easy
2D Bowl Gradient: $f(x, y) = x^2 + y^2 \implies \nabla f = [2x, 2y]^T$. At $(3, 4)$, $\nabla f = [6, 8]^T$.

## Example 2 — Beginner
Linear Model Gradient: $f(x, y) = 3x - 5y + 2 \implies \nabla f = [3, -5]^T$ (Constant vector!).

## Example 3 — Intermediate
MSE Loss Gradient: $L(w_1, w_2) = (w_1 x_1 + w_2 x_2 - y)^2 \implies \nabla_{\mathbf{w}} L = 2(w_1 x_1 + w_2 x_2 - y) [x_1, x_2]^T$.

## Example 4 — AI/ML Example
Steepest Descent Direction: At $(3, 4)$, steepest downhill direction is $-\nabla f = [-6, -8]^T$.

## Example 5 — Real-World Interpretation
Contour Line Orthogonality: Gradient $[6, 8]^T$ dot product with tangent vector $[-8, 6]^T$ equals 0.
