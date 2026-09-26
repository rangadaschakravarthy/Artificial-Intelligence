# Practice Exercises — Determinants

## Level 1 — Basic Understanding
1. Compute the determinant of 

$$\mathbf{A} = \begin{bmatrix} 4 & 2 \\ 1 & 5 \end{bmatrix}$$

.
2. Compute the determinant of 

$$\mathbf{B} = \begin{bmatrix} 6 & 3 \\ 4 & 2 \end{bmatrix}$$

. What does this tell you about invertibility?
3. What is the determinant of identity matrix $\mathbf{I}_n$?
4. If $\det(\mathbf{A}) = 4$, what is $\det(\mathbf{A}^{-1})$?
5. Can you compute the determinant of a $3 \times 2$ matrix?

## Level 2 — Calculation
1. Compute determinant of 3 \times 3 matrix 

$$\mathbf{M} = \begin{bmatrix} 2 & 0 & 1 \\ 3 & 1 & 2 \\ 0 & 4 & 1 \end{bmatrix}$$

 using cofactor expansion.
2. Find scalar k such that 

$$\det \begin{bmatrix} k & 4 \\ 2 & 3 \end{bmatrix} = 10$$

.
3. Calculate $\det(3\mathbf{A})$ for a $2 \times 2$ matrix $\mathbf{A}$ with $\det(\mathbf{A}) = 5$.
4. Calculate $\det(c\mathbf{A})$ for an $n \times n$ matrix $\mathbf{A}$.
5. Show that $\det(\mathbf{A}^T) = \det(\mathbf{A})$ for $2 \times 2$ matrices.

## Level 3 — Conceptual
1. State the effect on determinant when: 1) Two rows are swapped, 2) A row is multiplied by constant $c$, 3) A multiple of one row is added to another.
2. Explain why a matrix with two identical rows has a determinant of 0.
3. Why is the determinant of a triangular matrix equal to the product of its diagonal elements?
4. Show that for orthogonal matrix $\mathbf{Q}$, $\det(\mathbf{Q}) = \pm 1$.
5. Explain how determinant represents volume scaling in $n$ dimensions.

## Level 4 — AI/ML Application
1. In a Normalizing Flow model, latent variable $\mathbf{z}$ is transformed by $\mathbf{x} = \mathbf{A}\mathbf{z}$. If $\det(\mathbf{A}) = 0.5$, how does the probability density scale?
2. A 2D dataset is scaled by factor 2 along x-axis and factor 3 along y-axis using diagonal matrix 

$$\mathbf{S} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$$

. Compute area scaling factor.
3. Explain how characteristic equation $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$ is used to solve for eigenvalues.

## Level 5 — Interview Questions
1. Prove that $\det(\mathbf{A}\mathbf{B}) = \det(\mathbf{A}) \det(\mathbf{B})$ using elementary matrix factorizations.
2. Explain Laplace Expansion for computing $n \times n$ determinants.
3. Why is computing determinants via cofactor expansion $O(n!)$ computationally prohibitive for $n > 20$?
4. How do LU and QR decompositions allow computing determinants in $O(n^3)$ operations?
5. What is the log-determinant $\log |\det(\mathbf{A})|$ and why is it preferred numerically over raw determinant in deep learning?
