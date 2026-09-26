# Theory — Transpose

### 1. Simple Definition
The transpose of a matrix flips it over its main diagonal, turning all rows into columns and all columns into rows.

### 2. Intuition
Imagine holding a spreadsheet by its top-left corner and flipping the sheet sideways. What were once the table rows now become the table columns.

### 3. Mathematical Definition
For matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$, its transpose $\mathbf{A}^T \in \mathbb{R}^{n \times m}$ is defined by:
$$(\mathbf{A}^T)_{i,j} = a_{j,i}$$

### 4. Notation
$\mathbf{A}^T$, $\mathbf{A}'$, or $\mathbf{A}^\top$. Shape transforms from $m \times n$ to $n \times m$.

### 5. Formula
$$\text{If } \mathbf{A} = \begin{bmatrix} a & b \\ c & d \\ e & f \end{bmatrix}_{3 \times 2} \implies \mathbf{A}^T = \begin{bmatrix} a & c & e \\ b & d & f \end{bmatrix}_{2 \times 3}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{A}$: Original $m \times n$ matrix
- $\mathbf{A}^T$: Transposed $n \times m$ matrix
- $a_{j,i}$: Element at row $j$, col $i$ of original matrix

### 7. Step-by-Step Calculation
Given 

$$\mathbf{A} = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \end{bmatrix}_{2 \times 3}$$

:
- Row 1 $[1, 4, 7]$ becomes Column 1 $[1, 4, 7]^T$
- Row 2 $[2, 5, 8]$ becomes Column 2 $[2, 5, 8]^T$
$$\mathbf{A}^T = \begin{bmatrix} 1 & 2 \\ 4 & 5 \\ 7 & 8 \end{bmatrix}_{3 \times 2}$$

### 8. Second Example
Verify $(\mathbf{A}\mathbf{B})^T = \mathbf{B}^T \mathbf{A}^T$:
Let 

$$\mathbf{A} = \begin{bmatrix} 1 & 2 \end{bmatrix}_{1 \times 2}, \mathbf{B} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}_{2 \times 1}$$

.
$\mathbf{A}\mathbf{B} = [1(3)+2(4)] = [11]_{1 \times 1} \implies (\mathbf{A}\mathbf{B})^T = [11]$.


$$\mathbf{B}^T = [3, 4]_{1 \times 2}, \mathbf{A}^T = \begin{bmatrix} 1 \\ 2 \end{bmatrix}_{2 \times 1} \implies \mathbf{B}^T \mathbf{A}^T = 3(1)+4(2) = 11$$

. Matches!

### 9. Common Mistakes
Forgetting to reverse matrix order when transposing products: writing $(\mathbf{A}\mathbf{B})^T = \mathbf{A}^T \mathbf{B}^T$ (INCORRECT!).

### 10. AI Connection
Backpropagation weight gradient: $\frac{\partial L}{\partial \mathbf{X}} = \frac{\partial L}{\partial \mathbf{Z}} \mathbf{W}^T$. Linear Regression normal equation: $\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$. Neural Style Transfer Gram Matrix $G = \mathbf{F} \mathbf{F}^T$.

### 11. Algorithm Connection
Linear Regression, Backpropagation in Deep Learning, Principal Component Analysis, Neural Style Transfer.

### 12. Practical Interpretation
For any matrix $\mathbf{A}$, the product $\mathbf{A}^T \mathbf{A}$ is always a square, symmetric matrix of shape $n \times n$.

### 13. Interview Insight
Q: 'Why is $(\mathbf{A}\mathbf{B})^T = \mathbf{B}^T \mathbf{A}^T$?' A: Transposing reverses inner and outer dimensions. To keep inner dimensions compatible for multiplication, the matrix order must flip.

### 14. Summary
Matrix transpose swaps rows and columns $(\mathbf{A}^T)_{i,j} = a_{j,i}$. Key identity: $(\mathbf{A}\mathbf{B})^T = \mathbf{B}^T \mathbf{A}^T$. Product $\mathbf{A}^T \mathbf{A}$ is always square and symmetric.
