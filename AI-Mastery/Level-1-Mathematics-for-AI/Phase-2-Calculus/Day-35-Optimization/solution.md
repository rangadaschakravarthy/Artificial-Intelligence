# Solutions — Optimization

## Level 1 — Basic Understanding Solutions
### Question 1
1. A point $\mathbf{x}^*$ where the gradient vector equals zero $\nabla f(\mathbf{x}^*) = \mathbf{0}$.
### Question 2
2. The $n \times n$ symmetric matrix of all second-order partial derivatives $H_{i,j} = \frac{\partial^2 f}{\partial x_i \partial x_j}$.
### Question 3
3. All eigenvalues are strictly positive ($\lambda_i > 0$, Positive Definite $\mathbf{H} \succ 0$).
### Question 4
4. All eigenvalues are strictly negative ($\lambda_i < 0$, Negative Definite $\mathbf{H} \prec 0$).
### Question 5
5. Eigenvalues have mixed signs (some positive, some negative).

## Level 2 — Calculation Solutions
### Question 1
1. $\nabla f = [4x - 8, 6y - 12]^T = [0, 0]^T \implies x^* = 2, y^* = 2$. Critical point $(2, 2)$.
### Question 2
2. 

$$f_{xx} = 4, f_{xy} = 0, f_{yy} = 6 \implies \mathbf{H} = \begin{bmatrix} 4 & 0 \\ 0 & 6 \end{bmatrix}$$

.
### Question 3
3. Eigenvalues $\lambda_1 = 4, \lambda_2 = 6$. Both positive $\implies (2, 2)$ is a STRICT LOCAL MINIMUM.
### Question 4
4. \nabla f = [2x - 4y, -4x + 2y]^T = [0, 0]^T \implies (0, 0). 

$$\mathbf{H} = \begin{bmatrix} 2 & -4 \\ -4 & 2 \end{bmatrix}$$

. \det(\mathbf{H}-\lambda\mathbf{I}) = (2-\lambda)^2 - 16 = 0 \implies \lambda_1 = 6, \lambda_2 = -2. Mixed signs \implies (0, 0) is a SADDLE POINT!
### Question 5
5. $f'(x) = 2x - 6, f''(x) = 2$. At $x=0$: $x_{new} = 0 - \frac{-6}{2} = 0 + 3 = 3$. Minimum of quadratic reached in exactly 1 step!

## Level 3 — Conceptual Solutions
### Question 1
1. For strictly convex function, $f(\mathbf{y}) > f(\mathbf{x}) + \nabla f(\mathbf{x})^T (\mathbf{y} - \mathbf{x})$. At critical point $\nabla f(\mathbf{x}^*) = \mathbf{0} \implies f(\mathbf{y}) > f(\mathbf{x}^*)$ for all $\mathbf{y} \neq \mathbf{x}^*$. Global minimum!
### Question 2
2. For $d = 1,000,000$ parameters, Hessian matrix size is $10^{12}$ entries. Computing $\mathbf{H}^{-1}$ takes $O(d^3) = 10^{18}$ ops, requiring exabytes of memory.
### Question 3
3. BFGS updates an inverse Hessian approximation $B_t \approx \mathbf{H}^{-1}$ using rank-2 updates from parameter step $\mathbf{s}_t = \mathbf{x}_{t+1} - \mathbf{x}_t$ and gradient change $\mathbf{y}_t = g_{t+1} - g_t$, taking $O(d^2)$ ops. L-BFGS stores only last $m \approx 10$ vectors, taking $O(m d)$ ops.
### Question 4
4. Wide flat minima have low Hessian eigenvalues. Small test set input perturbations move predictions slightly within flat low-loss regions, ensuring strong generalization.
### Question 5
5. Ill-conditioning $\kappa(\mathbf{H}) = \lambda_{max} / \lambda_{min} \gg 1$ causes loss surface to form steep narrow ravines. SGD oscillates violently across high-curvature directions while making slow progress along low-curvature directions.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Rosenbrock minimum is at $(1, 1)$ with $f(1,1)=0$. Newton step $\mathbf{x}_{t+1} = \mathbf{x}_t - \mathbf{H}^{-1} \nabla f$ converges quadratically near minimum in 2-3 iterations.
### Question 2
2. In $d$ dimensions, probability of all $d$ random Hessian eigenvalues being positive is $1/2^d$. For $d=100$, probability is $1/2^{100} \approx 10^{-30}$. Almost all critical points in high-D spaces are saddle points with mixed eigenvalue signs.
### Question 3
3. SAM minimizes loss value and loss sharpness simultaneously: $\min_{\mathbf{w}} \max_{||\mathbf{\epsilon}|| \le \rho} L(\mathbf{w} + \mathbf{\epsilon})$, actively seeking flat minima regions robust to weight noise.

## Level 5 — Interview Questions Solutions
### Question 1
1. Taylor expansion: $f(\mathbf{x} + \Delta \mathbf{x}) \approx f(\mathbf{x}) + \nabla f(\mathbf{x})^T \Delta \mathbf{x} + \frac{1}{2} \Delta \mathbf{x}^T \mathbf{H} \Delta \mathbf{x}$. Differentiating w.r.t $\Delta \mathbf{x}$ and setting to $\mathbf{0}$: $\nabla f(\mathbf{x}) + \mathbf{H} \Delta \mathbf{x} = \mathbf{0} \implies \Delta \mathbf{x} = -\mathbf{H}^{-1} \nabla f(\mathbf{x})$. Thus $\mathbf{x}_{t+1} = \mathbf{x}_t - \mathbf{H}^{-1} \nabla f(\mathbf{x}_t)$.
### Question 2
2. Minimizing $f(\mathbf{x})$ subject to $g(\mathbf{x}) = 0$. At constrained optimum, gradient of $f$ must be parallel to constraint gradient $\nabla g$: $\nabla f(\mathbf{x}^*) = -\lambda \nabla g(\mathbf{x}^*)$. Stationary points of Lagrangian $\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda g(\mathbf{x})$ solve constrained system.
### Question 3
3. KKT conditions for $\min f(\mathbf{x})$ s.t. $g_i(\mathbf{x}) \le 0$: 1) Stationarity $\nabla f + \sum \mu_i \nabla g_i = \mathbf{0}$, 2) Primal feasibility $g_i(\mathbf{x}) \le 0$, 3) Dual feasibility $\mu_i \ge 0$, 4) Complementary slackness $\mu_i g_i(\mathbf{x}) = 0$.
### Question 4
4. Hessian-Free optimization uses Pearlmutter's R-operator algorithm to compute directional Hessian-vector product $\mathbf{H}\mathbf{v} = \left.\frac{d}{d\epsilon} \nabla f(\mathbf{x} + \epsilon \mathbf{v})\right|_{\epsilon=0}$ in 1 extra backward pass, solving $\mathbf{H}\mathbf{p} = -g$ via Conjugate Gradient without forming $\mathbf{H}$.
### Question 5
5. Filter Normalization projects 1,000,000D neural network loss surface onto 2D random direction vectors $v_1, v_2$ normalized to match filter weight norms: $f(\alpha, \beta) = L(\mathbf{w}_0 + \alpha \frac{\mathbf{v}_1}{||\mathbf{v}_1||} ||\mathbf{w}_0|| + \beta \frac{\mathbf{v}_2}{||\mathbf{v}_2||} ||\mathbf{w}_0||)$, plotting 3D loss surface topography.
