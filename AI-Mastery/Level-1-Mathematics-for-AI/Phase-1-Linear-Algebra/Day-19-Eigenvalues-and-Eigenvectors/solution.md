# Solutions — Eigenvalues and Eigenvectors

## Level 1 — Basic Understanding Solutions
### Question 1
1. $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$.
### Question 2
2. $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$.
### Question 3
3. Eigenvalues are the diagonal elements $\lambda_1 = 8, \lambda_2 = 3$.
### Question 4
4. $\text{Tr}(\mathbf{A}) = 4+6 = 10$. $\det(\mathbf{A}) = 4 \times 6 = 24$.
### Question 5
5. No! Eigenvectors MUST be non-zero vectors ($\mathbf{v} \neq \mathbf{0}$).

## Level 2 — Calculation Solutions
### Question 1
1. $\det \begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix} = (2-\lambda)^2 - 1 = 0 \implies (2-\lambda) = \pm 1 \implies \lambda_1 = 3, \lambda_2 = 1$.
### Question 2
2. For $\lambda_1=3$: $(\mathbf{A}-3\mathbf{I})\mathbf{v} = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} \implies \mathbf{v}_1 = [1/\sqrt{2}, 1/\sqrt{2}]^T$. For $\lambda_2=1$: $(\mathbf{A}-1\mathbf{I})\mathbf{v} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \implies \mathbf{v}_2 = [-1/\sqrt{2}, 1/\sqrt{2}]^T$.
### Question 3
3. $\text{Tr}(\mathbf{A}) = 2+2=4 = 3+1$. $\det(\mathbf{A}) = 4-1=3 = 3 \times 1$. Matches!
### Question 4
4. $\mathbf{A}^2 \mathbf{v} = \mathbf{A}(\mathbf{A}\mathbf{v}) = \mathbf{A}(\lambda \mathbf{v}) = \lambda (\mathbf{A}\mathbf{v}) = \lambda (\lambda \mathbf{v}) = \lambda^2 \mathbf{v}$.
### Question 5
5. Eigenvalues of $\mathbf{A}^{-1}$ are reciprocal eigenvalues $1/\lambda_i$.

## Level 3 — Conceptual Solutions
### Question 1
1. Spectral Theorem: Every real symmetric matrix $\mathbf{A} = \mathbf{A}^T$ can be factorized into $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^T$, where $\mathbf{Q}$ is an orthogonal matrix of real eigenvectors and $\mathbf{\Lambda}$ is a diagonal matrix of real eigenvalues.
### Question 2
2. Let $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$. Multiply left by $\bar{\mathbf{v}}^T$: $\bar{\mathbf{v}}^T \mathbf{A} \mathbf{v} = \lambda \bar{\mathbf{v}}^T \mathbf{v}$. Transpose conjugate yields $\bar{\lambda} = \lambda \implies \lambda \in \mathbb{R}$.
### Question 3
3. Let $\mathbf{A}\mathbf{v}_1 = \lambda_1 \mathbf{v}_1, \mathbf{A}\mathbf{v}_2 = \lambda_2 \mathbf{v}_2$. $\lambda_1 (\mathbf{v}_1 \cdot \mathbf{v}_2) = (\mathbf{A}\mathbf{v}_1) \cdot \mathbf{v}_2 = \mathbf{v}_1 \cdot (\mathbf{A}^T \mathbf{v}_2) = \mathbf{v}_1 \cdot (\mathbf{A}\mathbf{v}_2) = \lambda_2 (\mathbf{v}_1 \cdot \mathbf{v}_2) \implies (\lambda_1 - \lambda_2)(\mathbf{v}_1 \cdot \mathbf{v}_2) = 0$. Since $\lambda_1 \neq \lambda_2$, $\mathbf{v}_1 \cdot \mathbf{v}_2 = 0$.
### Question 4
4. $\det(\mathbf{A}) = \prod \lambda_i = 0$. Zero eigenvalue implies matrix is rank deficient and singular.
### Question 5
5. Power Iteration initializes random $\mathbf{x}_0$, repeatedly computes $\mathbf{x}_{k+1} = \frac{\mathbf{A}\mathbf{x}_k}{||\mathbf{A}\mathbf{x}_k||}$. Converges to eigenvector of largest eigenvalue $|\lambda_1|$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\det(\mathbf{\Sigma}-\lambda \mathbf{I}) = (3-\lambda)^2 - 1 = 0 \implies \lambda_1 = 4, \lambda_2 = 2$. Total variance $= 4+2 = 6$. Explained variance PC1 $= 4/6 = 66.67\%$.
### Question 2
2. Stationary probability distribution $\mathbf{p}$ satisfies $\mathbf{M}\mathbf{p} = \mathbf{p}$, which is exact eigenvalue equation with dominant eigenvalue $\lambda = 1$.
### Question 3
3. Graph Laplacian $L = D - A$ measures graph smooth signals. Eigenvalues $\lambda_i$ represent graph frequencies; eigenvectors $\mathbf{u}_i$ form Graph Fourier Basis.

## Level 5 — Interview Questions Solutions
### Question 1
1. Stack eigenvector equations $\mathbf{A}\mathbf{v}_i = \lambda_i \mathbf{v}_i$ into matrix form: $\mathbf{A} [\mathbf{v}_1 \dots \mathbf{v}_n] = [\mathbf{v}_1 \dots \mathbf{v}_n] \mathbf{\Lambda} \implies \mathbf{A}\mathbf{Q} = \mathbf{Q}\mathbf{\Lambda} \implies \mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^{-1}$.
### Question 2
2. For PSD matrix $\mathbf{A}$, $\mathbf{x}^T \mathbf{A} \mathbf{x} \ge 0$. Substitute $\mathbf{x} = \mathbf{v}_i \implies \mathbf{v}_i^T (\mathbf{A} \mathbf{v}_i) = \lambda_i ||\mathbf{v}_i||_2^2 \ge 0 \implies \lambda_i \ge 0$.
### Question 3
3. Defective matrices have geometric multiplicity of eigenvalues less than algebraic multiplicity (repeated eigenvalues without enough independent eigenvectors). Require Jordan Canonical Form $A = P J P^{-1}$.
### Question 4
4. Rayleigh quotient $R(\mathbf{A},\mathbf{x}) = \frac{\mathbf{x}^T \mathbf{A} \mathbf{x}}{\mathbf{x}^T \mathbf{x}}$. Maximum value equals dominant eigenvalue $\lambda_{max}$, achieved when $\mathbf{x}$ is 1st eigenvector.
### Question 5
5. Gershgorin Circle Theorem states every eigenvalue of $\mathbf{A}$ lies within at least one closed disc $D(a_{i,i}, R_i)$ in complex plane, where radius $R_i = \sum_{j \neq i} |a_{i,j}|$ is row off-diagonal sum.
