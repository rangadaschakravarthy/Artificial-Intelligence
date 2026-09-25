# Theory — Matrix Multiplication

### 1. Simple Definition
Matrix multiplication computes each entry $C_{i,j}$ of the output matrix as the dot product between row $i$ of the first matrix and column $j$ of the second matrix.

### 2. Intuition
Imagine transforming a batch of data. Each row of matrix $\mathbf{A}$ is a sample. Each column of matrix $\mathbf{B}$ is a linear feature extractor filter. Matrix multiplication applies all filters to all samples at once!

### 3. Mathematical Definition
For $\mathbf{A} \in \mathbb{R}^{m \times k}$ and $\mathbf{B} \in \mathbb{R}^{k \times n}$, their product $\mathbf{C} = \mathbf{A}\mathbf{B} \in \mathbb{R}^{m \times n}$ has entries:
$$c_{i,j} = \sum_{p=1}^k a_{i,p} b_{p,j} = \mathbf{a}_{i,:} \cdot \mathbf{b}_{:,j}$$

### 4. Notation
$\mathbf{C} = \mathbf{A} \mathbf{B}$ or $\mathbf{A} \cdot \mathbf{B}$. Shape check: $(m \times k) \times (k \times n) \rightarrow (m \times n)$.

### 5. Formula
$$c_{i,j} = a_{i,1}b_{1,j} + a_{i,2}b_{2,j} + \dots + a_{i,k}b_{k,j}$$

### 6. Symbol-by-Symbol Explanation
- $m$: Rows in matrix $\mathbf{A}$ (e.g. batch size)
- $k$: Columns in $\mathbf{A}$ = Rows in $\mathbf{B}$ (matching inner dimension)
- $n$: Columns in matrix $\mathbf{B}$ (e.g. output features)
- $c_{i,j}$: Dot product of row $i$ of $\mathbf{A}$ and col $j$ of $\mathbf{B}$

### 7. Step-by-Step Calculation
Multiply $\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{2 \times 2}$ and $\mathbf{B} = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}_{2 \times 2}$:
- $c_{1,1} = 1(5) + 2(7) = 5 + 14 = 19$
- $c_{1,2} = 1(6) + 2(8) = 6 + 16 = 22$
- $c_{2,1} = 3(5) + 4(7) = 15 + 28 = 43$
- $c_{2,2} = 3(6) + 4(8) = 18 + 32 = 50$
$$\mathbf{C} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

### 8. Second Example
Multiply $\mathbf{X}_{1 \times 3} = [2, 1, 3]$ and $\mathbf{W}_{3 \times 2} = \begin{bmatrix} 1 & 0 \\ -1 & 2 \\ 0 & 4 \end{bmatrix}$:
$c_{1,1} = 2(1) + 1(-1) + 3(0) = 1$
$c_{1,2} = 2(0) + 1(2) + 3(4) = 14$
Output $\mathbf{Y} = [1, 14]_{1 \times 2}$.

### 9. Common Mistakes
Multiplying matrices with incompatible inner dimensions; assuming $\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A}$ (matrix multiplication is GENERALLY NOT COMMUTATIVE!); multiplying element-wise instead of dot product.

### 10. AI Connection
Neural Network Linear Layer: Batch dataset $\mathbf{X}_{B \times D_{in}}$ multiplied by Weight matrix $\mathbf{W}_{D_{in} \times D_{out}}$ yields output $\mathbf{Y}_{B \times D_{out}}$. Tensor Cores on NVIDIA GPUs are hardware accelerated for matrix multiplication.

### 11. Algorithm Connection
Deep Neural Networks, Convolutional Networks (via cuDNN im2col), Transformer Self-Attention ($Q K^T V$), Graph Neural Networks.

### 12. Practical Interpretation
Matrix multiplication represents composition of linear transformations. Applying $\mathbf{B}$ then $\mathbf{A}$ to vector $\mathbf{x}$ is $(\mathbf{A}\mathbf{B})\mathbf{x}$.

### 13. Interview Insight
Q: 'If $\mathbf{A}$ is shape $(5, 10)$ and $\mathbf{B}$ is shape $(10, 3)$, can you compute $\mathbf{A}\mathbf{B}$? What about $\mathbf{B}\mathbf{A}$?' A: $\mathbf{A}\mathbf{B}$ is valid (shape $5 \times 3$). $\mathbf{B}\mathbf{A}$ is invalid because inner dimensions $(3 \neq 5)$ do not match.

### 14. Summary
Matrix multiplication computes row-by-column dot products. Dimensions must satisfy $(m \times k)(k \times n) = (m \times n)$. It is non-commutative but associative.
