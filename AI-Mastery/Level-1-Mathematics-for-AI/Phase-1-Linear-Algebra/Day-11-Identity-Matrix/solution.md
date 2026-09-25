# Solutions — Identity Matrix

## Level 1 — Basic Understanding Solutions
### Question 1
1. $\mathbf{I}_4 = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$.
### Question 2
2. $\mathbf{I}_n \mathbf{v} = \mathbf{v}$.
### Question 3
3. $\mathbf{I}_n^T = \mathbf{I}_n$ (Identity matrix is symmetric).
### Question 4
4. $\mathbf{I}_n^k = \mathbf{I}_n$.
### Question 5
5. $\delta_{3,3} = 1$, $\delta_{2,4} = 0$.

## Level 2 — Calculation Solutions
### Question 1
1. Left multiplication: $\mathbf{I}_2 \mathbf{A}_{2 \times 3}$. Right multiplication: $\mathbf{A}_{2 \times 3} \mathbf{I}_3$.
### Question 2
2. $\mathbf{A} + 3\mathbf{I}_2 = \begin{bmatrix} 1 & 4 \\ 2 & 5 \end{bmatrix} + \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 4 \\ 2 & 8 \end{bmatrix}$.
### Question 3
3. $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1(1)+0(0) & 1(0)+0(1) \\ 0(1)+1(0) & 0(0)+1(1) \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$.
### Question 4
4. $\det(\mathbf{I}_n) = 1$.
### Question 5
5. $\text{Tr}(\mathbf{I}_n) = \sum_{i=1}^n 1 = n$.

## Level 3 — Conceptual Solutions
### Question 1
1. Transforming any vector $\mathbf{x}$ by $\mathbf{I}$ yields $\mathbf{I}\mathbf{x} = \mathbf{x}$, preserving original length and direction angle.
### Question 2
2. All non-diagonal entries are 0 (diagonal). Entry $I_{i,j} = I_{j,i} = \delta_{i,j}$ (symmetric).
### Question 3
3. An orthogonal matrix has orthonormal columns $\mathbf{q}_i \cdot \mathbf{q}_j = \delta_{i,j}$, so $(\mathbf{Q}^T \mathbf{Q})_{i,j} = \mathbf{q}_i \cdot \mathbf{q}_j = \delta_{i,j} \implies \mathbf{Q}^T \mathbf{Q} = \mathbf{I}$.
### Question 4
4. A matrix is idempotent if $\mathbf{M}^2 = \mathbf{M}$. Since $\mathbf{I}\mathbf{I} = \mathbf{I}$, $\mathbf{I}$ is idempotent.
### Question 5
5. Initializing RNN weights to $\mathbf{I}$ allows hidden state to persist unchanged across time steps without exploding or vanishing.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\mathbf{X}^T \mathbf{X} + 0.5 \mathbf{I}_2 = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} + \begin{bmatrix} 0.5 & 0 \\ 0 & 0.5 \end{bmatrix} = \begin{bmatrix} 4.5 & 2.0 \\ 2.0 & 1.5 \end{bmatrix}$. Determinant $= 4.5(1.5) - 2(2) = 6.75 - 4.0 = 2.75 \neq 0$. Invertible!
### Question 2
2. $\mathbf{h} = [0.2, -0.1]^T + [1.0, 2.0]^T = [1.2, 1.9]^T$.
### Question 3
3. During backpropagation, error gradients flow directly through the identity shortcut path $\mathbf{I}$, guaranteeing that gradients never shrink to zero regardless of network depth.

## Level 5 — Interview Questions Solutions
### Question 1
1. Multiply $\mathbf{A}\mathbf{B} = \mathbf{I}$ on right by $\mathbf{C}$: $(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{I}\mathbf{C} = \mathbf{C}$. By associativity $\mathbf{A}(\mathbf{B}\mathbf{C}) = \mathbf{C} \implies \mathbf{A}\mathbf{I} = \mathbf{C} \implies \mathbf{A} = \mathbf{C}$.
### Question 2
2. A permutation matrix $\mathbf{P}$ has orthonormal rows/columns, so $\mathbf{P} \mathbf{P}^T = \mathbf{P}^T \mathbf{P} = \mathbf{I}$.
### Question 3
3. Householder reflection $H = I - 2 v v^T$. Givens rotation rotates 2 coordinate axes while leaving all other dimensions unchanged via embedded $I$ blocks.
### Question 4
4. $\mathbf{I}\mathbf{x} = 1 \cdot \mathbf{x}$ for all $\mathbf{x} \neq \mathbf{0}$. Thus characteristic equation $\det(\mathbf{I} - \lambda \mathbf{I}) = (1-\lambda)^n = 0 \implies \lambda = 1$.
### Question 5
5. Identity mapping in Autoencoders forces the network bottleneck to learn a compressed representation that can perfectly reconstruct original input $\hat{\mathbf{x}} \approx \mathbf{x}$.
