# Theory — Rank

### 1. Simple Definition
The rank of a matrix is the maximum number of linearly independent rows (or columns) it contains. It measures the number of non-redundant dimensions of information in the matrix.

### 2. Intuition
Imagine a table with 3 columns: Height in cm, Weight in kg, and Height in inches. Height in inches adds zero new information (it's just cm $\times 0.393$). Even though there are 3 columns, the true rank is only 2 because 1 column is completely redundant.

### 3. Mathematical Definition
For $\mathbf{A} \in \mathbb{R}^{m \times n}$, the column rank is the dimension of the column space $\text{col}(\mathbf{A})$, and the row rank is the dimension of the row space $\text{row}(\mathbf{A})$. Fundamental Theorem: $\text{Row Rank} = \text{Column Rank} = \text{Rank}(\mathbf{A}) \le \min(m, n)$.

### 4. Notation
$\text{Rank}(\mathbf{A})$ or $\text{rk}(\mathbf{A}) \in \mathbb{Z}_{\ge 0}$.

### 5. Formula
$$\text{Rank}(\mathbf{A}_{m \times n}) \le \min(m, n)$$
$$\mathbf{A} \text{ is Full Rank if } \text{Rank}(\mathbf{A}) = \min(m, n)$$

### 6. Symbol-by-Symbol Explanation
- $m, n$: Rows and columns of matrix
- $\min(m, n)$: Maximum possible rank upper bound

### 7. Step-by-Step Calculation
Find rank of 

$$\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 5 \end{bmatrix}$$

:
- Row 2 is exactly $2 \times$ Row 1 ($[2, 4, 6] = 2[1, 2, 3]$). Redundant!
- Row 3 $[0, 1, 5]$ is independent of Row 1.
- We have 2 linearly independent rows $\implies \text{Rank}(\mathbf{A}) = 2$. (Rank Deficient, since $\min(3,3)=3$).

### 8. Second Example
Rank of Identity Matrix 

$$\mathbf{I}_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

: All 3 rows are linearly independent \implies \text{Rank}(\mathbf{I}_3) = 3 (Full Rank!).

### 9. Common Mistakes
Assuming a $100 \times 5$ matrix can have rank 100 (rank CANNOT exceed $\min(m, n) = 5$); confusing matrix shape with matrix rank.

### 10. AI Connection
LoRA (Low-Rank Adaptation): Fine-tunes LLM weights $\mathbf{W} \in \mathbb{R}^{4096 \times 4096}$ using rank $r=8$ factorization $\mathbf{A}_{4096 \times 8} \mathbf{B}_{8 \times 4096}$, tuning only $2 \times 4096 \times 8 = 65,536$ parameters instead of 16.7M parameters!

### 11. Algorithm Connection
LoRA (LLM Fine-tuning), SVD Dimensionality Reduction, Matrix Completion (Netflix Prize), Principal Component Analysis.

### 12. Practical Interpretation
A dataset matrix with rank $r < n$ contains $n - r$ completely redundant feature columns.

### 13. Interview Insight
Q: 'What is the relationship between matrix rank and invertibility?' A: An $n \times n$ square matrix is invertible if and only if it is Full Rank ($\text{Rank}(\mathbf{A}) = n$).

### 14. Summary
Matrix rank is the number of linearly independent rows/columns: $\text{Rank}(\mathbf{A}) \le \min(m, n)$. Full rank means no redundancy; low-rank structure enables AI model compression.
