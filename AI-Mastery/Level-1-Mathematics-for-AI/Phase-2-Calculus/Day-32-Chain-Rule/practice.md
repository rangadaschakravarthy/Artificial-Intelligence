# Practice Exercises — Chain Rule

## Level 1 — Basic Understanding
1. State the single-variable Chain Rule formula $\frac{dy}{dx}$.
2. Differentiate $y = (x^2 + 3)^5$.
3. Differentiate $y = e^{4x}$.
4. Differentiate $y = \ln(5x)$.
5. Why does Backpropagation rely on the Chain Rule?

## Level 2 — Calculation
1. Compute derivative of $y = \sin(x^3)$.
2. Compute derivative of $y = (3x^2 - 2x + 1)^4$.
3. Given $z = u^2 + v^2$ with $u = 2t$ and $v = 3t$, compute $\frac{dz}{dt}$ using multi-variable Chain Rule.
4. Compute derivative of Sigmoid composition $f(x) = \sigma(2x + 3)$ at $x = 0$.
5. Compute derivative of $y = e^{-x^2/2}$.

## Level 3 — Conceptual
1. Derive multi-variable Chain Rule for $z = f(u, v)$ where $u = u(x, y)$ and $v = v(x, y)$ to find $\frac{\partial z}{\partial x}$.
2. Draw a computational graph for $L = (w x + b - y)^2$ and write chain rule factors for $\frac{\partial L}{\partial w}$ and $\frac{\partial L}{\partial b}$.
3. Compute derivative of composite loss function $L = -\ln(\sigma(z))$ with respect to $z$.
4. Explain why vanishing gradients occur in 50-layer networks when applying chain rule to Sigmoid activations.
5. Compare Forward-Mode Automatic Differentiation vs Reverse-Mode Automatic Differentiation.

## Level 4 — AI/ML Application
1. Given 2-layer network $z_1 = w_1 x + b_1$, $h_1 = \sigma(z_1)$, $z_2 = w_2 h_1 + b_2$, $\hat{y} = \sigma(z_2)$, and MSE loss $L = \frac{1}{2}(\hat{y} - y)^2$, write explicit Chain Rule expressions for $\frac{\partial L}{\partial w_2}$ and $\frac{\partial L}{\partial w_1}$.
2. Evaluate numerical value of $\frac{\partial L}{\partial w_1}$ for $x=1, y=1, w_1=0.5, b_1=0, w_2=1.0, b_2=0$.
3. Explain how PyTorch Autograd builds the `grad_fn` chain during the forward pass to execute reverse-mode AD.

## Level 5 — Interview Questions
1. Derive matrix chain rule for matrix weight gradient $\frac{\partial L}{\partial \mathbf{W}_1} = \mathbf{X}^T \left( (\frac{\partial L}{\partial \mathbf{H}_2} \mathbf{W}_2^T) \odot \sigma'(\mathbf{Z}_1) \right)$.
2. What is Jacobian-Vector Product (JVP) in Forward AD vs Vector-Jacobian Product (VJP) in Reverse AD?
3. Explain how Recurrent Neural Networks (RNNs) apply Backpropagation Through Time (BPTT) using unrolled chain rules across time steps.
4. Prove that Forward-Mode AD computes exact column $j$ of Jacobian matrix $J$, while Reverse-Mode AD computes exact row $i$ of $J$.
5. Explain Gradient Checkpointing (trade-off between memory and computation by recomputing forward activations during backward chain rule pass).
