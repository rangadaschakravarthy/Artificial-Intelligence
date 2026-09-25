# Solutions — Partial Derivatives

## Level 1 — Basic Understanding Solutions
### Question 1
1. A derivative w.r.t one variable in a multi-variable function while treating all other variables as fixed constants.
### Question 2
2. $\frac{\partial f}{\partial x} = 4(3x^2)y^2 = 12 x^2 y^2$.
### Question 3
3. $\frac{\partial f}{\partial y} = 4x^3 (2y) = 8 x^3 y$.
### Question 4
4. Mixed partial derivatives are equal ($f_{xy} = f_{yx}$) if second derivatives are continuous.
### Question 5
5. Treat $y$ as a constant number (like 5 or $\pi$).

## Level 2 — Calculation Solutions
### Question 1
1. $\frac{\partial f}{\partial x} = 2xy + \cos(x)$. $\frac{\partial f}{\partial y} = x^2 + e^y$.
### Question 2
2. $\frac{\partial f}{\partial x} = 10xy - 2y^3$. At $(1, 3)$: $10(1)(3) - 2(27) = 30 - 54 = -24$.
### Question 3
3. $f_x = 3x^2 y^4 \implies f_{xx} = 6x y^4$. $f_y = 4x^3 y^3 \implies f_{yy} = 12x^3 y^2$.
### Question 4
4. $f_{xy} = \frac{\partial}{\partial y}[3x^2 y^4] = 12x^2 y^3$. $f_{yx} = \frac{\partial}{\partial x}[4x^3 y^3] = 12x^2 y^3$. Equal!
### Question 5
5. $\frac{\partial L}{\partial w_1} = 2w_1 - 4w_2$. $\frac{\partial L}{\partial w_2} = 6w_2 - 4w_1$.

## Level 3 — Conceptual Solutions
### Question 1
1. $f_x = y e^{xy}$, $f_y = x e^{xy}$. $f_{xx} = y^2 e^{xy}$, $f_{yy} = x^2 e^{xy}$. $f_{xy} = f_{yx} = e^{xy} + xy e^{xy} = e^{xy}(1+xy)$.
### Question 2
2. Total differential $df$ combines linear approximation contributions of tiny changes $dx$ and $dy$ along each dimension.
### Question 3
3. $\frac{\partial f}{\partial x} = 2x - 4 = 0 \implies x = 2$. $\frac{\partial f}{\partial y} = 2y - 6 = 0 \implies y = 3$. Critical point at $(2, 3)$.
### Question 4
4. Backpropagation applies chain rule across multi-variable layer connections, requiring partial derivatives w.r.t each weight matrix entry.
### Question 5
5. Directional derivative $D_{\mathbf{u}} f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u}$ measures rate of change along any unit vector direction $\mathbf{u}$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\frac{\partial L}{\partial w} = \frac{2}{N} \sum (w x_i + b - y_i) x_i$. $\frac{\partial L}{\partial b} = \frac{2}{N} \sum (w x_i + b - y_i)$.
### Question 2
2. System: $w \sum x_i^2 + b \sum x_i = \sum x_i y_i$ and $w \sum x_i + N b = \sum y_i$. Solving this $2 \times 2$ matrix system yields closed-form OLS solutions for $w$ and $b$.
### Question 3
3. PyTorch builds dynamic execution graph during forward pass. `backward()` calculates partial derivatives $\frac{\partial L}{\partial w_i}$ for each tensor weight, accumulating values into `.grad` fields.

## Level 5 — Interview Questions Solutions
### Question 1
1. Define $g(h) = f(x+h, y+k) - f(x+h, y) - f(x, y+k) + f(x, y)$. Apply Mean Value Theorem twice to show limit as $h, k \to 0$ forces $f_{xy}(x, y) = f_{yx}(x, y)$.
### Question 2
2. Hessian matrix $\mathbf{H} \in \mathbb{R}^{n \times n}$ contains all second partial derivatives $H_{i,j} = \frac{\partial^2 f}{\partial x_i \partial x_j}$, describing local curvature of multi-variable loss surfaces.
### Question 3
3. Discriminant $D = f_{xx} f_{yy} - (f_{xy})^2 = \det(\mathbf{H})$. If $D > 0$ and $f_{xx} > 0 \implies$ Local Minimum. If $D > 0$ and $f_{xx} < 0 \implies$ Local Maximum. If $D < 0 \implies$ Saddle Point.
### Question 4
4. PINNs incorporate known partial differential equations directly into loss functions $L_{PINN} = L_{data} + \lambda L_{PDE}$, ensuring neural network predictions satisfy physical laws (e.g. $\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = \nu \frac{\partial^2 u}{\partial x^2}$).
### Question 5
5. For $L = |w_1| + |w_2|$, subgradient vector is $\mathbf{g} = [\text{sign}(w_1), \text{sign}(w_2)]^T$. At $w_i = 0$, subgradient set is $[-1, 1]$.
