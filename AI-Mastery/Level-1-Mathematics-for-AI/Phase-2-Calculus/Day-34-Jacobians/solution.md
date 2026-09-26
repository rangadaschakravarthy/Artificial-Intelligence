# Solutions — Jacobians

## Level 1 — Basic Understanding Solutions
### Question 1
1. A matrix containing all first-order partial derivatives of a vector-valued function $J_{i,j} = \frac{\partial f_i}{\partial x_j}$.
### Question 2
2. Shape is $2 \times 3$ ($m=2$ outputs, $n=3$ inputs).
### Question 3
3. Row 1: $[1, 1]$. Row 2: $[2y, 2x]$.
### Question 4
4. The matrix $\mathbf{A}$ itself.
### Question 5
5. The transformation preserves volume (neither expands nor contracts spatial volume).

## Level 2 — Calculation Solutions
### Question 1
1. 

$$
\mathbf{J} = \begin{bmatrix} 2x & 2y \\ 3y & 3x \end{bmatrix}
$$

. At (1, 2): 

$$
\mathbf{J}(1, 2) = \begin{bmatrix} 2 & 4 \\ 6 & 3 \end{bmatrix}
$$

.
### Question 2
2. 

$$
\mathbf{J} = \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix} \implies \det(\mathbf{J}) = r\cos^2\theta - (-r\sin^2\theta) = r(\cos^2\theta + \sin^2\theta) = r
$$

.
### Question 3
3. Shape 2 \times 3. 

$$
\mathbf{J} = \begin{bmatrix} 2x_1 & 0 & 0 \\ 0 & x_3 & x_2 \end{bmatrix}
$$

.
### Question 4
4. 

$$
\mathbf{J} = \begin{bmatrix} S_1(1-S_1) & -S_1 S_2 \\ -S_1 S_2 & S_2(1-S_2) \end{bmatrix}
$$

.
### Question 5
5. $\mathbf{f}(\mathbf{x}) \approx \mathbf{f}(\mathbf{x}_0) + \mathbf{J}(\mathbf{x}_0)(\mathbf{x} - \mathbf{x}_0)$.

## Level 3 — Conceptual Solutions
### Question 1
1. Apply single-variable chain rule to component $(J_h)_{i,k} = \frac{\partial f_i}{\partial x_k} = \sum_j \frac{\partial f_i}{\partial g_j} \frac{\partial g_j}{\partial x_k} = (J_f J_g)_{i,k}$. Matches matrix product $J_f J_g$!
### Question 2
2. For $1,000,000$ inputs and $1,000,000$ outputs, Jacobian matrix contains $10^{12}$ entries (4 Terabytes RAM), making explicit storage impossible.
### Question 3
3. VJP $v^T J$ multiplies loss gradient row vector $v_{1 \times m}$ by Jacobian $J_{m \times n}$, yielding $1 \times n$ gradient vector in 1 backward pass without building full $J$.
### Question 4
4. JVP $J v$ multiplies Jacobian $J_{m \times n}$ by input direction vector $v_{n \times 1}$, computing directional output derivative vector in 1 forward pass.
### Question 5
5. Generative sampling requires inverting transformation $\mathbf{z} = g^{-1}(\mathbf{x})$, and density evaluation requires computing $\log |\det \mathbf{J}_g|$, demanding fast inverted transforms and $O(n)$ determinants.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Partial derivatives: \frac{\partial y_1}{\partial x_1} = 1, \frac{\partial y_1}{\partial x_2} = 0; \frac{\partial y_2}{\partial x_1} = x_2 s'(x_1) e^{s(x_1)} + t'(x_1), \frac{\partial y_2}{\partial x_2} = e^{s(x_1)}. Lower triangular Jacobian 

$$
\mathbf{J} = \begin{bmatrix} 1 & 0 \\ \text{stuff} & e^{s(x_1)} \end{bmatrix} \implies \det(\mathbf{J}) = 1 \cdot e^{s(x_1)} = e^{s(x_1)}
$$

.
### Question 2
2. Let $\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b}$. $\mathbf{J}_{h, x} = \frac{\partial \mathbf{h}}{\partial \mathbf{z}} \frac{\partial \mathbf{z}}{\partial \mathbf{x}} = \text{diag}(\text{ReLU}'(\mathbf{z})) \mathbf{W}$.
### Question 3
3. `torch.autograd.functional.jacobian(func, inputs)` evaluates full Jacobian matrix of `func` at `inputs` using repeated VJP/JVP passes.

## Level 5 — Interview Questions Solutions
### Question 1
1. Probability conservation: $p_X(x) |dx| = p_Z(z) |dz|$. Since $x = g(z) \implies |dx| = |\det J_g| |dz| \implies p_X(x) = p_Z(z) / |\det J_g(z)| = p_Z(g^{-1}(x)) |\det J_{g^{-1}}(x)|$.
### Question 2
2. Neural ODE defines continuous transformation $\frac{dz}{dt} = f(z, t)$. Jacobi's formula for matrix determinant derivative yields instantaneous change of log-density $\frac{d \log p(z(t))}{d t} = -\text{Tr}\left(\frac{\partial f}{\partial z}\right)$, evaluated using Hutchinson's trace estimator.
### Question 3
3. Autoregressive flows enforce lower triangular Jacobian $J_{i,j} = 0$ for $j > i$. Determinant is simple product of diagonal elements $\prod J_{i,i}$.
### Question 4
4. Jacobian regularization adds penalty $L_{reg} = \lambda ||\mathbf{J}_f(\mathbf{x})||_F^2$ to loss, penalizing model output sensitivity to input perturbations and boosting adversarial robustness against FGSM attacks.
### Question 5
5. Singular values $\sigma_i$ of local Jacobian matrix $\mathbf{J}(\mathbf{x}_0)$ measure maximum directional stretch ratios along right singular vectors $\mathbf{v}_i$, mapping local unit hyperspheres into ellipses.
