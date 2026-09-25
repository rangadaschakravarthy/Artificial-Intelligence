# Theory — Matrix Operations

### 1. Simple Definition
Matrix addition adds corresponding elements of two matrices of identical shape. Scalar multiplication scales every entry by a number.

### 2. Intuition
If you have two tables of student test scores from Semester 1 and Semester 2, adding the matrices gives each student's total combined score for each subject.

### 3. Mathematical Definition
For $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{m \times n}$ and $c \in \mathbb{R}$:
$$(\mathbf{A} + \mathbf{B})_{i,j} = a_{i,j} + b_{i,j}, \quad (c\mathbf{A})_{i,j} = c \cdot a_{i,j}$$

### 4. Notation
$\mathbf{A} + \mathbf{B}$ for addition, $c\mathbf{A}$ for scalar mult, $\mathbf{A} \odot \mathbf{B}$ or $\mathbf{A} * \mathbf{B}$ for Hadamard product.

### 5. Formula
$$\mathbf{C} = \mathbf{A} \odot \mathbf{B} \implies c_{i,j} = a_{i,j} \cdot b_{i,j}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{A}, \mathbf{B}$: Input matrices of shape $m \times n$
- $\mathbf{C}$: Output matrix of shape $m \times n$
- $a_{i,j}, b_{i,j}$: Elements at row $i$, column $j$

### 7. Step-by-Step Calculation
Given $\mathbf{A} = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 5 & 0 \\ -1 & 2 \end{bmatrix}$:
1. $\mathbf{A} + \mathbf{B} = \begin{bmatrix} 1+5 & 3+0 \\ 2+(-1) & 4+2 \end{bmatrix} = \begin{bmatrix} 6 & 3 \\ 1 & 6 \end{bmatrix}$
2. $3\mathbf{A} = \begin{bmatrix} 3(1) & 3(3) \\ 3(2) & 3(4) \end{bmatrix} = \begin{bmatrix} 3 & 9 \\ 6 & 12 \end{bmatrix}$

### 8. Second Example
Hadamard Product $\mathbf{A} \odot \mathbf{B} = \begin{bmatrix} 1(5) & 3(0) \\ 2(-1) & 4(2) \end{bmatrix} = \begin{bmatrix} 5 & 0 \\ -2 & 8 \end{bmatrix}$.

### 9. Common Mistakes
Attempting matrix addition on matrices with different shapes; confusing Hadamard product $\mathbf{A} \odot \mathbf{B}$ with dot product matrix multiplication $\mathbf{A} \mathbf{B}$.

### 10. AI Connection
Bias addition across batch: Matrix $\mathbf{Z} \in \mathbb{R}^{B \times H}$ plus bias row vector $\mathbf{b} \in \mathbb{R}^{1 \times H}$ via broadcasting. ReLU activation $f(\mathbf{Z}) = \max(0, \mathbf{Z})$ applies element-wise.

### 11. Algorithm Connection
Batch Normalization, Neural Network Activations, Image Brightness Adjustments, Dropout Masking.

### 12. Practical Interpretation
Broadcasting expands lower-dimensional arrays across higher-dimensional arrays automatically without copying data.

### 13. Interview Insight
Q: 'What is NumPy broadcasting?' A: A mechanism that allows arithmetic operations on arrays of different shapes by implicitly stretching dimensions of size 1.

### 14. Summary
Matrix addition/subtraction and Hadamard product operate element-wise on matching shapes $m \times n$. Scalar multiplication rescales all entries.
