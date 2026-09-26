# Solutions — Matrices

## Level 1 — Basic Understanding Solutions
### Question 1
1. Shape is $4 \times 3$ (read '4 by 3').
### Question 2
2. $m = 3$ rows, $n = 2$ columns. Element $a_{3,1} = 7$ (3rd row, 1st column).
### Question 3
3. A square matrix is a matrix where the number of rows equals columns ($m = n$).
### Question 4
4. A diagonal matrix is a square matrix where all entries outside the main diagonal are zero ($a_{i,j} = 0$ for $i \neq j$).
### Question 5
5. A row vector (or 1D row matrix).

## Level 2 — Calculation Solutions
### Question 1
1. 

$$
\mathbf{I}_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

.
### Question 2
2. Example: 

$$
\mathbf{S} = \begin{bmatrix} 5 & 2 \\ 2 & 9 \end{bmatrix}
$$

 (off-diagonal elements must match).
### Question 3
3. $100 \times 20 = 2000$ numbers.
### Question 4
4. 2nd row vector is $[3, 4]$.
### Question 5
5. 1st column vector is $[1, 3, 5]^T$.

## Level 3 — Conceptual Solutions
### Question 1
1. Upper triangular has zeros below main diagonal ($a_{i,j}=0$ for $i > j$). Lower triangular has zeros above main diagonal ($a_{i,j}=0$ for $i < j$).
### Question 2
2. Covariance between feature $i$ and feature $j$ equals covariance between feature $j$ and feature $i$: $\text{Cov}(X_i, X_j) = \text{Cov}(X_j, X_i)$.
### Question 3
3. No. Symmetry requires $\mathbf{A} = \mathbf{A}^T$, which implies shape $(m \times n) = (n \times m) \implies m = n$ (must be square).
### Question 4
4. A zero matrix $\mathbf{0}$ is a matrix where every single element is zero.
### Question 5
5. Grayscale 28x28 image is a matrix of 28 rows and 28 columns, where entry $A_{i,j} \in [0, 255]$ represents pixel intensity at coordinate $(i, j)$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Mini-batch matrix shape is $32 \times 784$ (32 rows/samples, 784 columns/features).
### Question 2
2. Weight matrix $\mathbf{W}$ has dimensions $128 \times 784$ (or $784 \times 128$).
### Question 3
3. Rows represent unique words in vocabulary, columns represent documents. Cell $A_{i,j}$ contains frequency of word $i$ in document $j$.

## Level 5 — Interview Questions Solutions
### Question 1
1. The trace $\text{Tr}(\mathbf{A})$ is the sum of the elements along the main diagonal: $\sum_{i=1}^n a_{i,i}$.
### Question 2
2. $\text{Tr}(\mathbf{A}) = 3 + 5 + 8 = 16$.
### Question 3
3. Row-Major stores elements row-by-row sequentially in memory (C/Python NumPy default). Column-Major stores elements column-by-column (Fortran/R/MATLAB).
### Question 4
4. A block matrix is a matrix partitioned into smaller sub-matrices (blocks).
### Question 5
5. Dense matrices store mostly zeros wasting RAM. CSR (Compressed Sparse Row) stores only non-zero values, column indices, and row pointers, saving memory.
