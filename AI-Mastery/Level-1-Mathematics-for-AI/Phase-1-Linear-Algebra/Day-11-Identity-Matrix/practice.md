# Practice Exercises — Identity Matrix

## Level 1 — Basic Understanding
1. Write the $4 \times 4$ identity matrix $\mathbf{I}_4$.
2. What is $\mathbf{I}_n \mathbf{v}$ for any vector $\mathbf{v} \in \mathbb{R}^n$?
3. What is the transpose of an identity matrix $\mathbf{I}_n^T$?
4. What is $\mathbf{I}_n^k$ for any positive integer $k$?
5. Evaluate Kronecker delta $\delta_{3,3}$ and $\delta_{2,4}$.

## Level 2 — Calculation
1. Given $\mathbf{A} = \begin{bmatrix} 2 & -1 & 4 \\ 5 & 0 & 3 \end{bmatrix}_{2 \times 3}$, state which identity matrix $\mathbf{I}_k$ multiplies $\mathbf{A}$ on the left and right.
2. Calculate $\mathbf{A} + 3\mathbf{I}_2$ for $\mathbf{A} = \begin{bmatrix} 1 & 4 \\ 2 & 5 \end{bmatrix}$.
3. Show that $\mathbf{I}_2 \mathbf{I}_2 = \mathbf{I}_2$.
4. Calculate determinant of $\mathbf{I}_n$.
5. Compute trace of $\mathbf{I}_n$.

## Level 3 — Conceptual
1. Explain why $\mathbf{I}$ represents a zero-rotation, unit-scale geometric transformation.
2. Why is an identity matrix both symmetric and diagonal?
3. Show that for any orthogonal matrix $\mathbf{Q}$, $\mathbf{Q}^T \mathbf{Q} = \mathbf{I}$.
4. What is an idempotent matrix? Show that $\mathbf{I}$ is idempotent.
5. Why do we initialize RNN recurrent weights to identity matrices (Identity RNN)?

## Level 4 — AI/ML Application
1. In Ridge Regression, $\mathbf{X}^T \mathbf{X} = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}$ is singular (non-invertible). Add $\lambda \mathbf{I}$ with $\lambda = 0.5$ and show the result is invertible.
2. A ResNet layer output is $\mathbf{h} = F(\mathbf{x}) + \mathbf{I}\mathbf{x}$. If $F(\mathbf{x}) = [0.2, -0.1]^T$ and $\mathbf{x} = [1.0, 2.0]^T$, compute $\mathbf{h}$.
3. Explain how identity shortcut connections solve the vanishing gradient problem in 100+ layer deep neural networks.

## Level 5 — Interview Questions
1. Prove that if $\mathbf{A}\mathbf{B} = \mathbf{I}$ and $\mathbf{B}\mathbf{C} = \mathbf{I}$, then $\mathbf{A} = \mathbf{C}$.
2. What is a permutation matrix? Show that multiplying a permutation matrix by its transpose yields $\mathbf{I}$.
3. How is identity matrix used in Householder reflections and Givens rotations?
4. Prove that eigenvalues of identity matrix $\mathbf{I}_n$ are all equal to 1.
5. Explain the concept of identity mapping in Autoencoders.
