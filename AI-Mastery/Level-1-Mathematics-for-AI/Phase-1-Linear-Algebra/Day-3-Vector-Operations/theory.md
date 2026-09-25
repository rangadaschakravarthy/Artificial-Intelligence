# Theory — Vector Operations

### 1. Simple Definition
Vector addition adds corresponding elements of two vectors. Scalar multiplication rescales every element of a vector by a constant number.

### 2. Intuition
If walking vector $\mathbf{u}$ takes you 3 steps East and 2 North, and vector $\mathbf{v}$ takes you 1 step West and 4 North, their sum $\mathbf{u}+\mathbf{v}$ gives your net movement: 2 steps East and 6 North.

### 3. Mathematical Definition
For $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ and $c \in \mathbb{R}$:
$$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n \end{bmatrix}, \quad c\mathbf{u} = \begin{bmatrix} c u_1 \\ \vdots \\ c u_n \end{bmatrix}$$

### 4. Notation
$\mathbf{u} + \mathbf{v}$ for addition, $\mathbf{u} \odot \mathbf{v}$ or $\mathbf{u} * \mathbf{v}$ for element-wise (Hadamard) product.

### 5. Formula
$$\mathbf{w} = a\mathbf{u} + b\mathbf{v} = \begin{bmatrix} a u_1 + b v_1 \\ \vdots \\ a u_n + b v_n \end{bmatrix}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{u}, \mathbf{v}$: Input vectors
- $a, b$: Scalar weights
- $\mathbf{w}$: Resulting linear combination vector

### 7. Step-by-Step Calculation
Given $\mathbf{u} = [2, 5]^T$, $\mathbf{v} = [3, -1]^T$:
1. Addition: $\mathbf{u} + \mathbf{v} = [2+3, 5+(-1)]^T = [5, 4]^T$
2. Subtraction: $\mathbf{u} - \mathbf{v} = [2-3, 5-(-1)]^T = [-1, 6]^T$
3. Scalar product ($c=4$): $4\mathbf{u} = [4(2), 4(5)]^T = [8, 20]^T$

### 8. Second Example
Hadamard product of $\mathbf{a} = [1, 2, 3]^T$ and $\mathbf{b} = [4, 5, 6]^T$:
$$\mathbf{a} \odot \mathbf{b} = [1 \times 4, 2 \times 5, 3 \times 6]^T = [4, 10, 18]^T$$

### 9. Common Mistakes
Attempting to add vectors of different dimensions; confusing matrix multiplication with element-wise vector product.

### 10. AI Connection
Residual connections (ResNets) add input vector directly to layer output: $\mathbf{y} = F(\mathbf{x}) + \mathbf{x}$. Attention mechanisms compute weighted linear combinations of value vectors.

### 11. Algorithm Connection
ResNet architectures, Word Embedding arithmetic ('king' - 'man' + 'woman' = 'queen'), Gradient Descent updates.

### 12. Practical Interpretation
Vector subtraction $\mathbf{v} - \mathbf{u}$ yields the displacement vector pointing from $\mathbf{u}$ to $\mathbf{v}$.

### 13. Interview Insight
Q: 'Why can't you add a 3D vector to a 4D vector?' A: Vector spaces of different dimensions are not closed under addition; element-wise matching is undefined.

### 14. Summary
Vector arithmetic operates component-wise. Addition combines displacements; scalar multiplication scales vectors; Hadamard multiplication filters features.
