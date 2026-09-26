# Solutions — Gradients

## Level 1 — Basic Understanding Solutions
### Question 1
1. A column vector containing all first-order partial derivatives $\nabla f = [\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}]^T$.
### Question 2
2. In the direction of steepest ascent (greatest rate of increase).
### Question 3
3. In the direction of steepest descent (greatest rate of decrease).
### Question 4
4. 

$$\nabla f = \begin{bmatrix} 10x \\ 6y^2 \end{bmatrix}$$

.
### Question 5
5. The zero vector $\mathbf{0} = [0, \dots, 0]^T$.

## Level 2 — Calculation Solutions
### Question 1
1. \frac{\partial f}{\partial x} = 2xy - 3, \frac{\partial f}{\partial y} = x^2 + 8y. At (1, 2): 

$$\nabla f(1, 2) = \begin{bmatrix} 4-3 \\ 1+16 \end{bmatrix} = \begin{bmatrix} 1 \\ 17 \end{bmatrix}$$

.
### Question 2
2. Steepest descent direction is 

$$-\nabla f(1, 2) = \begin{bmatrix} -1 \\ -17 \end{bmatrix}$$

.
### Question 3
3. $\nabla f = [4x, 6y]^T$. At $(1, 1)$, $\nabla f = [4, 6]^T$. $D_{\mathbf{u}} f = [4, 6] \cdot [0.6, 0.8]^T = 2.4 + 4.8 = 7.2$.
### Question 4
4. $\nabla f = [2x - 6, 2y + 4]^T = [0, 0]^T \implies 2x=6 \implies x=3; 2y=-4 \implies y=-2$. Critical point at $(3, -2)$.
### Question 5
5. \nabla L = [2w_1, 4w_2]^T. At (3, 2), \nabla L = [6, 8]^T. Update: 

$$\mathbf{w}_{new} = \begin{bmatrix} 3 \\ 2 \end{bmatrix} - 0.1 \begin{bmatrix} 6 \\ 8 \end{bmatrix} = \begin{bmatrix} 3 - 0.6 \\ 2 - 0.8 \end{bmatrix} = \begin{bmatrix} 2.4 \\ 1.2 \end{bmatrix}$$

.

## Level 3 — Conceptual Solutions
### Question 1
1. $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = ||\nabla f||_2 ||\mathbf{u}||_2 \cos(\theta) = ||\nabla f||_2 \cos(\theta)$. Max value occurs when $\cos(\theta) = 1 \implies \theta = 0^\circ \implies \mathbf{u}$ is parallel to $\nabla f$.
### Question 2
2. Along level set $f(\mathbf{x}) = C$, rate of change $df = 0$. Differential $df = \nabla f \cdot d\mathbf{x} = 0 \implies \nabla f$ is orthogonal to displacement $d\mathbf{x}$ along level set contour.
### Question 3
3. When contour lines are elongated ellipses (ill-conditioned Hessian), gradient vectors point almost perpendicular to optimal minimum path, causing SGD to bounce off steep walls.
### Question 4
4. Momentum accumulates past gradient direction velocity $\mathbf{v}_t$. Oscillating perpendicular components cancel out, while consistent direction components accelerate forward.
### Question 5
5. Expand $f(\mathbf{x}) = \frac{1}{2} \mathbf{x}^T \mathbf{A} \mathbf{x} - \mathbf{b}^T \mathbf{x}$. Take gradient w.r.t $\mathbf{x}$: $\nabla f(\mathbf{x}) = \mathbf{A} \mathbf{x} - \mathbf{b}$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $L(\mathbf{w}) = \frac{1}{N} (\mathbf{X}\mathbf{w} - \mathbf{y})^T (\mathbf{X}\mathbf{w} - \mathbf{y}) = \frac{1}{N} (\mathbf{w}^T \mathbf{X}^T \mathbf{X} \mathbf{w} - 2 \mathbf{w}^T \mathbf{X}^T \mathbf{y} + \mathbf{y}^T \mathbf{y})$. Differentiating w.r.t $\mathbf{w}$: $\nabla_{\mathbf{w}} L = \frac{1}{N} (2 \mathbf{X}^T \mathbf{X} \mathbf{w} - 2 \mathbf{X}^T \mathbf{y}) = \frac{2}{N} \mathbf{X}^T (\mathbf{X}\mathbf{w} - \mathbf{y})$.
### Question 2
2. Analytical gradient formula $\nabla f_{exact}$. Numerical check computes $\frac{f(x_i + h) - f(x_i - h)}{2h}$ per axis. Maximum relative error $\frac{||g_{exact} - g_{num}||}{||g_{exact}|| + ||g_{num}||} < 10^{-7}$ confirms correct gradient logic.
### Question 3
3. Adam tracks 1st moment $m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$ and 2nd moment $v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$. Corrects bias $\hat{m}_t, \hat{v}_t$, updating weights $w_{t+1} = w_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$.

## Level 5 — Interview Questions Solutions
### Question 1
1. Loss $L = -\sum y_i \ln(S_i)$. $\frac{\partial L}{\partial z_j} = -\sum_i y_i \frac{1}{S_i} \frac{\partial S_i}{\partial z_j} = -\sum_i y_i \frac{1}{S_i} S_i (\delta_{i,j} - S_j) = -\sum_i y_i (\delta_{i,j} - S_j) = -y_j + S_j \sum y_i$. Since $\sum y_i = 1$, $\frac{\partial L}{\partial z_j} = S_j - y_j \implies \nabla_{\mathbf{z}} L = \mathbf{S} - \mathbf{y}$.
### Question 2
2. Mini-batch gradient $g_B$ is a noisy estimate of full population gradient. Stochastic noise adds random thermal fluctuations that help SGD bounce out of narrow local minima and saddle points into flat wider minima with better generalization.
### Question 3
3. Euclidean gradient $\nabla L$ assumes flat parameter space. Natural gradient computes $\tilde{\nabla} L = F^{-1} \nabla L$ where $F = E[\nabla \log p \nabla \log p^T]$ is Fisher Information Matrix (Kullback-Leibler divergence metric tensor), taking optimal steps on probability distribution manifold.
### Question 4
4. Gradient clipping rescales gradients if norm exceeds threshold: if $||g||_2 > \text{threshold} \implies g_{clip} = \text{threshold} \cdot \frac{g}{||g||_2}$, preventing numerical NaN exploding updates in unrolled RNNs.
### Question 5
5. Residual connection $y = f(x) + x \implies \frac{\partial y}{\partial x} = \frac{\partial f}{\partial x} + \mathbf{I}$. Even if $\frac{\partial f}{\partial x} \to 0$, identity matrix term $\mathbf{I}$ ensures gradient flows backward uninterrupted.
