# Examples — Matrix Inverse

## Example 1 — Very Easy
2x2 Inverse: 

$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}^{-1} = \frac{1}{-2} \begin{bmatrix} 4 & -2 \\ -3 & 1 \end{bmatrix} = \begin{bmatrix} -2 & 1 \\ 1.5 & -0.5 \end{bmatrix}$$

.

## Example 2 — Beginner
Diagonal Matrix Inverse: $\text{diag}(2, 5, 10)^{-1} = \text{diag}(1/2, 1/5, 1/10)$.

## Example 3 — Intermediate
Singular Matrix: 

$$\begin{bmatrix} 2 & 6 \\ 1 & 3 \end{bmatrix} \implies \det = 6 - 6 = 0 \implies$$

 Non-invertible!

## Example 4 — AI/ML Example
Solving System \mathbf{A}\mathbf{x} = \mathbf{b}: 

$$\begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 5 \\ 3 \end{bmatrix} \implies \mathbf{x} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 5 \\ 3 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

.

## Example 5 — Real-World Interpretation
Linear Regression OLS Normal Equation parameter estimation.
