# Practice Exercises — Matrices

## Level 1 — Basic Understanding
1. What is the shape of a matrix with 4 rows and 3 columns?
2. Given $\mathbf{A} = \begin{bmatrix} 8 & 3 \\ 1 & 4 \\ 7 & 9 \end{bmatrix}$, what is $m$, $n$, and element $a_{3,1}$?
3. What is a square matrix?
4. Define a diagonal matrix.
5. If a matrix has shape $1 \times n$, what special name does it have?

## Level 2 — Calculation
1. Construct a $3 \times 3$ identity matrix $\mathbf{I}_3$.
2. Write a symmetric $2 \times 2$ matrix with diagonal elements 5 and 9.
3. Given $\mathbf{X} \in \mathbb{R}^{100 \times 20}$, how many total numbers are stored in matrix $\mathbf{X}$?
4. Extract the 2nd row vector from $\mathbf{M} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$.
5. Extract the 1st column vector from $\mathbf{M}$ above.

## Level 3 — Conceptual
1. Explain the difference between upper triangular and lower triangular matrices.
2. Why must a covariance matrix always be symmetric?
3. Can a non-square matrix be symmetric? Explain.
4. What is a zero matrix $\mathbf{0}_{m \times n}$?
5. How is a grayscale $28 \times 28$ image structured as a matrix?

## Level 4 — AI/ML Application
1. A mini-batch of 32 images, each flattened to 784 features, is passed to a model. What are the dimensions of this mini-batch dataset matrix?
2. A layer takes 784 inputs and outputs 128 hidden nodes. What are the dimensions of its weight matrix $\mathbf{W}$?
3. Explain how word-document co-occurrence is stored in a Term-Document Matrix.

## Level 5 — Interview Questions
1. What is the trace of a square matrix $\text{Tr}(\mathbf{A})$?
2. Calculate the trace of $\mathbf{A} = \begin{bmatrix} 3 & 1 & 4 \\ 2 & 5 & 9 \\ 7 & 6 & 8 \end{bmatrix}$.
3. Explain matrix memory layout: Row-Major (C style) vs Column-Major (Fortran style).
4. What is a block matrix?
5. Why do sparse matrices require specialized storage formats (CSR, CSC) in ML?
