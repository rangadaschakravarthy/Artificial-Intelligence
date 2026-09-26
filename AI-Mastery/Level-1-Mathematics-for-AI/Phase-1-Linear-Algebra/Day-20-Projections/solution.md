# Solutions — Projections

## Level 1 — Basic Understanding Solutions
### Question 1
1. $\mathbf{u} \cdot \mathbf{v} = 2(4)+0(6) = 8$. $||\mathbf{u}||^2 = 4$. $\text{proj} = \frac{8}{4} [2,0]^T = 2[2,0]^T = [4,0]^T$.
### Question 2
2. $\mathbf{e} = [4,6]^T - [4,0]^T = [0, 6]^T$.
### Question 3
3. An idempotent matrix is a matrix satisfying $\mathbf{P}^2 = \mathbf{P}$.
### Question 4
4. $\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$.
### Question 5
5. $\mathbf{P}_W \mathbf{x} = \mathbf{x}$ (remains unchanged).

## Level 2 — Calculation Solutions
### Question 1
1. 

$$\mathbf{P} = \mathbf{u}\mathbf{u}^T = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix} \begin{bmatrix} 0.6 & 0.8 \end{bmatrix} = \begin{bmatrix} 0.36 & 0.48 \\ 0.48 & 0.64 \end{bmatrix}$$

.
### Question 2
2. For unit vector $\mathbf{u}$, $\mathbf{u}^T \mathbf{u} = ||\mathbf{u}||^2 = 1 \implies (\mathbf{u}^T \mathbf{u})^{-1} = 1 \implies \mathbf{P} = \mathbf{u}(1)\mathbf{u}^T = \mathbf{u}\mathbf{u}^T$.
### Question 3
3. \mathbf{A}^T \mathbf{A} = [1(1)+2(2)] = [5]. Inverse = [1/5]. 

$$\mathbf{P} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} [1/5] \begin{bmatrix} 1 & 2 \end{bmatrix} = \begin{bmatrix} 0.2 & 0.4 \\ 0.4 & 0.8 \end{bmatrix}$$

.
### Question 4
4. 

$$\mathbf{P}^T = \begin{bmatrix} 0.2 & 0.4 \\ 0.4 & 0.8 \end{bmatrix}^T = \mathbf{P}$$

. Symmetric!
### Question 5
5. 

$$\mathbf{P}^2 = \begin{bmatrix} 0.2 & 0.4 \\ 0.4 & 0.8 \end{bmatrix} \begin{bmatrix} 0.2 & 0.4 \\ 0.4 & 0.8 \end{bmatrix} = \begin{bmatrix} 0.04+0.16 & 0.08+0.32 \\ 0.08+0.32 & 0.16+0.64 \end{bmatrix} = \begin{bmatrix} 0.2 & 0.4 \\ 0.4 & 0.8 \end{bmatrix} = \mathbf{P}$$

. Idempotent!

## Level 3 — Conceptual Solutions
### Question 1
1. Proof: $\mathbf{P}^T = (\mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T)^T = (\mathbf{A}^T)^T ((\mathbf{A}^T \mathbf{A})^{-1})^T \mathbf{A}^T = \mathbf{A} ((\mathbf{A}^T \mathbf{A})^T)^{-1} \mathbf{A}^T = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T = \mathbf{P}$.
### Question 2
2. Proof: $\mathbf{P}^2 = (\mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T) (\mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T) = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} (\mathbf{A}^T \mathbf{A}) (\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T = \mathbf{A} \mathbf{I} (\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T = \mathbf{P}$.
### Question 3
3. Multiply $\mathbf{A}^T \mathbf{e} = \mathbf{A}^T (\mathbf{b} - \mathbf{P}\mathbf{b}) = \mathbf{A}^T \mathbf{b} - \mathbf{A}^T \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T \mathbf{b} = \mathbf{A}^T \mathbf{b} - \mathbf{A}^T \mathbf{b} = \mathbf{0}$. Residual $\mathbf{e}$ is perpendicular to columns of $\mathbf{A}$!
### Question 4
4. $\mathbf{P}\mathbf{v} = \lambda \mathbf{v} \implies \mathbf{P}^2 \mathbf{v} = \lambda^2 \mathbf{v}$. Since $\mathbf{P}^2 = \mathbf{P}$, $\lambda^2 \mathbf{v} = \lambda \mathbf{v} \implies \lambda^2 = \lambda \implies \lambda = 0$ or $\lambda = 1$.
### Question 5
5. $\text{Tr}(\mathbf{P}) = \text{Rank}(\mathbf{P}) = k$ (dimension of target subspace).

## Level 4 — AI/ML Application Solutions
### Question 1
1. Normal equation sets $\mathbf{X}^T (\mathbf{y} - \mathbf{X}\mathbf{w}) = \mathbf{0} \implies \mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$. Predicted $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w} = \mathbf{X}(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} = \mathbf{P}_X \mathbf{y}$.
### Question 2
2. $\mathbf{X}^T \mathbf{e} = \mathbf{X}^T (\mathbf{y} - \hat{\mathbf{y}}) = \mathbf{X}^T (\mathbf{y} - \mathbf{X}(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}) = \mathbf{X}^T \mathbf{y} - (\mathbf{X}^T \mathbf{X})(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} = \mathbf{0}$.
### Question 3
3. Gram-Schmidt builds orthogonal vector $\mathbf{u}_k$ by subtracting orthogonal projections onto all previously computed basis vectors: $\mathbf{u}_k = \mathbf{v}_k - \sum_{j < k} \text{proj}_{u_j}(\mathbf{v}_k)$.

## Level 5 — Interview Questions Solutions
### Question 1
1. $(\mathbf{I}-\mathbf{P})^2 = \mathbf{I} - 2\mathbf{P} + \mathbf{P}^2 = \mathbf{I} - 2\mathbf{P} + \mathbf{P} = \mathbf{I} - \mathbf{P}$. Idempotent! $(\mathbf{I}-\mathbf{P})$ projects onto the orthogonal complement subspace $\text{Col}(\mathbf{A})^\perp$.
### Question 2
2. Oblique projections project onto subspace $W$ along direction $V$ non-orthogonally. Satisfies $\mathbf{P}^2 = \mathbf{P}$ but is NOT symmetric ($\mathbf{P}^T \neq \mathbf{P}$).
### Question 3
3. Kernel PCA computes projections in high-dimensional feature space $\mathcal{F}$ via Kernel Matrix $K_{i,j} = k(x_i, x_j)$, solving eigenvalue problem on centered kernel matrix $K_{centered}$.
### Question 4
4. For any $\mathbf{z} \in \text{Col}(\mathbf{A})$, $(\mathbf{b} - \mathbf{z}) = (\mathbf{b} - \mathbf{P}\mathbf{b}) + (\mathbf{P}\mathbf{b} - \mathbf{z})$. Since $(\mathbf{b} - \mathbf{P}\mathbf{b}) \perp (\mathbf{P}\mathbf{b} - \mathbf{z})$, by Pythagorean theorem: $||\mathbf{b} - \mathbf{z}||^2 = ||\mathbf{b} - \mathbf{P}\mathbf{b}||^2 + ||\mathbf{P}\mathbf{b} - \mathbf{z}||^2 \ge ||\mathbf{b} - \mathbf{P}\mathbf{b}||^2$. Minimal distance occurs when $\mathbf{z} = \mathbf{P}\mathbf{b}$!
### Question 5
5. Conditional expectation $E[Y|X]$ is the orthogonal projection of random variable $Y$ onto the subspace of all $X$-measurable functions in $L^2$ Hilbert space.
