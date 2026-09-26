# Examples — Projections

## Example 1 — Very Easy
Projection onto x-axis: $\mathbf{v} = [4, 7]^T \implies \text{proj} = [4, 0]^T$.

## Example 2 — Beginner
Projection Matrix 2D: Projection onto line y = x spanned by 

$$
\mathbf{u} = [1, 1]^T \implies \mathbf{P} = \begin{bmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{bmatrix}
$$

.

## Example 3 — Intermediate
Idempotence Check: 

$$
\mathbf{P}^2 = \begin{bmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{bmatrix} = \begin{bmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{bmatrix} = \mathbf{P}
$$

.

## Example 4 — AI/ML Example
Residual Error Orthogonality: $\mathbf{e} = \mathbf{v} - \mathbf{P}\mathbf{v} \implies \mathbf{e} \cdot \mathbf{u} = 0$.

## Example 5 — Real-World Interpretation
OLS Regression Geometric View: $\hat{\mathbf{y}} = \mathbf{P}_{X} \mathbf{y}$ projecting target label vector.
