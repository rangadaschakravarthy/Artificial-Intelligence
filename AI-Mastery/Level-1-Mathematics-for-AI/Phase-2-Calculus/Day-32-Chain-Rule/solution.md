# Solutions — Chain Rule

## Level 1 — Basic Understanding Solutions
### Question 1
1. $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$.
### Question 2
2. Let $u = x^2+3 \implies y = u^5$. $\frac{dy}{dx} = 5u^4 (2x) = 10x(x^2+3)^4$.
### Question 3
3. $4 e^{4x}$.
### Question 4
4. $\frac{1}{5x} \cdot 5 = \frac{1}{x}$.
### Question 5
5. Because neural networks are multi-layered composite functions; Chain Rule allows computing derivatives w.r.t early layer weights by multiplying layer-by-layer derivatives backward.

## Level 2 — Calculation Solutions
### Question 1
1. $\cos(x^3) \cdot 3x^2 = 3x^2 \cos(x^3)$.
### Question 2
2. $4(3x^2-2x+1)^3 (6x - 2)$.
### Question 3
3. $\frac{\partial z}{\partial u} = 2u, \frac{du}{dt} = 2$; $\frac{\partial z}{\partial v} = 2v, \frac{dv}{dt} = 3$. $\frac{dz}{dt} = 2u(2) + 2v(3) = 4(2t) + 6(3t) = 8t + 18t = 26t$.
### Question 4
4. $f'(x) = \sigma'(2x+3) \cdot 2 = 2 \sigma(2x+3)(1 - \sigma(2x+3))$. At $x=0$, $2x+3=3$. $\sigma(3) \approx 0.9526 \implies 2(0.9526)(0.0474) \approx 0.0903$.
### Question 5
5. $e^{-x^2/2} (-x) = -x e^{-x^2/2}$.

## Level 3 — Conceptual Solutions
### Question 1
1. $\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x}$.
### Question 2
2. Nodes: $w, b, x \to z = wx+b \to \text{err} = z-y \to L = \text{err}^2$. $\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \text{err}} \frac{\partial \text{err}}{\partial z} \frac{\partial z}{\partial w} = 2(z-y) \cdot 1 \cdot x = 2(wx+b-y)x$. $\frac{\partial L}{\partial b} = 2(wx+b-y)$.
### Question 3
3. Let $u = \sigma(z) \implies L = -\ln(u)$. $\frac{dL}{dz} = \frac{dL}{du} \frac{du}{dz} = -\frac{1}{u} \cdot u(1-u) = -(1-u) = u - 1 = \sigma(z) - 1$.
### Question 4
4. Chain rule multiplies derivatives across 50 layers: $\prod_{l=1}^{50} \sigma'(z_l)$. Since $\sigma'(z) \le 0.25$, $0.25^{50} \approx 10^{-30} \to 0$, causing early layer weight updates to completely vanish.
### Question 5
5. Forward-mode AD computes derivatives along forward graph pass ($O(N_{inputs})$ ops). Reverse-mode AD runs forward pass to cache values, then propagates derivatives backward in 1 pass ($O(N_{outputs})$ ops, perfect for 1 scalar Loss $L$).

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\frac{\partial L}{\partial w_2} = (\hat{y} - y) \sigma'(z_2) h_1$. $\frac{\partial L}{\partial w_1} = (\hat{y} - y) \sigma'(z_2) w_2 \sigma'(z_1) x$.
### Question 2
2. $z_1 = 0.5(1)+0=0.5 \implies h_1 = \sigma(0.5) \approx 0.6225$. $z_2 = 1.0(0.6225)+0=0.6225 \implies \hat{y} = \sigma(0.6225) \approx 0.6508$. Error $(\hat{y}-y) = 0.6508-1.0 = -0.3492$. $\sigma'(z_2) = 0.6508(1-0.6508) \approx 0.2273$. $\sigma'(z_1) = 0.6225(1-0.6225) \approx 0.2350$. $\frac{\partial L}{\partial w_1} = (-0.3492)(0.2273)(1.0)(0.2350)(1.0) \approx -0.0186$.
### Question 3
3. During forward pass, PyTorch wraps created tensors in nodes recording operator function reference and pointers to input parent tensors. `.backward()` executes registered backward derivative closures in reverse topological sort order.

## Level 5 — Interview Questions Solutions
### Question 1
1. Let $\mathbf{Z}_1 = \mathbf{X}\mathbf{W}_1 + \mathbf{b}_1, \mathbf{H}_1 = \sigma(\mathbf{Z}_1), \mathbf{Z}_2 = \mathbf{H}_1\mathbf{W}_2 + \mathbf{b}_2$. $\frac{\partial L}{\partial \mathbf{Z}_1} = \frac{\partial L}{\partial \mathbf{H}_1} \odot \sigma'(\mathbf{Z}_1) = (\frac{\partial L}{\partial \mathbf{Z}_2} \mathbf{W}_2^T) \odot \sigma'(\mathbf{Z}_1)$. Then $\frac{\partial L}{\partial \mathbf{W}_1} = \mathbf{X}^T \frac{\partial L}{\partial \mathbf{Z}_1}$.
### Question 2
2. Jacobian $J_{m \times n}$. JVP computes $J v$ (multiplying Jacobian by vector $v$ in forward AD). VJP computes $v^T J = (J^T v)^T$ (multiplying transposed Jacobian by vector $v$ in reverse AD).
### Question 3
3. BPTT unrolls RNN across $T$ time steps: $h_t = f(W_{hh} h_{t-1} + W_{xh} x_t)$. Gradient $\frac{\partial L}{\partial W_{hh}} = \sum_{t=1}^T \sum_{k=1}^t \frac{\partial L_t}{\partial h_t} \frac{\partial h_t}{\partial h_k} \frac{\partial h_k}{\partial W_{hh}}$, accumulating gradients across all unrolled time steps.
### Question 4
4. Forward AD evaluates $J v_k$ for unit basis vector $e_k$, returning column $k$ of $J$. Reverse AD evaluates $v_k^T J$ for unit vector $e_k$, returning row $k$ of $J$. Since ML has 1 loss output ($m=1$), Reverse AD evaluates full gradient in 1 pass.
### Question 5
5. Gradient Checkpointing drops intermediate activation tensors from RAM during forward pass, recomputing them on-demand during backward pass. Saves 70-80% VRAM at cost of ~20-30% extra forward computation.
