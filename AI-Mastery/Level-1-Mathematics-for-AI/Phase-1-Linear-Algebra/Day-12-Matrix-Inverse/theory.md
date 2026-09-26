# Theory — Matrix Inverse

### 1. Simple Definition
The inverse of a matrix $\mathbf{A}$ (written $\mathbf{A}^{-1}$) is the matrix that 'undoes' the transformation performed by $\mathbf{A}$. Multiplying $\mathbf{A}$ by its inverse yields the identity matrix $\mathbf{I}$.

### 2. Intuition
Just as dividing by 5 undoes multiplying by 5 ($5 \times 5^{-1} = 1$), multiplying by $\mathbf{A}^{-1}$ undoes the transformation of $\mathbf{A}$. If $\mathbf{A}$ scales 2D space by 2, $\mathbf{A}^{-1}$ shrinks it back by 1/2.

### 3. Mathematical Definition
A square matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$ is invertible (non-singular) if there exists a matrix $\mathbf{A}^{-1} \in \mathbb{R}^{n \times n}$ such that:

$$
\mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}_n
$$

Matrix $\mathbf{A}$ is invertible if and only if $\det(\mathbf{A}) \neq 0$.

### 4. Notation
$\mathbf{A}^{-1}$. Non-square matrices do NOT have standard inverses (they use pseudoinverses).

### 5. Formula

$$
\text{For } \mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies \mathbf{A}^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix} \quad \text{provided } ad-bc \neq 0
$$

### 6. Symbol-by-Symbol Explanation
- $ad - bc$: Determinant of $2 \times 2$ matrix $\mathbf{A}$
- $d, -b, -c, a$: Adjugate matrix entries

### 7. Step-by-Step Calculation
Invert 

$$
\mathbf{A} = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}
$$

:
1. Determinant: $ad - bc = (4)(6) - (7)(2) = 24 - 14 = 10 \neq 0$.
2. Swap a,d and negate b,c: 

$$
\begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix}
$$

.
3. Divide by determinant: 

$$
\mathbf{A}^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix}
$$

.
4. Check: 

$$
\mathbf{A}\mathbf{A}^{-1} = \begin{bmatrix} 4(0.6)+7(-0.2) & 4(-0.7)+7(0.4) \\ 2(0.6)+6(-0.2) & 2(-0.7)+6(0.4) \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

.

### 8. Second Example
Non-invertible singular matrix example: 

$$
\mathbf{B} = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}
$$

. Determinant = 1(4) - 2(2) = 0. Inverse does not exist (division by zero)!

### 9. Common Mistakes
Inverting element-wise ($1/a_{i,j}$); trying to invert non-square matrices; applying inverse when determinant is zero.

### 10. AI Connection
Linear Regression OLS closed-form solution: $\hat{\mathbf{w}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$. Linear system solvers in Kalman filters and Gaussian Processes.

### 11. Algorithm Connection
Ordinary Least Squares (OLS), Ridge Regression, Linear Discriminant Analysis (LDA), Newton-Raphson Optimization.

### 12. Practical Interpretation
A singular matrix squashes $n$-dimensional space into a lower dimension (e.g. 2D plane into a 1D line), losing information permanently so it cannot be undone.

### 13. Interview Insight
Q: 'Why should you use `np.linalg.solve(A, b)` instead of `np.linalg.inv(A) @ b` in Python?' A: Direct inversion is computationally slower ($O(n^3)$ with larger constants) and suffers from severe numerical instability/floating-point inaccuracy compared to LU decomposition solving.

### 14. Summary
Matrix inverse $\mathbf{A}^{-1}$ satisfies $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$. Exists only for square matrices with non-zero determinant. Product inverse flips order: $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$.
