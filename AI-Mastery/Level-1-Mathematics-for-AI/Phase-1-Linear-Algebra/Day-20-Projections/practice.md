# Practice Exercises — Projections

## Level 1 — Basic Understanding
1. Calculate the vector projection of $\mathbf{v} = [4, 6]^T$ onto $\mathbf{u} = [2, 0]^T$.
2. What is the residual error vector $\mathbf{e} = \mathbf{v} - \text{proj}_{\mathbf{u}}(\mathbf{v})$?
3. What is an idempotent matrix?
4. State the formula for Projection Matrix $\mathbf{P}$ onto column space of $\mathbf{A}$.
5. If vector $\mathbf{x}$ ALREADY lies in subspace $W$, what is $\mathbf{P}_W \mathbf{x}$?

## Level 2 — Calculation
1. Compute Projection Matrix $\mathbf{P}$ for line spanned by unit vector $\mathbf{u} = [0.6, 0.8]^T$.
2. Show that for unit vector $\mathbf{u}$, projection matrix formula simplifies to $\mathbf{P} = \mathbf{u} \mathbf{u}^T$.
3. Given $\mathbf{A} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$, calculate $\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$.
4. Verify that $\mathbf{P}^T = \mathbf{P}$ for the projection matrix computed above.
5. Verify that $\mathbf{P}^2 = \mathbf{P}$ for the projection matrix computed above.

## Level 3 — Conceptual
1. Prove that projection matrix $\mathbf{P} = \mathbf{A}(\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T$ is always symmetric: $\mathbf{P}^T = \mathbf{P}$.
2. Prove that projection matrix $\mathbf{P}$ is idempotent: $\mathbf{P}^2 = \mathbf{P}$.
3. Show that residual error vector $\mathbf{e} = (\mathbf{I} - \mathbf{P})\mathbf{b}$ is orthogonal to $\text{Col}(\mathbf{A})$.
4. What are the eigenvalues of any projection matrix $\mathbf{P}$? (Hint: Use $\mathbf{P}^2 \mathbf{v} = \lambda^2 \mathbf{v}$).
5. What is the trace of a projection matrix $\text{Tr}(\mathbf{P})$?

## Level 4 — AI/ML Application
1. In Linear Regression $\mathbf{y} = \mathbf{X}\mathbf{w} + \mathbf{e}$, prove that prediction vector $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w}$ is the orthogonal projection of $\mathbf{y}$ onto $\text{Col}(\mathbf{X})$.
2. Show that residual vector $\mathbf{e} = \mathbf{y} - \hat{\mathbf{y}}$ is orthogonal to every feature column in $\mathbf{X}$ (meaning $\mathbf{X}^T \mathbf{e} = \mathbf{0}$).
3. Explain how Gram-Schmidt process uses successive orthogonal projections to build an orthonormal basis.

## Level 5 — Interview Questions
1. Show that $(\mathbf{I} - \mathbf{P})$ is also a projection matrix. Onto which subspace does $(\mathbf{I} - \mathbf{P})$ project?
2. What is an Oblique Projection matrix (non-orthogonal projection)?
3. Explain how Kernel PCA computes non-linear projections in feature spaces.
4. Prove that distance $|\mathbf{b} - \mathbf{P}\mathbf{b}\|_2 \le ||\mathbf{b} - \mathbf{z}||_2$ for any vector $\mathbf{z} \in \text{Col}(\mathbf{A})$ (Pythagorean Theorem of projections).
5. Explain the connection between Orthogonal Projections and Conditional Expectation $E[Y|X]$ in Hilbert spaces of random variables.
