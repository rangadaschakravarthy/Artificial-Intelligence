# Practice Exercises — Matrix Operations

## Level 1 — Basic Understanding
1. Add matrices 

$$\mathbf{A} = \begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix}$$

 and 

$$\mathbf{B} = \begin{bmatrix} 5 & 1 \\ 0 & 2 \end{bmatrix}$$

.
2. Calculate 4 \mathbf{A} for 

$$\mathbf{A} = \begin{bmatrix} 1 & -2 \\ 3 & 0 \end{bmatrix}$$

.
3. Compute Hadamard product \mathbf{A} \odot \mathbf{B} for 

$$\mathbf{A} = \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 2 & 0 \\ -1 & 5 \end{bmatrix}$$

.
4. Can you add a $3 \times 2$ matrix to a $2 \times 3$ matrix? Why or why not?
5. What is the result of $\mathbf{A} - \mathbf{A}$ for any matrix $\mathbf{A}$?

## Level 2 — Calculation
1. Compute linear combination 2\mathbf{A} - 3\mathbf{B} for 

$$\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 0 & 4 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 3 & -1 \\ 2 & 1 \end{bmatrix}$$

.
2. Solve for matrix \mathbf{X} in equation: 

$$\mathbf{X} + \begin{bmatrix} 1 & 3 \\ 2 & 0 \end{bmatrix} = \begin{bmatrix} 4 & 5 \\ 1 & 2 \end{bmatrix}$$

.
3. Perform element-wise ReLU activation f(x) = \max(0, x) on matrix 

$$\mathbf{Z} = \begin{bmatrix} 2.5 & -1.2 \\ -0.5 & 3.0 \end{bmatrix}$$

.
4. Given $\mathbf{A} \in \mathbb{R}^{4 \times 3}$ and vector $\mathbf{b} \in \mathbb{R}^{1 \times 3}$, what is the shape of $\mathbf{A} + \mathbf{b}$ using broadcasting?
5. Show that matrix addition is commutative: $\mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}$ for $2 \times 2$ matrices.

## Level 3 — Conceptual
1. State the properties of matrix addition (Closure, Associativity, Commutativity, Identity, Inverse).
2. Explain how scalar multiplication distributes over matrix addition: $c(\mathbf{A} + \mathbf{B}) = c\mathbf{A} + c\mathbf{B}$.
3. What is the identity element for matrix addition?
4. Explain NumPy broadcasting rules step-by-step for shapes $(3, 4)$ and $(1, 4)$.
5. Why do deep learning frameworks execute element-wise operations using GPU CUDA kernels?

## Level 4 — AI/ML Application
1. In gradient descent weight update \mathbf{W} = \mathbf{W} - \eta \mathbf{G}, given 

$$\mathbf{W} = \begin{bmatrix} 0.5 & 1.0 \\ -0.2 & 0.8 \end{bmatrix}$$

, \eta = 0.1, 

$$\mathbf{G} = \begin{bmatrix} 2.0 & -1.0 \\ 0.5 & 4.0 \end{bmatrix}$$

, compute updated weight matrix \mathbf{W}.
2. A mini-batch activation matrix \mathbf{Z} \in \mathbb{R}^{3 \times 2} is 

$$\begin{bmatrix} 1.0 & 2.0 \\ 3.0 & 4.0 \\ 5.0 & 6.0 \end{bmatrix}$$

. Bias vector \mathbf{b} = [0.5, -0.5]. Compute broadcasted sum \mathbf{Z} + \mathbf{b}.
3. Explain how Dropout deactivates activations during training via Hadamard product with a random binary matrix.

## Level 5 — Interview Questions
1. Prove that the set of all $m \times n$ matrices forms a vector space under matrix addition and scalar multiplication.
2. What are the constraints for broadcasting two shapes $(d_1, d_2, d_3)$ and $(e_1, e_2, e_3)$ in NumPy/PyTorch?
3. How does element-wise division by standard deviation work in Layer Normalization?
4. Compare computational memory footprint of explicit vector expansion vs memory-strided broadcasting.
5. Show that Hadamard product of two positive semi-definite matrices is positive semi-definite (Schur Product Theorem).
