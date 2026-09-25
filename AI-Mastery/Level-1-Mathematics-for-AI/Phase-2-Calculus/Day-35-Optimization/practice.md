# Practice Exercises — Optimization

## Level 1 — Basic Understanding
1. What is a critical point in optimization?
2. What is the Hessian matrix?
3. How do Hessian eigenvalues classify a local minimum?
4. How do Hessian eigenvalues classify a local maximum?
5. How do Hessian eigenvalues classify a saddle point?

## Level 2 — Calculation
1. Find the critical point of $f(x, y) = 2x^2 + 3y^2 - 8x - 12y + 20$.
2. Construct the Hessian matrix for $f(x, y) = 2x^2 + 3y^2 - 8x - 12y + 20$.
3. Classify the critical point from Question 1 using Hessian eigenvalues.
4. Find and classify critical points of $f(x, y) = x^2 - 4xy + y^2$.
5. Compute Newton-Raphson 1D update step $x_{new} = x - \frac{f'(x)}{f''(x)}$ for $f(x) = x^2 - 6x + 5$ starting at $x=0$.

## Level 3 — Conceptual
1. Prove that if function $f(\mathbf{x})$ is strictly convex, any local minimum is a global minimum.
2. Explain why computing exact Hessian matrix inversion $\mathbf{H}^{-1}$ is computationally prohibitive in deep learning ($O(d^3)$ ops for $d=10^6$).
3. Explain Quasi-Newton methods (BFGS and L-BFGS) that approximate $\mathbf{H}^{-1}$ using low-rank gradient updates.
4. Why do deep neural networks prefer wide flat minima over sharp narrow minima for better test set generalization?
5. What is the condition number of the Hessian matrix $\kappa(\mathbf{H}) = \frac{\lambda_{max}}{\lambda_{min}}$ and how does ill-conditioning slow down SGD?

## Level 4 — AI/ML Application
1. Perform Newton's Method optimization in Python on 2D Rosenbrock function $f(x, y) = (1-x)^2 + 100(y-x^2)^2$. Verify 1-step convergence near minimum.
2. Explain why saddle points with negative eigenvalues are more common than true local minima in high-dimensional non-convex loss surfaces.
3. Explain how Sharpness-Aware Minimization (SAM) optimizer explicitly seeks flat loss minima.

## Level 5 — Interview Questions
1. Derive Newton's Optimization Method formula $\mathbf{x}_{t+1} = \mathbf{x}_t - \mathbf{H}^{-1} \nabla f(\mathbf{x}_t)$ using second-order Taylor expansion.
2. Explain Constrained Optimization and the Method of Lagrange Multipliers $\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda g(\mathbf{x})$.
3. State the Karush-Kuhn-Tucker (KKT) conditions for non-linear inequality constrained optimization.
4. Explain Hessian-Free Optimization (Truncated Newton) using Conjugate Gradient to compute Hessian-vector products $\mathbf{H}\mathbf{v}$ without building $\mathbf{H}$.
5. Explain how Loss Landscape Visualization (e.g. Filter Normalization contour plotting) visualizes high-dimensional neural network loss surfaces.
