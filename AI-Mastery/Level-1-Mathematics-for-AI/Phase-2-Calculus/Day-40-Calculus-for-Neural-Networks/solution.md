# Solutions — Calculus for Neural Networks

## Level 1 — Basic Understanding Solutions
### Question 1
1. $\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}, \mathbf{a}^{(l)} = \sigma(\mathbf{z}^{(l)})$.
### Question 2
2. Vector of partial derivatives of loss w.r.t pre-activations: $\mathbf{\delta}^{(l)} = \frac{\partial L}{\partial \mathbf{z}^{(l)}}$.
### Question 3
3. $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$.
### Question 4
4. $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$.
### Question 5
5. $\text{ReLU}'(x) = 1$ if $x > 0$, and $0$ if $x < 0$ (undefined/0 at $x=0$).

## Level 2 — Calculation Solutions
### Question 1
1. Output delta $\delta^{(2)} = a^{(2)} - y = 0.9 - 1.0 = -0.1$.
### Question 2
2. $\frac{\partial L}{\partial \mathbf{W}^{(2)}} = -0.1 [0.4, 0.8] = [-0.04, -0.08]$.
### Question 3
3. $\mathbf{W}^{(2)T} \delta^{(2)} = \begin{bmatrix} 1.5 \\ -2.0 \end{bmatrix} (-0.1) = \begin{bmatrix} -0.15 \\ 0.20 \end{bmatrix}$. $\mathbf{\delta}^{(1)} = \begin{bmatrix} -0.15 \\ 0.20 \end{bmatrix} \odot \begin{bmatrix} 0.2 \\ 0.2 \end{bmatrix} = \begin{bmatrix} -0.03 \\ 0.04 \end{bmatrix}$.
### Question 4
4. $\text{ReLU}'(\mathbf{z}) = [0, 1, 0]^T$.
### Question 5
5. Because activation derivatives $\sigma'(\mathbf{z}^{(l)})$ evaluated during backward pass require pre-activation values $\mathbf{z}^{(l)}$ computed during forward pass.

## Level 3 — Conceptual Solutions
### Question 1
1. Loss $L = -\sum y_k \ln(a_k^{(L)})$. $\delta_i^{(L)} = \frac{\partial L}{\partial z_i^{(L)}} = \sum_k \frac{\partial L}{\partial a_k^{(L)}} \frac{\partial a_k^{(L)}}{\partial z_i^{(L)}} = \sum_k \left(-\frac{y_k}{a_k^{(L)}}\right) a_k^{(L)}(\delta_{k,i} - a_i^{(L)}) = -y_i + a_i^{(L)} \sum y_k = a_i^{(L)} - y_i$. Vector form: $\mathbf{\delta}^{(L)} = \mathbf{a}^{(L)} - \mathbf{y}$.
### Question 2
2. By chain rule: $\frac{\partial L}{\partial W_{i,j}^{(l)}} = \frac{\partial L}{\partial z_i^{(l)}} \frac{\partial z_i^{(l)}}{\partial W_{i,j}^{(l)}} = \delta_i^{(l)} a_j^{(l-1)}$. Matrix outer product form: $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$.
### Question 3
3. Standard ReLU has 0 derivative for $x < 0$, deactivating neurons permanently if weights push $z < 0$ (Dying ReLU). LeakyReLU has small non-zero slope $0.01$ for $x < 0$, ensuring non-zero error deltas always propagate.
### Question 4
4. $\text{tanh}'(x) = 1 - \text{tanh}^2(x)$ maxes out at $1.0$ at $x=0$, whereas $\sigma'(x)$ maxes out at $0.25$. Tanh provides 4x larger gradient signals than Sigmoid, easing deep network training.
### Question 5
5. For mini-batch activation matrix $\mathbf{A}^{(l-1)}_{B \times d_{in}}$ and error delta matrix $\mathbf{\Delta}^{(l)}_{B \times d_{out}}$, weight gradient matrix is computed in 1 matrix product: $\nabla_{\mathbf{W}^{(l)}} = \mathbf{\Delta}^{(l)T} \mathbf{A}^{(l-1)}$ (shape $d_{out} \times d_{in}$).

