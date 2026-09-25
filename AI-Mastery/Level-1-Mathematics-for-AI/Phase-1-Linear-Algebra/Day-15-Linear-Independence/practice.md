# Practice Exercises — Linear Independence

## Level 1 — Basic Understanding
1. Are vectors $\mathbf{u} = [1, 3]^T$ and $\mathbf{v} = [2, 6]^T$ linearly independent? Why?
2. Are standard basis vectors $\mathbf{e}_1 = [1, 0, 0]^T, \mathbf{e}_2 = [0, 1, 0]^T, \mathbf{e}_3 = [0, 0, 1]^T$ linearly independent?
3. What is the maximum number of linearly independent vectors in $\mathbb{R}^4$?
4. If a set of vectors contains the zero vector $\mathbf{0}$, is it linearly independent or dependent?
5. State the linear independence equation $c_1 \mathbf{v}_1 + \dots + c_k \mathbf{v}_k = \mathbf{0}$.

## Level 2 — Calculation
1. Test if $\mathbf{a} = [1, 2]^T$ and $\mathbf{b} = [-1, 3]^T$ are linearly independent using determinant.
2. Determine if $\mathbf{u} = [1, 0, 1]^T, \mathbf{v} = [0, 1, 1]^T, \mathbf{w} = [1, 1, 2]^T$ are independent.
3. If $\mathbf{v}_1, \mathbf{v}_2$ are independent, are $2\mathbf{v}_1, 3\mathbf{v}_2$ independent?
4. Show that any 2 non-parallel vectors in $\mathbb{R}^2$ are linearly independent.
5. Explain why adding a 3rd vector $\mathbf{w} = 2\mathbf{u} - \mathbf{v}$ creates a dependent set.

## Level 3 — Conceptual
1. Prove that any set of vectors containing the zero vector $\mathbf{0}$ is ALWAYS linearly dependent.
2. Prove that if $\{\mathbf{v}_1, \mathbf{v}_2\}$ is linearly independent, then $\{\mathbf{v}_1 + \mathbf{v}_2, \mathbf{v}_1 - \mathbf{v}_2\}$ is also linearly independent.
3. Explain why $k > n$ vectors in $\mathbb{R}^n$ must be linearly dependent using Gaussian Elimination.
4. What is the relationship between linear independence of column vectors and matrix rank?
5. Show that non-zero orthogonal vectors are always linearly independent.

## Level 4 — AI/ML Application
1. In Categorical One-Hot Encoding for 3 colors (Red, Green, Blue), we create 3 binary features $x_1, x_2, x_3$. Show that $x_1 + x_2 + x_3 = 1$ creates linear dependence with bias feature $x_0 = 1$ (Dummy Variable Trap).
2. A sensor outputs temperature in Celsius ($x_1$) and Fahrenheit ($x_2 = 1.8x_1 + 32$). Are $[x_1, x_2]^T$ features linearly independent?
3. Explain how Gram-Schmidt Orthogonalization converts a set of linearly independent vectors into an orthonormal basis.

## Level 5 — Interview Questions
1. Prove that columns of matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$ are linearly independent if and only if $\mathbf{A} \mathbf{x} = \mathbf{0}$ has ONLY the trivial solution $\mathbf{x} = \mathbf{0}$.
2. Explain the concept of Linear Span $\text{Span}(\mathbf{v}_1, \dots, \mathbf{v}_k)$ and its relation to linear independence.
3. What is a Basis of a vector space?
4. How does linear dependence relate to the presence of 0 eigenvalues in a square matrix?
5. Explain the Vapnik-Chervonenkis (VC) dimension and linear independence in Kernel SVM hyperplanes.
