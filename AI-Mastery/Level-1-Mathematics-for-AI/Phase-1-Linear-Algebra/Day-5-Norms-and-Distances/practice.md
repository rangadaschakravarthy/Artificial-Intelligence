# Practice Exercises — Norms and Distances

## Level 1 — Basic Understanding
1. Calculate the L1 norm of $\mathbf{v} = [3, -2, 5]^T$.
2. Calculate the L2 norm of $\mathbf{v} = [6, 8]^T$.
3. Calculate the Infinity norm of $\mathbf{v} = [-10, 4, 7]^T$.
4. What is the Euclidean distance between points $\mathbf{a} = [1, 1]^T$ and $\mathbf{b} = [4, 5]^T$?
5. What is a unit vector?

## Level 2 — Calculation
1. Normalize vector $\mathbf{v} = [5, 12]^T$ to create unit vector $\hat{\mathbf{v}}$.
2. Compute Manhattan distance between $\mathbf{x} = [2, -3, 4]^T$ and $\mathbf{y} = [5, 1, -2]^T$.
3. Show that $||c \mathbf{v}||_2 = |c| ||\mathbf{v}||_2$ for $c = -3$ and $\mathbf{v} = [3, 4]^T$.
4. Given $\mathbf{u} = [1, 2]^T$ and $\mathbf{v} = [4, 2]^T$, calculate $||\mathbf{u} + \mathbf{v}||_2$ and compare with $||\mathbf{u}||_2 + ||\mathbf{v}||_2$ (Triangle Inequality).
5. Calculate $L_2$ squared norm $||\mathbf{v}||_2^2$ for $\mathbf{v} = [2, -1, 3]^T$ using dot product.

## Level 3 — Conceptual
1. Prove the Triangle Inequality $||\mathbf{u} + \mathbf{v}|| \le ||\mathbf{u}|| + ||\mathbf{v}||$ for 1D scalars.
2. Explain why $||\mathbf{v}||_2 \le ||\mathbf{v}||_1$ for any vector $\mathbf{v}$.
3. Draw/describe the unit circles ($||\mathbf{x}|| = 1$) for L1, L2, and $L_\infty$ norms in 2D space.
4. What happens to a vector's norm when it is multiplied by zero scalar?
5. Why is Euclidean distance sensitive to feature scale?

## Level 4 — AI/ML Application
1. In Ridge Regression, loss function is $J(\mathbf{w}) = \text{MSE} + \lambda ||\mathbf{w}||_2^2$. If weights $\mathbf{w} = [0.6, -0.8]^T$ and $\lambda = 0.5$, compute regularization penalty.
2. In Lasso Regression, loss is $J(\mathbf{w}) = \text{MSE} + \lambda ||\mathbf{w}||_1$. If weights $\mathbf{w} = [0.6, -0.8]^T$ and $\lambda = 0.5$, compute Lasso penalty.
3. Compute the normalized embedding vectors for $\mathbf{a} = [3, 0]^T$ and $\mathbf{b} = [2, 2]^T$.

## Level 5 — Interview Questions
1. Mathematically derive why L1 norm contour intersects cost function axes at sharp corners causing zero weights.
2. Prove that Euclidean distance satisfies symmetry: $d(\mathbf{u}, \mathbf{v}) = d(\mathbf{v}, \mathbf{u})$.
3. What is Minkowski distance? How does it generalize Manhattan and Euclidean distances?
4. Explain why high-dimensional spaces suffer from norm concentration ('curse of dimensionality' in distance metrics).
5. How does batch normalization utilize vector mean and L2 variance?
