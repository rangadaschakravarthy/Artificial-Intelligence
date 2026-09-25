# Solutions — Dot Product

## Level 1 — Basic Understanding Solutions
### Question 1
1. $1(4) + 3(2) = 4 + 6 = 10$.
### Question 2
2. (-2)(3) + 5(0) + 1(4) = -6 + 0 + 4 = -2.
### Question 3
3. The dot product is a scalar (a single real number).
### Question 4
4. $\mathbf{v} \cdot \mathbf{0} = 0$, because every component product is 0.
### Question 5
5. The vectors are orthogonal (perpendicular at 90 degrees).

## Level 2 — Calculation Solutions
### Question 1
1. $\mathbf{w}^T \mathbf{x} = 2(0.5) + (-1)(2.0) + 3(1.0) = 1.0 - 2.0 + 3.0 = 2.0$.
### Question 2
2. $[2, k]^T \cdot [3, 4]^T = 2(3) + k(4) = 6 + 4k = 0 \implies 4k = -6 \implies k = -1.5$.
### Question 3
3. $\mathbf{v} \cdot \mathbf{v} = 3(3) + 4(4) = 9 + 16 = 25$. This equals the squared Euclidean length $|\mathbf{v}||_2^2 = 5^2 = 25$.
### Question 4
4. $\mathbf{u} \cdot \mathbf{v} = 1(4) + 2(5) + 3(6) = 4 + 10 + 18 = 32$. $2(32) = 64$.
### Question 5
5. $\mathbf{u} \cdot \mathbf{v} = 2(-3) + 1(5) = -6 + 5 = -1$. $\mathbf{v} \cdot \mathbf{u} = (-3)(2) + 5(1) = -6 + 5 = -1$. Both equal -1.

## Level 3 — Conceptual Solutions
### Question 1
1. $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \sum u_i (v_i + w_i) = \sum (u_i v_i + u_i w_i) = \sum u_i v_i + \sum u_i w_i = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$.
### Question 2
2. $\mathbf{u} \cdot \mathbf{v} = ||\mathbf{u}|| ||\mathbf{v}|| \cos(\theta) = 0$. For non-zero magnitudes, $\cos(\theta) = 0 \implies \theta = 90^\circ$.
### Question 3
3. Doubling one vector magnitude doubles the resulting dot product: $(c\mathbf{u}) \cdot \mathbf{v} = c(\mathbf{u} \cdot \mathbf{v})$.
### Question 4
4. A unit vector $\mathbf{u}$ has magnitude $|\mathbf{u}|| = 1$. $\mathbf{u} \cdot \mathbf{u} = ||\mathbf{u}||^2 = 1^2 = 1$.
### Question 5
5. Called 'inner product' because it maps two elements of the same vector space into the underlying scalar field (unlike outer product which produces a matrix).

## Level 4 — AI/ML Application Solutions
### Question 1
1. $z = \mathbf{w}^T \mathbf{x} + b = (1.5)(2.0) + (-2.0)(1.0) + (0.5)(4.0) + (-0.5) = 3.0 - 2.0 + 2.0 - 0.5 = 2.5$. Yes, $z > 0$.
### Question 2
2. $S = (0.6)(0.8) + (0.8)(0.6) = 0.48 + 0.48 = 0.96$.
### Question 3
3. A CNN kernel filter is a matrix of weights. For each image patch, it computes the element-wise product sum (dot product) between kernel weights and pixel intensities.

## Level 5 — Interview Questions Solutions
### Question 1
1. $|\mathbf{u} - \mathbf{v}||^2 = (\mathbf{u} - \mathbf{v}) \cdot (\mathbf{u} - \mathbf{v}) = \mathbf{u}\cdot\mathbf{u} - 2\mathbf{u}\cdot\mathbf{v} + \mathbf{v}\cdot\mathbf{v} = ||\mathbf{u}||^2 + ||\mathbf{v}||^2 - 2(\mathbf{u} \cdot \mathbf{v})$.
### Question 2
2. For large key dimensions $d_k$, dot products grow large in magnitude, pushing softmax functions into regions with extremely small gradients (vanishing gradients). Scaling by $\sqrt{d_k}$ keeps variance at 1.
### Question 3
3. $(Q u) \cdot (Q v) = (Q u)^T (Q v) = u^T Q^T Q v = u^T I v = u^T v = u \cdot v$.
### Question 4
4. The scalar projection of $\mathbf{u}$ onto $\mathbf{v}$ is $\frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{v}||}$. Dot product measures how much length $\mathbf{u}$ contributes along direction $\mathbf{v}$.
### Question 5
5. Vectorized dot products leverage specialized BLAS (Basic Linear Algebra Subprograms) libraries and CPU SIMD registers, completing operations in parallel memory bursts.
