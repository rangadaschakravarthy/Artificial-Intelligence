# Practice Exercises — Vector Operations

## Level 1 — Basic Understanding
1. Compute $[3, 7]^T + [2, -4]^T$.
2. Compute $5 \cdot [-1, 2, 0]^T$.
3. Compute $[4, 5, 6]^T - [1, 2, 3]^T$.
4. Find the Hadamard product of $[2, 3]^T$ and $[4, -1]^T$.
5. Can you add $\mathbf{a} \in \mathbb{R}^3$ and $\mathbf{b} \in \mathbb{R}^4$? Why or why not?

## Level 2 — Calculation
1. Compute linear combination $2[1, 3, -2]^T - 3[0, 2, 1]^T$.
2. Given $\mathbf{u} = [5, 12]^T$, find $-1 \cdot \mathbf{u}$. What is its geometric relation to $\mathbf{u}$?
3. Solve for vector $\mathbf{x}$ in equation: $\mathbf{x} + [2, 3]^T = [7, 1]^T$.
4. Given $\mathbf{a} = [2, 0]^T, \mathbf{b} = [0, 3]^T$, compute $3\mathbf{a} + 4\mathbf{b}$.
5. Compute Hadamard product $\mathbf{x} \odot \mathbf{y}$ for $\mathbf{x} = [0.5, 2.0, 1.5]^T, \mathbf{y} = [2.0, 0.5, 3.0]^T$.

## Level 3 — Conceptual
1. Explain the geometric Parallelogram Law of vector addition.
2. Show that vector addition is commutative: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$.
3. What is the identity element for vector addition in $\mathbb{R}^n$?
4. Explain how vector subtraction $\mathbf{b} - \mathbf{a}$ represents a direction vector from $\mathbf{a}$ to $\mathbf{b}$.
5. Why is Hadamard multiplication different from dot product?

## Level 4 — AI/ML Application
1. In Gradient Descent, weight vector update is $\mathbf{\theta}_{t+1} = \mathbf{\theta}_t - \eta \nabla J(\mathbf{\theta}_t)$. Calculate $\mathbf{\theta}_1$ if $\mathbf{\theta}_0 = [0.5, -0.5]^T$, learning rate $\eta = 0.01$, gradient $\nabla J = [10.0, -5.0]^T$.
2. A ResNet block computes $\mathbf{y} = f(\mathbf{x}) + \mathbf{x}$. If input feature $\mathbf{x} = [1.2, 0.8]^T$ and transformed output $f(\mathbf{x}) = [-0.2, 0.5]^T$, compute block output $\mathbf{y}$.
3. How can Hadamard product be used for Dropout in neural networks?

## Level 5 — Interview Questions
1. Prove that scalar multiplication distributes over vector addition: $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$.
2. What is a convex combination of vectors $\mathbf{u}$ and $\mathbf{v}$?
3. Explain how word vector analogy works using vector addition and subtraction.
4. If $\mathbf{w}_1, \mathbf{w}_2$ are vectors in $\mathbb{R}^n$, under what condition is $a\mathbf{w}_1 + b\mathbf{w}_2 = \mathbf{0}$ with $a,b \neq 0$?
5. Why is vectorization faster in NumPy than Python loops for element-wise operations?
