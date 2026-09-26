# Practice Exercises — Matrix Inverse

## Level 1 — Basic Understanding
1. Calculate the inverse of 

$$\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 4 & 2 \end{bmatrix}$$

.
2. Is matrix 

$$\mathbf{B} = \begin{bmatrix} 2 & 4 \\ 3 & 6 \end{bmatrix}$$

 invertible? Explain why.
3. State the formula for $(\mathbf{A}\mathbf{B})^{-1}$.
4. What is $(\mathbf{A}^{-1})^{-1}$?
5. What is the inverse of identity matrix $\mathbf{I}_n$?

## Level 2 — Calculation
1. Find the inverse of diagonal matrix 

$$\mathbf{D} = \begin{bmatrix} 4 & 0 \\ 0 & -2 \end{bmatrix}$$

.
2. Given 

$$\mathbf{A} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$$

 and 

$$\mathbf{B} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$

, compute (\mathbf{A}\mathbf{B})^{-1}.
3. Solve the system of equations using matrix inverse: $2x + y = 7, \, x + 3y = 11$.
4. If $\mathbf{A}^T = \mathbf{A}^{-1}$, what special type of matrix is $\mathbf{A}$?
5. Compute the determinant of $\mathbf{A}^{-1}$ if $\det(\mathbf{A}) = 5$.

## Level 3 — Conceptual
1. Prove that $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$ for invertible square matrices.
2. Prove that $(\mathbf{A}^T)^{-1} = (\mathbf{A}^{-1})^T$.
3. Explain geometrically why a matrix with zero determinant cannot be inverted.
4. Show that if $\mathbf{A}^2 = \mathbf{I}$, then $\mathbf{A}^{-1} = \mathbf{A}$.
5. What is the computational complexity of $n \times n$ matrix inversion using Gaussian Elimination?

## Level 4 — AI/ML Application
1. In Linear Regression, given dataset feature matrix 

$$\mathbf{X} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}$$

 and targets 

$$\mathbf{y} = \begin{bmatrix} 2 \\ 3 \\ 3.5 \end{bmatrix}$$

, compute \mathbf{X}^T \mathbf{X}, (\mathbf{X}^T \mathbf{X})^{-1}, and parameter vector \mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}.
2. Why does collinearity (multicollinearity) between features cause $(\mathbf{X}^T \mathbf{X})^{-1}$ to fail or produce wildly unstable weights?
3. Explain how Ridge Regularization $\lambda \mathbf{I}$ guarantees that $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})$ is invertible.

## Level 5 — Interview Questions
1. What is the Moore-Penrose Pseudoinverse $\mathbf{A}^+$? How does it extend matrix inversion to non-square $m \times n$ matrices?
2. Derive the pseudoinverse formula $\mathbf{A}^+ = (\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$ for tall matrices with full column rank.
3. Explain the Sherman-Morrison-Woodbury formula for updating matrix inverse after low-rank updates.
4. Why is condition number $\kappa(\mathbf{A}) = ||\mathbf{A}|| ||\mathbf{A}^{-1}||$ critical for evaluating matrix ill-conditioning?
5. How does LU Decomposition ($PA = LU$) avoid computing explicit matrix inverse when solving linear systems?
