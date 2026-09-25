# Practice Exercises — Calculus for Neural Networks

## Level 1 — Basic Understanding
1. Write the forward pass equation for neural network layer $l$.
2. What is the layer error delta vector $\mathbf{\delta}^{(l)}$ defined as?
3. State the backward error recurrence formula for hidden layer $\mathbf{\delta}^{(l)}$.
4. State the weight gradient formula $\frac{\partial L}{\partial \mathbf{W}^{(l)}}$.
5. What is the derivative of ReLU activation function?

## Level 2 — Calculation
1. Given output activation $a^{(2)} = 0.9$ and target $y = 1.0$, compute output layer delta $\delta^{(2)}$ for BCE loss.
2. Given $\delta^{(2)} = -0.1$ and previous layer activation $\mathbf{a}^{(1)} = [0.4, 0.8]^T$, compute weight gradient $\frac{\partial L}{\partial \mathbf{W}^{(2)}}$.
3. Given $\mathbf{W}^{(2)} = [1.5, -2.0]$, $\delta^{(2)} = -0.1$, and $\sigma'(\mathbf{z}^{(1)}) = [0.2, 0.2]^T$, compute hidden delta $\mathbf{\delta}^{(1)}$.
4. If pre-activation $\mathbf{z} = [-2.0, 3.0, 0.0]^T$, evaluate ReLU derivative vector $\text{ReLU}'(\mathbf{z})$.
5. Why do we store pre-activations $\mathbf{z}^{(l)}$ during the forward pass?

## Level 3 — Conceptual
1. Derive output layer error delta $\mathbf{\delta}^{(L)} = \mathbf{a}^{(L)} - \mathbf{y}$ for Softmax activation paired with Categorical Cross-Entropy loss.
2. Prove that $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$ using matrix chain rule.
3. Explain why LeakyReLU $f(x) = \max(0.01x, x)$ prevents Dying ReLU neurons during backward pass.
4. Analyze derivative of Tanh activation $f(x) = \text{tanh}(x) \implies f'(x) = 1 - \text{tanh}^2(x)$ and compare with Sigmoid.
5. How does mini-batch matrix notation rewrite backpropagation deltas as 2D matrix multiplications?

## Level 4 — AI/ML Application
1. Implement a 2-layer Neural Network class from scratch in Python with manual forward and backward pass functions. Verify training loss decreases on XOR problem.
2. Explain Gradient Vanishing in deep neural networks when using Sigmoid vs ReLU activations using the backward recurrence formula $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$.
3. Explain Gradient Exploding and why weight initialization methods (He Initialization, Xavier/Glorot Initialization) set weight variance to $\frac{2}{n_{in}}$ or $\frac{2}{n_{in} + n_{out}}$.

## Level 5 — Interview Questions
1. Derive full matrix backpropagation equations for a mini-batch dataset matrix $\mathbf{X}_{B \times d}$: $\mathbf{Z}^{(1)} = \mathbf{X} \mathbf{W}^{(1)T} + \mathbf{b}^{(1)}$, $\mathbf{\Delta}^{(2)} = \mathbf{A}^{(2)} - \mathbf{Y}$, $\mathbf{\Delta}^{(1)} = (\mathbf{\Delta}^{(2)} \mathbf{W}^{(2)}) \odot \sigma'(\mathbf{Z}^{(1)})$, $\nabla_{\mathbf{W}^{(1)}} = \mathbf{\Delta}^{(1)T} \mathbf{X}$.
2. Explain how Recurrent Neural Networks (RNNs) extend backpropagation deltas across temporal sequence steps (Backpropagation Through Time BPTT).
3. Derive gradient of Batch Normalization layer $\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$ with respect to input activations $x_i$.
4. Explain Convolutional Layer backpropagation: how weight gradient $\nabla_{\mathbf{K}}$ is computed via cross-correlation of input maps and error delta maps.
5. What is Gradient Checkpointing and how does it optimize memory by recalculating forward activations during backward delta propagation?
