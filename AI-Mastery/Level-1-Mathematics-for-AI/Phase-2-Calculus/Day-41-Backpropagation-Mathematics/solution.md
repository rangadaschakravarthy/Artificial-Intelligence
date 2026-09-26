# Solutions — Backpropagation Mathematics

## Level 1 — Basic Understanding Solutions
### Question 1
1. Eq 1: $\mathbf{\delta}^{(L)} = \nabla_{\mathbf{a}} L \odot \sigma'(\mathbf{z}^{(L)})$. Eq 2: $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$. Eq 3: $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \mathbf{\delta}^{(l)}$. Eq 4: $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$.
### Question 2
2. Layer error delta vector $\mathbf{\delta}^{(l)} = \frac{\partial L}{\partial \mathbf{z}^{(l)}}$, representing partial derivatives of loss w.r.t pre-activation vector $\mathbf{z}^{(l)}$.
### Question 3
3. Hadamard product (element-wise vector multiplication).
### Question 4
4. Transposing $\mathbf{W}^{(l+1)}$ flips its dimensions from $(n_{l+1} \times n_l)$ to $(n_l \times n_{l+1})$, allowing matrix multiplication with error vector $\mathbf{\delta}^{(l+1)}$ of shape $(n_{l+1} \times 1)$ to produce output shape $(n_l \times 1)$.
### Question 5
5. $\mathbf{\delta}^{(L)} = \mathbf{a}^{(L)} - \mathbf{y}$ (since $\sigma'(z) = 1$ and $\nabla_{\mathbf{a}} L = \mathbf{a}^{(L)} - \mathbf{y}$).

## Level 2 — Calculation Solutions
### Question 1
1. 

$$\mathbf{W}^{(2)T} \mathbf{\delta}^{(2)} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 0.2 \\ -0.4 \end{bmatrix} = \begin{bmatrix} 0.2 - 0.8 \\ 0.6 - 1.6 \end{bmatrix} = \begin{bmatrix} -0.6 \\ -1.0 \end{bmatrix}$$

. 

$$\mathbf{\delta}^{(1)} = \begin{bmatrix} -0.6 \\ -1.0 \end{bmatrix} \odot \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix} = \begin{bmatrix} -0.3 \\ -0.5 \end{bmatrix}$$

.
### Question 2
2. 

$$\frac{\partial L}{\partial \mathbf{W}^{(1)}} = \mathbf{\delta}^{(1)} \mathbf{x}^T = \begin{bmatrix} -0.1 \\ 0.3 \end{bmatrix} [2, 5] = \begin{bmatrix} -0.2 & -0.5 \\ 0.6 & 1.5 \end{bmatrix}$$

.
### Question 3
3. Order: $\mathbf{\delta}^{(5)} \rightarrow \mathbf{\delta}^{(4)} \rightarrow \mathbf{\delta}^{(3)} \rightarrow \mathbf{\delta}^{(2)} \rightarrow \mathbf{\delta}^{(1)}$.
### Question 4
4. 1D scalar chain rule: $\delta^{(1)} = \frac{\partial L}{\partial z_1} = \frac{\partial L}{\partial z_2} \frac{\partial z_2}{\partial a_1} \frac{\partial a_1}{\partial z_1} = \delta^{(2)} w_2 \sigma'(z_1)$.
### Question 5
5. $O(W)$ operations (proportional to total number of weights $W$), identical complexity to forward pass!

## Level 3 — Conceptual Solutions
### Question 1
1. $L = \frac{1}{2} \sum (a_k^{(L)} - y_k)^2 \implies \frac{\partial L}{\partial a_i^{(L)}} = (a_i^{(L)} - y_i)$. By chain rule: $\delta_i^{(L)} = \frac{\partial L}{\partial z_i^{(L)}} = \frac{\partial L}{\partial a_i^{(L)}} \frac{\partial a_i^{(L)}}{\partial z_i^{(L)}} = (a_i^{(L)} - y_i) \sigma'(z_i^{(L)})$. Vector form: $\mathbf{\delta}^{(L)} = (\mathbf{a}^{(L)} - \mathbf{y}) \odot \sigma'(\mathbf{z}^{(L)})$. Q.E.D.
### Question 2
2. $z_i^{(l)} = \sum_j W_{i,j}^{(l)} a_j^{(l-1)} + b_i^{(l)}$. Partial w.r.t $b_i^{(l)}$ is $\frac{\partial z_i^{(l)}}{\partial b_i^{(l)}} = 1$. By chain rule: $\frac{\partial L}{\partial b_i^{(l)}} = \frac{\partial L}{\partial z_i^{(l)}} \frac{\partial z_i^{(l)}}{\partial b_i^{(l)}} = \delta_i^{(l)} \cdot 1 = \delta_i^{(l)}$. Vector form: $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \mathbf{\delta}^{(l)}$. Q.E.D.
### Question 3
3. Partial w.r.t $W_{i,j}^{(l)}$ is $\frac{\partial z_i^{(l)}}{\partial W_{i,j}^{(l)}} = a_j^{(l-1)}$. By chain rule: $\frac{\partial L}{\partial W_{i,j}^{(l)}} = \frac{\partial L}{\partial z_i^{(l)}} \frac{\partial z_i^{(l)}}{\partial W_{i,j}^{(l)}} = \delta_i^{(l)} a_j^{(l-1)}$. Matrix outer product form: $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$. Q.E.D.
### Question 4
4. Forward-mode AD evaluates derivatives w.r.t 1 input parameter per pass ($O(N_{params})$ passes). Reverse-mode AD evaluates derivatives w.r.t ALL parameters in 1 backward pass ($O(1)$ pass), making it essential for models with millions of parameters.
### Question 5
5. Mini-batch dataset matrix $\mathbf{X}_{B \times d_0}$. Activations $\mathbf{A}^{(l)}_{B \times d_l}$, pre-activations $\mathbf{Z}^{(l)}_{B \times d_l}$, error deltas $\mathbf{\Delta}^{(l)}_{B \times d_l}$. Recurrence: $\mathbf{\Delta}^{(l)} = (\mathbf{\Delta}^{(l+1)} \mathbf{W}^{(l+1)}) \odot \sigma'(\mathbf{Z}^{(l)})$. Weight gradients: $\nabla_{\mathbf{W}^{(l)}} = \mathbf{\Delta}^{(l)T} \mathbf{A}^{(l-1)}$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Forward: 

