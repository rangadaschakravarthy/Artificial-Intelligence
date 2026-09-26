# Solutions — Transpose

## Level 1 — Basic Understanding Solutions
### Question 1
1. 

$$
\mathbf{A}^T = \begin{bmatrix} 1 & 2 \\ 5 & 6 \\ 9 & 0 \end{bmatrix}_{3 \times 2}
$$

.
### Question 2
2. Shape is $2 \times 5$.
### Question 3
3. $(\mathbf{A}^T)^T = \mathbf{A}$.
### Question 4
4. Yes, because 

$$
\mathbf{S}^T = \begin{bmatrix} 3 & -1 \\ -1 & 4 \end{bmatrix} = \mathbf{S}
$$

.
### Question 5
5. $(\mathbf{A}\mathbf{B})^T = \mathbf{B}^T \mathbf{A}^T$.

## Level 2 — Calculation Solutions
### Question 1
1. 

$$
\mathbf{A}+\mathbf{B} = \begin{bmatrix} 1 & 3 \\ 5 & 9 \end{bmatrix} \implies (\mathbf{A}+\mathbf{B})^T = \begin{bmatrix} 1 & 5 \\ 3 & 9 \end{bmatrix}
$$

. 

$$
\mathbf{A}^T+\mathbf{B}^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix} + \begin{bmatrix} 0 & 2 \\ 1 & 5 \end{bmatrix} = \begin{bmatrix} 1 & 5 \\ 3 & 9 \end{bmatrix}
$$

. Equal!
### Question 2
2. 

$$
\mathbf{A}\mathbf{B} = \begin{bmatrix} 1(2)+3(4) & 1(1)+3(0) \\ 0(2)+2(4) & 0(1)+2(0) \end{bmatrix} = \begin{bmatrix} 14 & 1 \\ 8 & 0 \end{bmatrix} \implies (\mathbf{A}\mathbf{B})^T = \begin{bmatrix} 14 & 8 \\ 1 & 0 \end{bmatrix}
$$

.
### Question 3
3. 

$$
\mathbf{B}^T = \begin{bmatrix} 2 & 4 \\ 1 & 0 \end{bmatrix}, \mathbf{A}^T = \begin{bmatrix} 1 & 0 \\ 3 & 2 \end{bmatrix} \implies \mathbf{B}^T \mathbf{A}^T = \begin{bmatrix} 2(1)+4(3) & 2(0)+4(2) \\ 1(1)+0(3) & 1(0)+0(2) \end{bmatrix} = \begin{bmatrix} 14 & 8 \\ 1 & 0 \end{bmatrix}
$$

. Matches!
### Question 4
4. 

$$
\mathbf{A}^T \mathbf{A} = \begin{bmatrix} 1 & 3 \\ 2 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 0 \end{bmatrix} = \begin{bmatrix} 10 & 2 \\ 2 & 4 \end{bmatrix}
$$

. Yes, it is symmetric!
### Question 5
5. A square matrix $\mathbf{K}$ where $\mathbf{K}^T = -\mathbf{K}$ (all diagonal entries must be 0).

## Level 3 — Conceptual Solutions
### Question 1
1. Proof: $\mathbf{S}^T = (\mathbf{A} + \mathbf{A}^T)^T = \mathbf{A}^T + (\mathbf{A}^T)^T = \mathbf{A}^T + \mathbf{A} = \mathbf{S}$. Thus $\mathbf{S}$ is symmetric.
### Question 2
2. Proof: $\mathbf{K}^T = (\mathbf{A} - \mathbf{A}^T)^T = \mathbf{A}^T - (\mathbf{A}^T)^T = \mathbf{A}^T - \mathbf{A} = -(\mathbf{A} - \mathbf{A}^T) = -\mathbf{K}$. Thus skew-symmetric.
### Question 3
3. Add symmetric part $\mathbf{S}_{half}$ and skew-symmetric part $\mathbf{K}_{half}$: $\frac{1}{2}\mathbf{A} + \frac{1}{2}\mathbf{A}^T + \frac{1}{2}\mathbf{A} - \frac{1}{2}\mathbf{A}^T = \mathbf{A}$.
### Question 4
4. Proof: $(\mathbf{A}^T \mathbf{A})^T = \mathbf{A}^T (\mathbf{A}^T)^T = \mathbf{A}^T \mathbf{A}$. Therefore $\mathbf{A}^T \mathbf{A}$ is symmetric.
### Question 5
5. A scalar is its own transpose ($c^T = c$).

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\mathbf{X}^T_{5 \times 100} \mathbf{X}_{100 \times 5} = (\mathbf{X}^T \mathbf{X})_{5 \times 5}$. Inverse is $(5 \times 5)$. $(\mathbf{X}^T \mathbf{X})^{-1}_{5 \times 5} \mathbf{X}^T_{5 \times 100} \mathbf{y}_{100 \times 1} = \mathbf{w}_{5 \times 1}$. Correct!
### Question 2
2. $\mathbf{X}^T$ has shape $H_{in} \times B$. $\delta$ has shape $B \times H_{out}$. Product $\mathbf{X}^T \delta$ has shape $(H_{in} \times B) \cdot (B \times H_{out}) = (H_{in} \times H_{out})$. Matches weight matrix shape!
### Question 3
3. To align embedding dimension $D$ for dot product: $(B \times S \times D) \cdot (B \times D \times S) = (B \times S \times S)$.

## Level 5 — Interview Questions Solutions
### Question 1
1. Proof by induction: Base case $(A_1 A_2)^T = A_2^T A_1^T$. Assume for $k-1$. For $k$: $( (A_1 \dots A_{k-1}) A_k )^T = A_k^T (A_1 \dots A_{k-1})^T = A_k^T A_{k-1}^T \dots A_1^T$.
### Question 2
2. An orthogonal matrix $\mathbf{Q}$ has orthonormal columns. $\mathbf{Q}^T \mathbf{Q} = \mathbf{I} \implies \mathbf{Q}^{-1} = \mathbf{Q}^T$.
### Question 3
3. NumPy `.T` swaps shape tuple $(m, n) \rightarrow (n, m)$ and stride tuple $(s_1, s_2) \rightarrow (s_2, s_1)$ without copying underlying array bytes in memory.
### Question 4
4. Swapping strides makes array memory non-contiguous (C-contiguous flag becomes False). C-extensions expecting contiguous memory blocks will fail unless re-copied.
### Question 5
5. $\text{Tr}(\mathbf{A}^T \mathbf{A}) = \sum_{i} (\mathbf{A}^T \mathbf{A})_{i,i} = \sum_i \sum_j a_{j,i}^2 = ||\mathbf{A}||_F^2$ (Frobenius norm squared).