## Level 4 — AI/ML Application Solutions
### Question 1
1. Implement 2-layer MLP class (`W1, b1, W2, b2`). `forward()` computes $z_1, a_1 = \text{sigmoid}(z_1), z_2, a_2 = \text{sigmoid}(z_2)$. `backward()` computes $\delta_2 = a_2 - y$, $dW_2 = \delta_2 a_1^T$, $\delta_1 = (W_2^T \delta_2) * a_1(1-a_1)$, $dW_1 = \delta_1 x^T$. Updates weights via SGD. Loss decays to $<0.01$ on XOR.
### Question 2
2. In $L$-layer network, hidden delta $\mathbf{\delta}^{(1)} = (\prod_{l=2}^L \mathbf{W}^{(l)T} \text{diag}(\sigma'(\mathbf{z}^{(l)}))) \mathbf{\delta}^{(L)}$. For Sigmoid, $\sigma' \le 0.25$. Product of $L=50$ terms yields $0.25^{50} \approx 10^{-30} \to 0$ (Vanishing Gradient). For ReLU, $\text{ReLU}' \in \{0, 1\}$, eliminating decay factor $0.25^L$.
### Question 3
3. If weight variance is too small, activations shrink to 0. If weight variance is too large ($||W|| > 1$), gradient product $\prod W^{(l)T}$ grows exponentially $c^L \to \infty$ (Exploding Gradient). He initialization sets $W \sim \mathcal{N}(0, \frac{2}{n_{in}})$, preserving activation and gradient variance $\text{Var}(z^{(l)}) = \text{Var}(a^{(l-1)})$ across all layers.

## Level 5 — Interview Questions Solutions
### Question 1
1. Forward: $\mathbf{Z}^{(1)}_{B \times d_1} = \mathbf{X}_{B \times d_0} \mathbf{W}^{(1)T}_{d_0 \times d_1} + \mathbf{b}^{(1)}$, $\mathbf{A}^{(1)} = \sigma(\mathbf{Z}^{(1)})$, $\mathbf{Z}^{(2)}_{B \times d_2} = \mathbf{A}^{(1)} \mathbf{W}^{(2)T}_{d_1 \times d_2} + \mathbf{b}^{(2)}$, $\mathbf{A}^{(2)} = \text{Softmax}(\mathbf{Z}^{(2)})$. Output Delta: $\mathbf{\Delta}^{(2)}_{B \times d_2} = \mathbf{A}^{(2)} - \mathbf{Y}$. Hidden Delta: $\mathbf{\Delta}^{(1)}_{B \times d_1} = (\mathbf{\Delta}^{(2)} \mathbf{W}^{(2)}_{d_2 \times d_1}) \odot \sigma'(\mathbf{Z}^{(1)})$. Gradients: $\nabla_{\mathbf{W}^{(2)}} = \mathbf{\Delta}^{(2)T} \mathbf{A}^{(1)}$, $\nabla_{\mathbf{b}^{(2)}} = \sum_{rows} \mathbf{\Delta}^{(2)}$, $\nabla_{\mathbf{W}^{(1)}} = \mathbf{\Delta}^{(1)T} \mathbf{X}$, $\nabla_{\mathbf{b}^{(1)}} = \sum_{rows} \mathbf{\Delta}^{(1)}$. Perfect batch matrix calculus!
### Question 2
2. In RNNs $h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t)$, hidden delta recurrence propagates across time steps: $\delta_t = \frac{\partial L}{\partial h_t} = \frac{\partial L_t}{\partial h_t} + W_{hh}^T (\delta_{t+1} \odot \text{tanh}'(z_{t+1}))$. Unrolled chain rule sums error deltas backward through time.
### Question 3
3. BatchNorm gradient $\frac{\partial L}{\partial x_i} = \frac{1}{B \sigma_B} \left( \frac{\partial L}{\partial \hat{x}_i} - \frac{1}{B} \sum_j \frac{\partial L}{\partial \hat{x}_j} - \hat{x}_i \frac{1}{B} \sum_j \frac{\partial L}{\partial \hat{x}_j} \hat{x}_j \right)$. Combines direct activation gradient with mean and variance normalization terms.
### Question 4
4. Forward conv: $Y = X * K$. Error delta map $\Delta_Y = \frac{\partial L}{\partial Y}$. Kernel weight gradient $\nabla_K = X * \Delta_Y$ (cross-correlation of input map $X$ with error delta map $\Delta_Y$). Input error delta $\Delta_X = \Delta_Y * K^{rot180}$ (full convolution of delta map with 180-degree rotated kernel).
### Question 5
5. Gradient Checkpointing drops intermediate activation matrices $\mathbf{A}^{(l)}$ from VRAM during forward pass. During backward pass, when computing layer $l$ deltas, it executes a local mini-forward pass from nearest saved checkpoint layer $k$ to recompute $\mathbf{A}^{(l)}$ on-the-fly, reducing peak memory from $O(L)$ to $O(\sqrt{L})$.
