# Theory — Determinants

### 1. Simple Definition
The determinant is a single scalar number calculated from a square matrix that measures how much the matrix scales areas or volumes when transforming space.

### 2. Intuition
Imagine a 1x1 unit square grid on graph paper. A matrix transforms this grid. The area of the new shape (parallelogram) is the determinant! If $\det = 2$, area doubles. If $\det = 0$, the square collapses into a flat line (zero area).

### 3. Mathematical Definition
The determinant $\det(\mathbf{A})$ or $|\mathbf{A}|$ of a square matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$ is a scalar representing the signed $n$-dimensional hypervolume of the unit hypercube transformed by $\mathbf{A}$.

### 4. Notation
$\det(\mathbf{A})$ or $|\mathbf{A}|$. Applies ONLY to square matrices.

### 5. Formula
$$\text{For } 2 \times 2: \det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$
$$\text{For } 3 \times 3: \det \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = a(ei - fh) - b(di - fg) + c(dh - eg)$$

### 6. Symbol-by-Symbol Explanation
- $a, b, c, \dots$: Matrix element entries
- $(ei - fh)$: $2 \times 2$ sub-determinant (minor) for element $a$

### 7. Step-by-Step Calculation
Calculate determinant of 

$$\mathbf{A} = \begin{bmatrix} 3 & 8 \\ 4 & 6 \end{bmatrix}$$

:
$$\det(\mathbf{A}) = (3)(6) - (8)(4) = 18 - 32 = -14$$
(Negative sign means orientation of space was flipped!)

### 8. Second Example
Calculate 3 \times 3 determinant for 

$$\mathbf{B} = \begin{bmatrix} 1 & 2 & 0 \\ 3 & 4 & 1 \\ 0 & 1 & 2 \end{bmatrix}$$

:
$\det(\mathbf{B}) = 1(4\cdot 2 - 1\cdot 1) - 2(3\cdot 2 - 1\cdot 0) + 0(3\cdot 1 - 4\cdot 0)$
$= 1(8 - 1) - 2(6 - 0) + 0 = 7 - 12 = -5$.

### 9. Common Mistakes
Applying determinant formulas to non-square matrices; confusing matrix magnitude/norm with determinant.

### 10. AI Connection
Normalizing Flows (Generative Models): $p_{\mathbf{X}}(\mathbf{x}) = p_{\mathbf{Z}}(\mathbf{z}) |\det J_f(\mathbf{z})|^{-1}$. Multivariate Gaussian probability density function uses $|\mathbf{\Sigma}|^{-1/2}$.

### 11. Algorithm Connection
Normalizing Flow Generative Models, Multivariate Gaussian Distributions, PCA Eigenvalue calculations.

### 12. Practical Interpretation
A negative determinant indicates that the transformation reverses spatial orientation (like a mirror reflection).

### 13. Interview Insight
Q: 'Why does $\det(\mathbf{A}\mathbf{B}) = \det(\mathbf{A})\det(\mathbf{B})$ make intuitive sense?' A: If $\mathbf{B}$ scales volume by factor $k_1$ and $\mathbf{A}$ scales volume by factor $k_2$, applying both sequentially scales volume by $k_1 \times k_2$.

### 14. Summary
Determinant $\det(\mathbf{A})$ measures spatial area/volume scaling. Matrix is invertible if and only if $\det(\mathbf{A}) \neq 0$. Key rule: $\det(\mathbf{A}\mathbf{B}) = \det(\mathbf{A})\det(\mathbf{B})$.
