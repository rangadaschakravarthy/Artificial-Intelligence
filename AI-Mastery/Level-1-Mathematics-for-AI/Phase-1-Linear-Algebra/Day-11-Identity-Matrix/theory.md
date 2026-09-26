# Theory — Identity Matrix

### 1. Simple Definition
An identity matrix is a square matrix filled with ones along the main diagonal and zeros everywhere else. Multiplying any matrix by an identity matrix leaves it completely unchanged.

### 2. Intuition
The identity matrix is the matrix equivalent of the number 1 in scalar arithmetic. Just as $5 \times 1 = 5$, multiplying $\mathbf{A} \times \mathbf{I} = \mathbf{A}$.

### 3. Mathematical Definition
An identity matrix $\mathbf{I}_n \in \mathbb{R}^{n \times n}$ is defined by elements $I_{i,j} = \delta_{i,j}$, where $\delta_{i,j} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$ (Kronecker delta).

### 4. Notation
$\mathbf{I}_n$ or simply $\mathbf{I}$. Diagonal elements are 1, off-diagonal elements are 0.

### 5. Formula
$$\mathbf{I}_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{I}_n$: $n \times n$ Identity Matrix
- $\delta_{i,j}$: Kronecker Delta function

### 7. Step-by-Step Calculation
Multiply 

$$\mathbf{A} = \begin{bmatrix} 3 & 7 \\ 2 & 9 \end{bmatrix}$$

 by 

$$\mathbf{I}_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$

:
- $c_{1,1} = 3(1) + 7(0) = 3$
- $c_{1,2} = 3(0) + 7(1) = 7$
- $c_{2,1} = 2(1) + 9(0) = 2$
- $c_{2,2} = 2(0) + 9(1) = 9$
$$\mathbf{A}\mathbf{I}_2 = \begin{bmatrix} 3 & 7 \\ 2 & 9 \end{bmatrix} = \mathbf{A}$$

### 8. Second Example
Identify property on non-square matrix: $\mathbf{A}_{2 \times 3} \mathbf{I}_{3 \times 3} = \mathbf{A}_{2 \times 3}$.

### 9. Common Mistakes
Assuming identity matrices can be non-square (identity matrices are ALWAYS square $n \times n$).

### 10. AI Connection
ResNet skip connections: $\mathbf{y} = F(\mathbf{x}) + \mathbf{I} \mathbf{x}$. Identity initialization (IdentityInit) prevents gradient vanishing in ultra-deep networks.

### 11. Algorithm Connection
ResNet, Identity RNNs, Ridge Regression $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1}$, Matrix Inversion algorithms.

### 12. Practical Interpretation
Geometrically, an identity matrix represents a linear transformation that leaves every vector in space completely unmoved.

### 13. Interview Insight
Q: 'Why is $\lambda \mathbf{I}$ added in Ridge Regression $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})$?' A: It adds positive constants to the main diagonal, guaranteeing invertibility by preventing zero eigenvalues.

### 14. Summary
The identity matrix $\mathbf{I}_n$ has 1s on diagonal, 0s elsewhere. It is the multiplicative identity: $\mathbf{A}\mathbf{I} = \mathbf{I}\mathbf{A} = \mathbf{A}$.
