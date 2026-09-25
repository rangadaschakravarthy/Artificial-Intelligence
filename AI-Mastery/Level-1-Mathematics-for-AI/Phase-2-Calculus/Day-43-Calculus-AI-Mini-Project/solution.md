# Solutions — Calculus AI Mini-Project

## Level 1 — Basic Understanding Solutions
### Question 1
1. To build a complete Multi-Layer Neural Network library from scratch in pure NumPy using Calculus and Backpropagation.
### Question 2
2. XOR is not linearly separable; no single straight line can separate $(0,0)$ and $(1,1)$ from $(0,1)$ and $(1,0)$.
### Question 3
3. Zero initialization causes all hidden neurons to compute identical forward activations and identical backward gradients, failing to learn distinct features (symmetry problem).
### Question 4
4. $\text{ReLU}'(x) = 1$ if $x > 0$, and $0$ if $x < 0$.
### Question 5
5. Binary Cross-Entropy (BCE) Loss.

## Level 2 — Calculation Solutions
### Question 1
1. $\sigma = \sqrt{\frac{2}{784}} = \sqrt{0.002551} \approx 0.0505$.
### Question 2
2. Matrix shape is $64 \times 128$ (Batch size $B=64$, Hidden neurons $H=128$).
### Question 3
3. $\nabla_{\mathbf{W}_1} = \frac{1}{B} \mathbf{\Delta}_1^T \mathbf{X}$.
### Question 4
4. Reduce the Learning Rate $\eta$ (e.g. from $0.5 \to 0.05$).
### Question 5
5. Thresholding probability $p = 0.5$ converts continuous sigmoid confidence scores into discrete binary predictions.

## Level 3 — Conceptual Solutions
### Question 1
1. $\nabla_{\mathbf{b}_1} = \frac{1}{B} \sum_{i=1}^B \mathbf{\Delta}_{1, i} = \frac{1}{B} \mathbf{1}_{1 \times B} \mathbf{\Delta}_1$ (summing error deltas across rows of batch).
### Question 2
2. For $z = \sum_{i=1}^{n_{in}} w_i x_i$, $\text{Var}(z) = n_{in} \text{Var}(w) \text{Var}(x)$. For ReLU, half activations are zeroed out (dividing variance by 2). Setting $\text{Var}(w) = \frac{2}{n_{in}}$ cancels out factors: $n_{in} (\frac{2}{n_{in}}) (\frac{1}{2} \text{Var}(x)) = \text{Var}(x)$, maintaining constant variance!
### Question 3
3. Forward: $A_1 = X W_1^T + b_1$. Output: $Z_2 = (X W_1^T + b_1) W_2^T + b_2 = X (W_1^T W_2^T) + (b_1 W_2^T + b_2) = X W_{combined}^T + b_{combined}$. Pure linear model!
### Question 4
4. XOR loss surface has flat regions. Momentum maintains velocity along previous descent directions, pushing weights rapidly through flat zero-gradient zones.
### Question 5
5. Perturb each weight $w_{i,j} \pm \epsilon$, compute numerical gradient $g_{num} = \frac{L(w+\epsilon) - L(w-\epsilon)}{2\epsilon}$, and check relative norm difference with backprop gradient $g_{backprop}$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Add Layer 2 (`W2, b2`) with ReLU, update output layer to Layer 3 (`W3, b3`) with Sigmoid. Compute $\Delta_3 = A_3 - Y$, $\Delta_2 = (\Delta_3 W_3) * \text{ReLU}'(Z_2)$, $\Delta_1 = (\Delta_2 W_2) * \text{ReLU}'(Z_1)$. Network easily fits Concentric Circles dataset.
### Question 2
2. Loss becomes $L_{total} = L_{BCE} + \frac{\lambda}{2B} (||W_1||_F^2 + ||W_2||_F^2)$. Weight gradients add decay term: $\nabla_{W_1} = \frac{1}{B} \Delta_1^T X + \frac{\lambda}{B} W_1$.
### Question 3
3. Set $\eta_t = \eta_{min} + 0.5(\eta_{max} - \eta_{min})(1 + \cos(t / T \cdot \pi))$ inside epoch loop.

## Level 5 — Interview Questions Solutions
### Question 1
1. Output layer: $Z_2 = A_1 W_2^T + b_2$, $A_2 = \text{Softmax}(Z_2)$. CCE Loss $L = -\frac{1}{B} \sum \sum Y_{i,c} \ln A_{2, i,c}$. Output Delta $\Delta_2 = A_2 - Y$. Weight gradient $\nabla_{W_2} = \frac{1}{B} \Delta_2^T A_1$. Train on MNIST 10-class digits.
### Question 2
2. Define `Tensor` object with `.data`, `.grad`, and `_backward()` closures for `matmul`, `add`, `relu`, `sigmoid`. Calling `loss.backward()` automatically computes all layer gradients.
### Question 3
3. BatchNorm Layer: Forward computes batch mean $\mu_B$ and variance $\sigma_B^2$, normalizes $\hat{X} = \frac{X - \mu_B}{\sqrt{\sigma_B^2+\epsilon}}$, scales $Y = \gamma \hat{X} + \beta$. Backward computes $\nabla_\gamma = \sum \Delta_Y \odot \hat{X}$, $\nabla_\beta = \sum \Delta_Y$, and propagates input delta $\Delta_X$.
### Question 4
4. Adam Optimizer maintains 1st moment $m_W = \beta_1 m_W + (1-\beta_1) g_W$ and 2nd moment $v_W = \beta_2 v_W + (1-\beta_2) g_W^2$. Corrects bias $\hat{m} = m / (1-\beta_1^t), \hat{v} = v / (1-\beta_2^t)$, updates $W -= \frac{\eta}{\sqrt{\hat{v}} + \epsilon} \hat{m}$.
### Question 5
5. DARTS (Differentiable Architecture Search) relaxes discrete architecture choices into continuous Softmax weights over candidate operations (Conv, Linear, Skip), optimizing architecture parameters via bi-level gradient descent.
