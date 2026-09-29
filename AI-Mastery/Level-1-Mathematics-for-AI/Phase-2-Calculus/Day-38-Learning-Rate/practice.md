# Practice Exercises — Learning Rate

## Level 1 — Basic Understanding
1. What is the learning rate in gradient descent?
2. What happens if the learning rate is too small?
3. What happens if the learning rate is too large?
4. What is a Learning Rate Schedule?
5. What does Learning Rate Warmup do?

## Level 2 — Calculation
1. For $L(w) = 4w^2$, determine the maximum stable learning rate $\eta_{max} = 2 / f''(w)$.
2. Simulate 3 steps of $w_{t+1} = w_t - \eta (8w_t)$ for $w_0 = 1.0$ and unstable $\eta = 0.3$. Does it diverge?
3. Calculate learning rate at epoch 30 for Exponential Decay $\eta_t = 0.1 \times (0.95)^t$.
4. Calculate learning rate for Cosine Annealing at halfway point $t = T/2$ given $\eta_{max} = 0.1, \eta_{min} = 0.0$.
5. What PyTorch scheduler automatically drops learning rate when validation loss stops improving?

## Level 3 — Conceptual
1. Mathematical derivation of maximum stable learning rate $\eta < \frac{2}{\lambda_{max}(\mathbf{H})}$ using Taylor expansion.
2. Explain why Learning Rate Finder (Fast.ai technique) sweeps $\eta$ exponentially from $10^{-6}$ to $10^1$ to find optimal $\eta$.
3. Explain the difference between Step Decay, Exponential Decay, and Cosine Annealing with Warm Restarts (SGDR).
4. Why does AdamW require smaller learning rates ($10^{-4}$) compared to SGD ($10^{-1}$)?
5. How does batch size $B$ scale with learning rate $\eta$ under Linear Learning Rate Scaling Rule ($\to$ double $B \implies$ double $\eta$)?

## Level 4 — AI/ML Application
1. Write a Python function implementing Cosine Annealing with Warmup learning rate scheduler. Plot $\eta_t$ over 100 epochs.
2. Demonstrate learning rate sensitivity on 2D quadratic bowl function in Python, plotting trajectories for small, optimal, and overshooting $\eta$.
3. Explain how Warmup prevents Early Layer Collapse in Vision Transformers (ViT).

## Level 5 — Interview Questions
1. Prove that under Linear Scaling Rule, multiplying batch size by $K$ ($B \to K B$) requires scaling learning rate $\eta \to K \eta$ to preserve total gradient variance per epoch.
2. Explain AdaFactor and LARS (Layer-wise Adaptive Rate Scaling) for training ultra-large models with batch sizes $B > 32,000$.
3. Derive exact optimal step size $\eta^* = \frac{||g_t||_2^2}{g_t^2 \mathbf{H} g_t}$ for quadratic functions using Line Search.
4. Explain Stochastic Weight Averaging (SWA) combined with cyclical learning rates for finding flat minima.
5. What is Hypergradient Descent (learning rate on the learning rate $\eta_{t+1} = \eta_t - \beta \nabla_\eta L$)?
