# Practice Exercises — Transpose

## Level 1 — Basic Understanding
1. Find the transpose of $\mathbf{A} = \begin{bmatrix} 1 & 5 & 9 \\ 2 & 6 & 0 \end{bmatrix}$.
2. What is the shape of $\mathbf{M}^T$ if $\mathbf{M}$ has shape $5 \times 2$?
3. What is $(\mathbf{A}^T)^T$ for any matrix $\mathbf{A}$?
4. Is matrix $\mathbf{S} = \begin{bmatrix} 3 & -1 \\ -1 & 4 \end{bmatrix}$ symmetric?
5. State the product transpose rule for $(\mathbf{A}\mathbf{B})^T$.

## Level 2 — Calculation
1. Given $\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ and $\mathbf{B} = \begin{bmatrix} 0 & 1 \\ 2 & 5 \end{bmatrix}$, compute $(\mathbf{A} + \mathbf{B})^T$ and verify it equals $\mathbf{A}^T + \mathbf{B}^T$.
2. Given $\mathbf{A} = \begin{bmatrix} 1 & 3 \\ 0 & 2 \end{bmatrix}$ and $\mathbf{B} = \begin{bmatrix} 2 & 1 \\ 4 & 0 \end{bmatrix}$, compute $(\mathbf{A}\mathbf{B})^T$.
3. Compute $\mathbf{B}^T \mathbf{A}^T$ for matrices above and verify it equals $(\mathbf{A}\mathbf{B})^T$.
4. Compute Gram matrix $\mathbf{A}^T \mathbf{A}$ for $\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 0 \end{bmatrix}$. Is it symmetric?
5. What is a skew-symmetric matrix?

## Level 3 — Conceptual
1. Prove that for any square matrix $\mathbf{A}$, the matrix $\mathbf{S} = \mathbf{A} + \mathbf{A}^T$ is always symmetric.
2. Prove that for any square matrix $\mathbf{A}$, the matrix $\mathbf{K} = \mathbf{A} - \mathbf{A}^T$ is always skew-symmetric.
3. Show that any square matrix $\mathbf{A}$ can be decomposed into a sum of a symmetric and skew-symmetric matrix: $\mathbf{A} = \frac{1}{2}(\mathbf{A} + \mathbf{A}^T) + \frac{1}{2}(\mathbf{A} - \mathbf{A}^T)$.
4. Prove that $\mathbf{A}^T \mathbf{A}$ is always a symmetric matrix for any $m \times n$ matrix $\mathbf{A}$.
5. What is the transpose of a scalar?

## Level 4 — AI/ML Application
1. In Linear Regression normal equations $\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$, if $\mathbf{X} \in \mathbb{R}^{100 \times 5}$ and $\mathbf{y} \in \mathbb{R}^{100 \times 1}$, verify the shapes of every matrix product to ensure $\mathbf{w} \in \mathbb{R}^{5 \times 1}$.
2. In deep learning backpropagation, if error gradient $\delta \in \mathbb{R}^{B \times H_{out}}$ and input $\mathbf{X} \in \mathbb{R}^{B \times H_{in}}$, show that weight gradient $\nabla_{\mathbf{W}} = \mathbf{X}^T \delta$ has shape $H_{in} \times H_{out}$.
3. In Transformer Attention $S = Q K^T$, if $Q \in \mathbb{R}^{B \times S \times D}$ and $K \in \mathbb{R}^{B \times S \times D}$, why do we transpose $K$?

## Level 5 — Interview Questions
1. Prove the general product transpose rule for $k$ matrices: $(\mathbf{A}_1 \mathbf{A}_2 \dots \mathbf{A}_k)^T = \mathbf{A}_k^T \dots \mathbf{A}_2^T \mathbf{A}_1^T$.
2. What is an orthogonal matrix? Show that for an orthogonal matrix $\mathbf{Q}$, $\mathbf{Q}^T \mathbf{Q} = \mathbf{I}$.
3. Explain how zero-copy transpose works in NumPy via memory stride manipulation (`ndarray.strides`).
4. Why does a non-contiguous memory stride after `.T` require calling `.copy()` or `np.ascontiguousarray()` before certain C-extensions?
5. What is the relationship between the trace of $\mathbf{A}^T \mathbf{A}$ and the Frobenius norm $||\mathbf{A}||_F^2$?
