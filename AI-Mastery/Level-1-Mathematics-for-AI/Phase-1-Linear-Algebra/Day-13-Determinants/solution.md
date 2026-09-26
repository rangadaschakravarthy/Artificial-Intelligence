# Solutions — Determinants

## Level 1 — Basic Understanding Solutions
### Question 1
1. $\det = 4(5) - 2(1) = 20 - 2 = 18$.
### Question 2
2. $\det = 6(2) - 3(4) = 12 - 12 = 0$. Since $\det = 0$, $\mathbf{B}$ is singular and non-invertible.
### Question 3
3. $\det(\mathbf{I}_n) = 1$.
### Question 4
4. $\det(\mathbf{A}^{-1}) = \frac{1}{\det(\mathbf{A})} = \frac{1}{4} = 0.25$.
### Question 5
5. No. Determinants exist ONLY for square matrices ($n \times n$).

## Level 2 — Calculation Solutions
### Question 1
1. Expand along top row: $2(1\cdot 1 - 2\cdot 4) - 0 + 1(3\cdot 4 - 1\cdot 0) = 2(1 - 8) + 1(12) = 2(-7) + 12 = -14 + 12 = -2$.
### Question 2
2. $\det = 3k - 8 = 10 \implies 3k = 18 \implies k = 6$.
### Question 3
3. Scaling a $2 \times 2$ matrix by scalar 3 multiplies every row by 3: $\det(3\mathbf{A}) = 3^2 \det(\mathbf{A}) = 9 \times 5 = 45$.
### Question 4
4. General formula: $\det(c\mathbf{A}) = c^n \det(\mathbf{A})$ for $n \times n$ matrix.
### Question 5
5. 

$$\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies \det(\mathbf{A}) = ad - bc$$

. 

$$\mathbf{A}^T = \begin{bmatrix} a & c \\ b & d \end{bmatrix} \implies \det(\mathbf{A}^T) = ad - cb = ad - bc$$

. Equal!

## Level 3 — Conceptual Solutions
### Question 1
1. Swapping 2 rows negates $\det$ ($-\det$). Multiplying row by $c$ scales $\det$ ($c \det$). Adding row multiple leaves $\det$ UNCHANGED.
### Question 2
2. Swapping the two identical rows flips sign ($\det = -\det$), which forces $\det = 0$.
### Question 3
3. Upper/Lower triangular matrix elimination reduces cofactor expansion along first column/row recursively to product of main diagonal elements $\prod_{i=1}^n a_{i,i}$.
### Question 4
4. $\mathbf{Q}^T \mathbf{Q} = \mathbf{I} \implies \det(\mathbf{Q}^T \mathbf{Q}) = \det(\mathbf{I}) = 1 \implies \det(\mathbf{Q}^T)\det(\mathbf{Q}) = 1 \implies (\det(\mathbf{Q}))^2 = 1 \implies \det(\mathbf{Q}) = \pm 1$.
### Question 5
5. The unit hypercube spanned by standard basis vectors has volume 1. Transformed vectors span a parallelotope whose $n$-dimensional volume equals $|\det(\mathbf{A})|$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Change of variables density formula $p_X(x) = p_Z(z) / |\det(A)| = p_Z(z) / 0.5 = 2 p_Z(z)$. Density doubles because volume shrunk by half.
### Question 2
2. Area scaling factor $= \det(\mathbf{S}) = 2 \times 3 - 0 = 6$. Transformed region area is 6 times larger.
### Question 3
3. Eigenvalue problem $\mathbf{A}\mathbf{x} = \lambda \mathbf{x} \implies (\mathbf{A} - \lambda \mathbf{I})\mathbf{x} = \mathbf{0}$. For non-trivial eigenvectors $\mathbf{x} \neq \mathbf{0}$ to exist, matrix $(\mathbf{A} - \lambda \mathbf{I})$ must be singular, requiring $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$.

## Level 5 — Interview Questions Solutions
### Question 1
1. Express $\mathbf{A}$ as product of elementary matrices $E_k \dots E_1$. Determinant of product equals product of determinants for elementary row operations.
### Question 2
2. Laplace expansion expands determinant along row $i$: $\det(\mathbf{A}) = \sum_{j=1}^n (-1)^{i+j} a_{i,j} M_{i,j}$, where $M_{i,j}$ is minor sub-determinant.
### Question 3
3. Direct recursive expansion evaluates $n!$ operations. For $n=20$, $20! \approx 2.43 \times 10^{18}$ ops, taking years of computation.
### Question 4
4. LU decomposition $A = LU$ takes $O(n^3)$ operations. Determinant is computed in $O(n)$ steps as product of diagonal entries of $U$: $\det(A) = \prod u_{i,i}$.
### Question 5
5. Large determinants cause numerical floating-point underflow/overflow ($10^{-300}$ or $10^{+300}$). Log-determinant $\sum \log u_{i,i}$ stays stably bounded.
