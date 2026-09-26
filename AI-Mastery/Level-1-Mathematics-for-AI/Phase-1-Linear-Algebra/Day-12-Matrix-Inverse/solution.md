# Solutions — Matrix Inverse

## Level 1 — Basic Understanding Solutions
### Question 1
1. \det = 3(2) - 1(4) = 2. 

$$
\mathbf{A}^{-1} = \frac{1}{2} \begin{bmatrix} 2 & -1 \\ -4 & 3 \end{bmatrix} = \begin{bmatrix} 1 & -0.5 \\ -2 & 1.5 \end{bmatrix}
$$

.
### Question 2
2. No. $\det = 2(6) - 4(3) = 12 - 12 = 0$. Singular matrices have no inverse.
### Question 3
3. $(\mathbf{A}\mathbf{B})^{-1} = \B^{-1} \mathbf{A}^{-1}$.
### Question 4
4. $(\mathbf{A}^{-1})^{-1} = \mathbf{A}$.
### Question 5
5. $\mathbf{I}_n^{-1} = \mathbf{I}_n$.

## Level 2 — Calculation Solutions
### Question 1
1. 

$$
\mathbf{D}^{-1} = \begin{bmatrix} 1/4 & 0 \\ 0 & -1/2 \end{bmatrix} = \begin{bmatrix} 0.25 & 0 \\ 0 & -0.5 \end{bmatrix}
$$

.
### Question 2
2. 

$$
\mathbf{A}\mathbf{B} = \begin{bmatrix} 2 & 2 \\ 0 & 3 \end{bmatrix}
$$

. \det = 6. 

$$
(\mathbf{A}\mathbf{B})^{-1} = \frac{1}{6} \begin{bmatrix} 3 & -2 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 0.5 & -1/3 \\ 0 & 1/3 \end{bmatrix}
$$

.
### Question 3
3. System 

$$
\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 7 \\ 11 \end{bmatrix}
$$

. \det = 5. Inverse 

$$
= \frac{1}{5} \begin{bmatrix} 3 & -1 \\ -1 & 2 \end{bmatrix}
$$

. Solution 

$$
\begin{bmatrix} x \\ y \end{bmatrix} = \frac{1}{5} \begin{bmatrix} 21-11 \\ -7+22 \end{bmatrix} = \frac{1}{5} \begin{bmatrix} 10 \\ 15 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}
$$

.
### Question 4
4. An orthogonal matrix ($\mathbf{A}^T = \mathbf{A}^{-1} \implies \mathbf{A}^T \mathbf{A} = \mathbf{I}$).
### Question 5
5. $\det(\mathbf{A}^{-1}) = \frac{1}{\det(\mathbf{A})} = \frac{1}{5} = 0.2$.

## Level 3 — Conceptual Solutions
### Question 1
1. Multiply $(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1}) = \mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1} = \mathbf{A}\mathbf{I}\mathbf{A}^{-1} = \mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$. Thus $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$.
### Question 2
2. Transpose identity $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I} \implies (\mathbf{A}\mathbf{A}^{-1})^T = \mathbf{I}^T \implies (\mathbf{A}^{-1})^T \mathbf{A}^T = \mathbf{I}$. Multiply by $(\mathbf{A}^T)^{-1}$ yields $(\mathbf{A}^{-1})^T = (\mathbf{A}^T)^{-1}$.
### Question 3
3. Zero determinant collapses 2D space into a 1D line or point. Multiple original inputs map to the exact same output, making it mathematically impossible to uniquely reverse.
### Question 4
4. Multiply $\mathbf{A}^2 = \mathbf{I}$ by $\mathbf{A}^{-1}$ yields $\mathbf{A}^{-1}\mathbf{A}^2 = \mathbf{A}^{-1}\mathbf{I} \implies \mathbf{A} = \mathbf{A}^{-1}$.
### Question 5
5. Standard Gaussian elimination matrix inversion takes $O(n^3)$ operations.

## Level 4 — AI/ML Application Solutions
### Question 1
1. 

$$
\mathbf{X}^T \mathbf{X} = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}
$$

. \det = 42 - 36 = 6. 

$$
(\mathbf{X}^T \mathbf{X})^{-1} = \frac{1}{6} \begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix}
$$

. 

$$
\mathbf{X}^T \mathbf{y} = \begin{bmatrix} 8.5 \\ 18.5 \end{bmatrix}
$$

. 

$$
\mathbf{w} = \frac{1}{6} \begin{bmatrix} 14(8.5)-6(18.5) \\ -6(8.5)+3(18.5) \end{bmatrix} = \frac{1}{6} \begin{bmatrix} 119-111 \\ -51+55.5 \end{bmatrix} = \frac{1}{6} \begin{bmatrix} 8 \\ 4.5 \end{bmatrix} = \begin{bmatrix} 1.333 \\ 0.75 \end{bmatrix}
$$

.
### Question 2
2. Collinearity makes feature columns linearly dependent, producing $\det(\mathbf{X}^T \mathbf{X}) \approx 0$. Dividing by near-zero yields massive weight values and numerical overflow.
### Question 3
3. Adding $\lambda \mathbf{I}$ pushes all eigenvalues of $\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I}$ strictly above 0 ($\lambda_i + \lambda > 0$), guaranteeing a positive non-zero determinant and stable inverse.

## Level 5 — Interview Questions Solutions
### Question 1
1. Moore-Penrose pseudoinverse $\mathbf{A}^+$ generalizes inversion for any $m \times n$ matrix satisfying 4 conditions: $\mathbf{A}\mathbf{A}^+\mathbf{A}=\mathbf{A}$, $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=\mathbf{A}^+$, $(\mathbf{A}\mathbf{A}^+)^T=\mathbf{A}\mathbf{A}^+$, $(\mathbf{A}^+\mathbf{A})^T=\mathbf{A}^+\mathbf{A}$.
### Question 2
2. For tall full-rank $\mathbf{X}_{m \times n}$ ($m > n$), $\mathbf{X}^T \mathbf{X}$ is $n \times n$ non-singular. Left inverse: $(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{X} = \mathbf{I}_n \implies \mathbf{X}^+ = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T$.
### Question 3
3. Sherman-Morrison-Woodbury formula calculates $(\mathbf{A} + \mathbf{U}\mathbf{C}\mathbf{V})^{-1} = \mathbf{A}^{-1} - \mathbf{A}^{-1}\mathbf{U}(\mathbf{C}^{-1} + \mathbf{V}\mathbf{A}^{-1}\mathbf{U})^{-1}\mathbf{V}\mathbf{A}^{-1}$, computing rank-$k$ updates in $O(k^3)$ instead of $O(n^3)$.
### Question 4
4. Condition number $\kappa(\mathbf{A}) = \frac{\sigma_{max}}{\sigma_{min}}$. Large $\kappa(\mathbf{A})$ means small numerical rounding errors in $\mathbf{b}$ cause massive errors in calculated solution $\mathbf{x}$.
### Question 5
5. LU decomposition factorizes $A = LU$. Solving $Ax=b$ reduces to forward substitution $Ly=Pb$ ($O(n^2)$) and back substitution $Ux=y$ ($O(n^2)$), avoiding expensive $O(n^3)$ explicit inversion.
