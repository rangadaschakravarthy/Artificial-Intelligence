# Practice Exercises — Calculus AI Mini-Project

## Level 1 — Basic Understanding
1. What is the main goal of the Phase 2 Mini-Project?
2. Why is a 1-layer linear model unable to solve the XOR problem?
3. Why must neural network weights be initialized with small random values instead of all zeros?
4. What is the derivative of ReLU for positive vs negative inputs?
5. What loss function is used for binary classification in the mini-project?

## Level 2 — Calculation
1. Calculate He Normal weight standard deviation for a layer with $n_{in} = 784$ input features.
2. Write the matrix shape for hidden error delta $\mathbf{\Delta}_1$ when batch size $B=64$ and hidden size $H=128$.
3. Write the matrix formula for hidden layer weight gradient $\nabla_{\mathbf{W}_1}$.
4. If training loss is oscillating wildly during mini-project execution, what hyperparameter should be reduced?
5. Explain how predicting probabilities $p > 0.5 \implies 1, p \le 0.5 \implies 0$ evaluates classification accuracy.

## Level 3 — Conceptual
1. Derive the exact mathematical matrix equation for bias gradients $\nabla_{\mathbf{b}_1}$ and $\nabla_{\mathbf{b}_2}$ when using mini-batches of size $B$.
2. Explain how He Normal Initialization $\text{Var}(W) = \frac{2}{n_{in}}$ preserves activation variance across ReLU layers.
3. Show that if ReLU is replaced with identity function $f(x) = x$, the 2-layer network collapses to a 1-layer linear model.
4. Why does adding a Momentum term $v_{t+1} = \beta v_t + \eta \nabla L$ speed up XOR training convergence?
5. Explain Gradient Checking logic used to verify mini-project backpropagation implementations.

## Level 4 — AI/ML Application
1. Modify the mini-project code to add a 3rd hidden layer (`Dense(8) -> ReLU -> Dense(4) -> ReLU -> Dense(1) -> Sigmoid`). Train on Concentric Circles dataset.
2. Add L2 Weight Decay Regularization penalty $\frac{\lambda}{2} ||W||_F^2$ to the mini-project loss and backprop gradients.
3. Add Learning Rate Cosine Annealing scheduler to the mini-project training loop.

## Level 5 — Interview Questions
1. Extend the mini-project framework to support Softmax activation and Categorical Cross-Entropy loss for Multi-Class classification (MNIST digit recognition).
2. Implement Automatic Differentiation (Micrograd-style autograd engine) inside the mini-project framework instead of manual backprop deltas.
3. Explain how Batch Normalization layers can be implemented from scratch inside the mini-project framework including forward and backward passes.
4. Implement Adam Optimizer (`m_t, v_t` bias-corrected moments) inside the mini-project framework.
5. Explain how Neural Architecture Search (NAS) automates finding optimal layer sizes $H$ using reinforcement learning or gradient-based DARTS.