$$z_1 = \begin{bmatrix}0.1&0.2\\0.3&0.4\end{bmatrix} \begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}0.3\\0.7\end{bmatrix}$$

. 

$$a_1 = \begin{bmatrix}\sigma(0.3)\\\sigma(0.7)\end{bmatrix} = \begin{bmatrix}0.5744\\0.6682\end{bmatrix}$$

. 

$$z_2 = [0.5, 0.6] \begin{bmatrix}0.5744\\0.6682\end{bmatrix} = 0.2872 + 0.4009 = 0.6881$$

. a_2 = \sigma(0.6881) = 0.6655. Loss = 0.5(0.6655 - 1.0)^2 = 0.0559. Output Delta: \delta_2 = (0.6655 - 1.0) \sigma'(0.6881) = (-0.3345)(0.6655)(0.3345) = -0.0744. Hidden Delta: 

$$\mathbf{W}^{(2)T} \delta_2 = \begin{bmatrix}0.5\\0.6\end{bmatrix} (-0.0744) = \begin{bmatrix}-0.0372\\-0.0446\end{bmatrix}$$

. 

$$\sigma'(z_1) = \begin{bmatrix}0.2444\\0.2217\end{bmatrix}$$

. 

$$\delta_1 = \begin{bmatrix}-0.0372(0.2444)\\-0.0446(0.2217)\end{bmatrix} = \begin{bmatrix}-0.0091\\-0.0099\end{bmatrix}$$

. Gradients: dW_2 = \delta_2 a_1^T = -0.0744 [0.5744, 0.6682] = [-0.0427, -0.0497]. 

$$dW_1 = \delta_1 x^T = \begin{bmatrix}-0.0091\\-0.0099\end{bmatrix} [1, 1] = \begin{bmatrix}-0.0091&-0.0091\\-0.0099&-0.0099\end{bmatrix}$$

.
### Question 2
2. Python script executes forward and backward pass formulas above, printing values matching hand calculation to 4 decimal places.
### Question 3
3. PyTorch builds Directed Acyclic Graph (DAG) of `Node` objects during forward pass. Calling `loss.backward()` executes topological sort on DAG, running registered `backward()` C++ functions sequentially.

## Level 5 — Interview Questions Solutions
### Question 1
1. Conv layer $Y_{m,n} = \sum_{i,j} X_{m+i, n+j} K_{i,j}$. Input error delta $\delta_X = \frac{\partial L}{\partial X}$. By chain rule, error delta propagates backward as full 2D convolution of output delta $\delta_Y$ with 180-degree flipped kernel: $\delta_X = \text{conv2d}_{full}(\delta_Y, K_{rot180})$. Kernel gradient $dW = \text{cross\_correlation}(X, \delta_Y)$.
### Question 2
2. BPTT unrolls RNN over $T$ time steps: $h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)$. Error delta at time $t$: $\delta_t = \frac{\partial L}{\partial h_t} = \frac{\partial L_t}{\partial h_t} + W_{hh}^T (\delta_{t+1} \odot (1 - h_{t+1}^2))$. Total weight gradient $dW_{hh} = \sum_{t=1}^T \delta_t h_{t-1}^T$.
### Question 3
3. BatchNorm $\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}, y_i = \gamma \hat{x}_i + \beta$. Gradients: $\frac{\partial L}{\partial \gamma} = \sum \frac{\partial L}{\partial y_i} \hat{x}_i$, $\frac{\partial L}{\partial \beta} = \sum \frac{\partial L}{\partial y_i}$. Input gradient: $\frac{\partial L}{\partial x_i} = \frac{\gamma}{B \sqrt{\sigma_B^2 + \epsilon}} \left( B \frac{\partial L}{\partial \hat{x}_i} - \sum_j \frac{\partial L}{\partial \hat{x}_j} - \hat{x}_i \sum_j \frac{\partial L}{\partial \hat{x}_j} \hat{x}_j \right)$.
### Question 4
4. Standard backprop caches all activations $a^{(l)}$ in VRAM ($O(L)$ memory). Gradient Checkpointing saves activations only every $k$ layers (e.g. $k=\sqrt{L}$), recomputing intermediate activations on-demand during backward pass via local forward pass ($O(\sqrt{L})$ memory).
### Question 5
5. Second-order backprop computes Hessian-vector products $H v = \nabla_{\mathbf{w}} (\nabla_{\mathbf{w}} L \cdot v)$. PyTorch evaluates this by calling `torch.autograd.grad(outputs=grad_w, inputs=w, grad_outputs=v)`, executing backward pass over the backward computational graph!
