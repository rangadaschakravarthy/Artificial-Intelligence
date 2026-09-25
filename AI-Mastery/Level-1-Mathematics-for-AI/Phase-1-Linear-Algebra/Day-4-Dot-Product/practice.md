# Practice Exercises — Dot Product

## Level 1 — Basic Understanding
1. Calculate $[1, 3]^T \cdot [4, 2]^T$.
2. Calculate $[-2, 5, 1]^T \cdot [3, 0, 4]^T$.
3. Is the dot product of two vectors a scalar or a vector?
4. What is the dot product of any vector $\mathbf{v}$ with the zero vector $\mathbf{0}$?
5. If $\mathbf{a} \cdot \mathbf{b} = 0$, what is the geometric relationship between $\mathbf{a}$ and $\mathbf{b}$?

## Level 2 — Calculation
1. Given $\mathbf{x} = [2, -1, 3]^T$ and $\mathbf{w} = [0.5, 2.0, 1.0]^T$, compute $\mathbf{w}^T \mathbf{x}$.
2. Find scalar $k$ such that $[2, k]^T$ is orthogonal to $[3, 4]^T$.
3. Compute $\mathbf{v} \cdot \mathbf{v}$ for $\mathbf{v} = [3, 4]^T$. How does this relate to length?
4. If $\mathbf{u} = [1, 2, 3]^T$ and $\mathbf{v} = [4, 5, 6]^T$, compute $2(\mathbf{u} \cdot \mathbf{v})$.
5. Prove numerically that $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$ for $\mathbf{u} = [2, 1]^T, \mathbf{v} = [-3, 5]^T$.

## Level 3 — Conceptual
1. State and prove the distributive property of dot products: $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$.
2. Explain why $\mathbf{u} \cdot \mathbf{v} = 0$ implies $\cos(\theta) = 0$ for non-zero vectors.
3. How does dot product change when one vector's magnitude is doubled?
4. What is the dot product of a unit vector with itself?
5. Why is dot product called an 'inner product'?

## Level 4 — AI/ML Application
1. A linear classifier has weight vector $\mathbf{w} = [1.5, -2.0, 0.5]^T$ and bias $b = -0.5$. Predict output $z = \mathbf{w}^T \mathbf{x} + b$ for sample $\mathbf{x} = [2.0, 1.0, 4.0]^T$. Is $z > 0$?
2. Compute attention score $S = \mathbf{q}^T \mathbf{k}$ for query $\mathbf{q} = [0.6, 0.8]^T$ and key $\mathbf{k} = [0.8, 0.6]^T$.
3. Explain how convolution operations in CNNs perform local dot products between kernel filters and image patches.

## Level 5 — Interview Questions
1. Derive the relationship between dot product $\mathbf{u} \cdot \mathbf{v}$ and Euclidean distance $|\mathbf{u} - \mathbf{v}||_2^2$.
2. Why is scaled dot-product attention $\frac{Q K^T}{\sqrt{d_k}}$ scaled by $\sqrt{d_k}$ in Transformer architectures?
3. Show that dot product preserves linear transformations under orthogonal matrices: $(Q u) \cdot (Q v) = u \cdot v$.
4. What is the geometric interpretation of dot product as vector projection?
5. Why is vectorized matrix-vector dot product multiplication faster than scalar nested loops?
