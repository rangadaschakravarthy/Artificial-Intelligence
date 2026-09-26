# Practice Exercises — Backpropagation Mathematics

## Level 1 — Basic Understanding
1. Write down the 4 Fundamental Equations of Backpropagation.
2. What does $\mathbf{\delta}^{(l)}$ represent mathematically?
3. What operation is represented by the symbol $\odot$ in Backpropagation?
4. Why do we transpose the weight matrix $\mathbf{W}^{(l+1)T}$ when propagating deltas backward?
5. What is the output layer delta $\mathbf{\delta}^{(L)}$ for MSE loss with linear activation?

## Level 2 — Calculation
1. Given \mathbf{\delta}^{(2)} = [0.2, -0.4]^T, 

$$
\mathbf{W}^{(2)} = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
$$

, and \sigma'(\mathbf{z}^{(1)}) = [0.5, 0.5]^T, calculate hidden delta \mathbf{\delta}^{(1)}.
2. Given $\mathbf{\delta}^{(1)} = [-0.1, 0.3]^T$ and input vector $\mathbf{x} = [2, 5]^T$, compute weight gradient matrix $\frac{\partial L}{\partial \mathbf{W}^{(1)}}$.
3. If a network has 5 layers, list the order in which deltas $\mathbf{\delta}^{(l)}$ are computed.
4. Show that for a 1D network, $\delta^{(1)} = \delta^{(2)} w_2 \sigma'(z_1)$.
5. What is the computational complexity of backpropagation per sample for an $L$-layer MLP?

## Level 3 — Conceptual
1. Complete the mathematical proof of Equation 1 (Output Layer Delta) for MSE loss $L = \frac{1}{2} ||\mathbf{a}^{(L)} - \mathbf{y}||_2^2$ with Sigmoid activation.
2. Complete the mathematical proof of Equation 3 (Bias Gradient $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \mathbf{\delta}^{(l)}$).
3. Complete the mathematical proof of Equation 4 (Weight Gradient $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$).
4. Explain why backpropagation is an application of Reverse-Mode Automatic Differentiation.
5. How does mini-batch matrix backpropagation rewrite vector deltas as 2D matrix multiplications?

## Level 4 — AI/ML Application
1. Perform a complete hand calculation of forward pass, loss, backward pass deltas, and weight gradients for a 2-layer network with inputs x=[1, 1]^T, initial weights 

$$
W^{(1)}=\begin{bmatrix}0.1&0.2\\0.3&0.4\end{bmatrix}, b^{(1)}=[0, 0]^T, W^{(2)}=[0.5, 0.6], b^{(2)}=0
$$

, and target y=1.0. Verify every number.
2. Write a Python script that implements the hand calculation above and confirms exact matching numerical values.
3. Explain how PyTorch's `autograd` engine automatically constructs the backward execution graph without requiring manual gradient derivation.

## Level 5 — Interview Questions
1. Derive Backpropagation equations for Convolutional Neural Networks (CNNs), proving that error delta propagation through a convolutional layer is executed via convolution with flipped filter kernels $K_{rot180}$.
2. Derive Backpropagation Through Time (BPTT) for Recurrent Neural Networks (RNNs) with hidden state recurrence $h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)$.
3. Derive backpropagation gradient formulas for Batch Normalization layer $\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$, $y_i = \gamma \hat{x}_i + \beta$ with respect to $\gamma, \beta$, and input $x_i$.
4. Explain the Memory-Computation trade-off in Gradient Checkpointing (recomputing activations during backward pass vs caching them).
5. What is Second-Order Backpropagation (Hessian-Vector Products $\mathbf{H}\mathbf{v}$) and how is it derived using double backward passes (`torch.autograd.grad` of gradients)?
