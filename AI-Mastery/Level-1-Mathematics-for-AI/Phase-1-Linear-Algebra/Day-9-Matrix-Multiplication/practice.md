# Practice Exercises — Matrix Multiplication

## Level 1 — Basic Understanding
1. Given $\mathbf{A}$ of shape $3 \times 4$ and $\mathbf{B}$ of shape $4 \times 2$, is $\mathbf{A}\mathbf{B}$ valid? What is the output shape?
2. Given $\mathbf{A}$ of shape $3 \times 4$ and $\mathbf{B}$ of shape $4 \times 2$, is $\mathbf{B}\mathbf{A}$ valid?
3. Multiply 

$$\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$$

 and 

$$\mathbf{B} = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}$$

.
4. Multiply matrix 

$$\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 2 & 5 \end{bmatrix}$$

 by vector 

$$\mathbf{x} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$$

.
5. What is $\mathbf{A} \mathbf{I}$ where $\mathbf{I}$ is the identity matrix?

## Level 2 — Calculation
1. Compute \mathbf{A}\mathbf{B} for 

$$\mathbf{A} = \begin{bmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{bmatrix}_{2 \times 3}$$

 and 

$$\mathbf{B} = \begin{bmatrix} 3 & 1 \\ 2 & 1 \\ 1 & 0 \end{bmatrix}_{3 \times 2}$$

.
2. Compute $\mathbf{B}\mathbf{A}$ for the matrices in Question 1 above. Is $\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A}$?
3. If dataset $\mathbf{X}$ has 100 samples and 50 features, and weight matrix $\mathbf{W}$ maps to 10 hidden units, what shape must $\mathbf{W}$ have for $\mathbf{X}\mathbf{W}$?
4. Calculate matrix square \mathbf{A}^2 = \mathbf{A}\mathbf{A} for 

$$\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}$$

.
5. Show that $(\mathbf{A} + \mathbf{B})\mathbf{C} = \mathbf{A}\mathbf{C} + \mathbf{B}\mathbf{C}$ for $2 \times 2$ matrices.

## Level 3 — Conceptual
1. State the Associative Law of matrix multiplication: $(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})$. Does order matter?
2. Explain why matrix multiplication can be viewed as computing linear combinations of columns of $\mathbf{A}$.
3. Explain why matrix multiplication can also be viewed as computing linear combinations of rows of $\mathbf{B}$.
4. What is the computational complexity (number of scalar multiplications) to multiply $\mathbf{A}_{m \times k}$ and $\mathbf{B}_{k \times n}$?
5. Can the product of two non-zero matrices be a zero matrix? Give an example.

## Level 4 — AI/ML Application
1. In a Multi-Layer Perceptron layer: Input 

$$\mathbf{X}_{2 \times 3} = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 3 & 1 \end{bmatrix}$$

, Weights 

$$\mathbf{W}_{3 \times 2} = \begin{bmatrix} 1 & -1 \\ 2 & 0 \\ 0 & 1 \end{bmatrix}$$

, Bias \mathbf{b} = [1, 2]. Compute layer pre-activation \mathbf{Z} = \mathbf{X}\mathbf{W} + \mathbf{b}.
2. In Attention Mechanism, $Q \in \mathbb{R}^{B \times S \times D}$ and $K \in \mathbb{R}^{B \times S \times D}$. What is the shape of attention weight matrix $Q K^T$?
3. Explain why PyTorch linear layer defines weight matrix as shape `(out_features, in_features)` and computes $x W^T + b$.

## Level 5 — Interview Questions
1. What is Strassen's Algorithm for fast matrix multiplication? How does it improve asymptotic time complexity over $O(n^3)$?
2. Explain how GPU Tensor Cores execute mixed-precision Matrix-Multiply-Accumulate (MMA) operations ($D = A \cdot B + C$).
3. Prove that $\text{Tr}(\mathbf{A}\mathbf{B}) = \text{Tr}(\mathbf{B}\mathbf{A})$ for compatible matrices.
4. What is a nilpotent matrix?
5. How does Matrix Chain Multiplication dynamic programming optimize parenthesization order for $(\mathbf{A}_1 \mathbf{A}_2 \dots \mathbf{A}_k)$?
