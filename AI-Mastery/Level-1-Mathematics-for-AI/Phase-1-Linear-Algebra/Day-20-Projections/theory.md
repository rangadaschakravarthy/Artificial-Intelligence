# Theory — Projections

### 1. Simple Definition
Projection drops a perpendicular line from a vector point down onto a line or plane subspace, finding the closest point in that subspace.

### 2. Intuition
Imagine a 3D object casting a shadow under a spotlight overhead. The 2D shadow on the floor is the orthogonal projection of the 3D object onto the floor plane!

### 3. Mathematical Definition
The orthogonal projection of vector $\mathbf{v}$ onto line spanned by non-zero vector $\mathbf{u}$ is:
$$\text{proj}_{\mathbf{u}}(\mathbf{v}) = \left(\frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{u}||_2^2}\right) \mathbf{u}$$
For projection onto column space of matrix $\mathbf{A}$, projection matrix $\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$, and projected vector $\hat{\mathbf{b}} = \mathbf{P}\mathbf{b}$.

### 4. Notation
$\text{proj}_{W}(\mathbf{v})$ or $\mathbf{P}\mathbf{v}$. Residual error vector $\mathbf{e} = \mathbf{v} - \mathbf{P}\mathbf{v}$.

### 5. Formula
$$\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T \implies \hat{\mathbf{b}} = \mathbf{P}\mathbf{b}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{A}$: Matrix spanning target subspace
- $\mathbf{P}$: Projection Matrix of shape $m \times m$
- $\mathbf{b}$: Input target vector
- $\hat{\mathbf{b}}$: Projected closest vector in subspace

### 7. Step-by-Step Calculation
Project vector $\mathbf{v} = [3, 4]^T$ onto line $\mathbf{u} = [1, 0]^T$ ($x$-axis):
1. Dot product: $\mathbf{u} \cdot \mathbf{v} = 1(3) + 0(4) = 3$.
2. L2 norm squared $||\mathbf{u}||^2 = 1^2 + 0^2 = 1$.
3. Projection: $\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{3}{1} [1, 0]^T = [3, 0]^T$.
4. Residual error $\mathbf{e} = [3,4]^T - [3,0]^T = [0, 4]^T$. (Notice $\mathbf{e} \perp \mathbf{u}$!).

### 8. Second Example
Project $\mathbf{b} = [1, 2, 3]^T$ onto column space of $\mathbf{A} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$ ($xy$-plane in $\mathbb{R}^3$):
$\mathbf{A}^T \mathbf{A} = \mathbf{I}_2 \implies \mathbf{P} = \mathbf{A} \mathbf{A}^T = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}$.
$\hat{\mathbf{b}} = \mathbf{P}\mathbf{b} = [1, 2, 0]^T$. Drops $z$-coordinate!

### 9. Common Mistakes
Forgetting that projecting an ALREADY projected vector does nothing (idempotence $\mathbf{P}^2 = \mathbf{P}$).

### 10. AI Connection
Least Squares Regression: Solves $\mathbf{X}\mathbf{w} = \mathbf{y}$ when no exact solution exists by projecting $\mathbf{y}$ orthogonally onto $\text{Col}(\mathbf{X})$. Output $\hat{\mathbf{y}} = \mathbf{X}(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$.

### 11. Algorithm Connection
Linear Regression (OLS), Gram-Schmidt Orthogonalization, Principal Component Analysis, Support Vector Machines.

### 12. Practical Interpretation
The projection point $\hat{\mathbf{b}} = \mathbf{P}\mathbf{b}$ is the UNIQUE point in subspace $\text{Col}(\mathbf{A})$ that minimizes Euclidean distance $|\mathbf{b} - \hat{\mathbf{b}}\|_2$.

### 13. Interview Insight
Q: 'Why is a projection matrix idempotent ($\mathbf{P}^2 = \mathbf{P}$)?' A: Once a vector is projected onto a subspace, it already lies inside the subspace. Projecting it a second time leaves it in the exact same spot.

### 14. Summary
Orthogonal projection finds the closest point in a subspace: $\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{u}\cdot\mathbf{v}}{||\mathbf{u}||^2}\mathbf{u}$. Projection matrix $\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$ is symmetric and idempotent ($\mathbf{P}^2 = \mathbf{P}$).
