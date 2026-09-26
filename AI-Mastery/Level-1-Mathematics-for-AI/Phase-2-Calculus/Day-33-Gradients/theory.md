# Theory — Gradients

### 1. Simple Definition
The gradient is a vector that gathers all the partial derivatives of a function into a single directional arrow. It points in the direction of steepest increase (steepest uphill slope).

### 2. Intuition
If you drop a ball on a 3D terrain loss surface, gravity pulls it in the direction of steepest downhill slope. That downhill direction is the NEGATIVE gradient vector $-\nabla f$!

### 3. Mathematical Definition
For scalar function $f: \mathbb{R}^n \rightarrow \mathbb{R}$, the gradient vector $\nabla f(\mathbf{x}) \in \mathbb{R}^n$ is:

$$
\nabla f(\mathbf{x}) = \text{grad}(f) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}
$$

### 4. Notation
$\nabla f(\mathbf{x})$ or $\text{grad}(f)$. Column vector of partial derivatives.

### 5. Formula

$$
D_{\mathbf{u}} f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u} = ||\nabla f(\mathbf{x})||_2 ||\mathbf{u}||_2 \cos(\theta)
$$

$$
\text{Max rate of change occurs when } \cos(\theta) = 1 \implies \mathbf{u} \text{ aligns with } \nabla f
$$

### 6. Symbol-by-Symbol Explanation
- $\nabla$: Nabla operator $(\frac{\partial}{\partial x_1}, \dots, \frac{\partial}{\partial x_n})^T$
- $D_{\mathbf{u}} f$: Directional derivative along unit vector $\mathbf{u}$
- $\theta$: Angle between unit direction $\mathbf{u}$ and gradient $\nabla f$

### 7. Step-by-Step Calculation
Calculate gradient of $f(x, y) = x^2 + 3y^2$ at point $(2, 1)$:
1. Partial w.r.t $x$: $\frac{\partial f}{\partial x} = 2x$.
2. Partial w.r.t $y$: $\frac{\partial f}{\partial y} = 6y$.
3. Gradient vector: 

$$
\nabla f(x, y) = \begin{bmatrix} 2x \\ 6y \end{bmatrix}
$$

.
4. Evaluate at (2, 1): 

$$
\nabla f(2, 1) = \begin{bmatrix} 2(2) \\ 6(1) \end{bmatrix} = \begin{bmatrix} 4 \\ 6 \end{bmatrix}
$$

.
Steepest uphill direction is along vector $[4, 6]^T$. Steepest descent direction is $[-4, -6]^T$.

### 8. Second Example
Directional derivative at $(2, 1)$ along unit vector $\mathbf{u} = [1/\sqrt{2}, 1/\sqrt{2}]^T$:
$D_{\mathbf{u}} f(2, 1) = \nabla f \cdot \mathbf{u} = [4, 6] \cdot [1/\sqrt{2}, 1/\sqrt{2}]^T = \frac{4+6}{\sqrt{2}} = \frac{10}{\sqrt{2}} \approx 7.071$.

### 9. Common Mistakes
Confusing gradient (vector of partial derivatives) with derivative of single variable (scalar); thinking gradient points downhill (gradient points UPHILL, negative gradient points DOWNHILL!).

### 10. AI Connection
Gradient Descent Parameter Update: $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$. Subtracting $\eta \nabla L$ steps downhill toward lower loss.

### 11. Algorithm Connection
Gradient Descent, Stochastic Gradient Descent (SGD), Adam, RMSprop, Momentum, Conjugate Gradient.

### 12. Practical Interpretation
The magnitude of the gradient $||\nabla f||_2$ measures the exact steepness of the slope at that point. At a minimum or maximum, $||\nabla f||_2 = 0$.

### 13. Interview Insight
Q: 'Why is the gradient vector always perpendicular (orthogonal) to contour lines (level sets)?' A: Along a contour line $f(x, y) = c$, function output doesn't change ($df = 0$). Since $df = \nabla f \cdot d\mathbf{r} = 0$, $\nabla f$ must be perpendicular to displacement vector $d\mathbf{r}$ along contour.

### 14. Summary
Gradient vector $\nabla f = [\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}]^T$ points in direction of steepest ascent. Negative gradient $-\nabla f$ drives model weight optimization in steepest descent.
