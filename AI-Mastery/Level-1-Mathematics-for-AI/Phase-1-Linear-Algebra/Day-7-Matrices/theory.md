# Theory — Matrices

### 1. Simple Definition
A matrix is a two-dimensional rectangular grid of numbers arranged in rows (horizontal) and columns (vertical).

### 2. Intuition
Think of a spreadsheet table. Each row represents a student, each column represents an exam grade. The whole table is a matrix of shape (number of students $\times$ number of exams).

### 3. Mathematical Definition
A matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ is a rectangular array with $m$ rows and $n$ columns:
$$\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}$$

### 4. Notation
Uppercase bold letters $\mathbf{A}, \mathbf{B}, \mathbf{W} \in \mathbb{R}^{m \times n}$. Individual entry at row $i$, column $j$ is $a_{i,j}$ or $A_{i,j}$.

### 5. Formula
$$\mathbf{A}_{m \times n} = [a_{i,j}], \quad 1 \le i \le m, \, 1 \le j \le n$$

### 6. Symbol-by-Symbol Explanation
- $m$: Number of rows
- $n$: Number of columns
- $a_{i,j}$: Element at row $i$ and column $j$

### 7. Step-by-Step Calculation
For matrix $\mathbf{A} = \begin{bmatrix} 5 & 2 & 9 \\ 1 & 7 & 3 \end{bmatrix}$:
Rows $m = 2$, Columns $n = 3$. Shape is $2 \times 3$.
Element $a_{1,1} = 5$, $a_{1,3} = 9$, $a_{2,2} = 7$.

### 8. Second Example
Special Matrix: Diagonal matrix $\mathbf{D} = \begin{bmatrix} 4 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 9 \end{bmatrix}$. All non-diagonal entries ($i \neq j$) are zero!

### 9. Common Mistakes
Mixing up row-first vs column-first index order (remember: Row $\times$ Column = 'RC Cola'); confusing shape (2,3) with (3,2).

### 10. AI Connection
Input batch tensor shape in PyTorch: `(batch_size, num_features)`. Weight matrix $\mathbf{W}$ connects input features to output hidden nodes.

### 11. Algorithm Connection
Linear Models, Multi-Layer Perceptrons (MLPs), Covariance Matrices, Image Convolution Kernels.

### 12. Practical Interpretation
A row of a matrix represents one data observation. A column represents one feature dimension across all observations.

### 13. Interview Insight
Q: 'What is a symmetric matrix?' A: A square matrix where $\mathbf{A} = \mathbf{A}^T$, meaning $a_{i,j} = a_{j,i}$ for all $i,j$.

### 14. Summary
Matrices are 2D arrays $\mathbf{A} \in \mathbb{R}^{m \times n}$. They serve as dataset storage containers and linear operators in machine learning.
