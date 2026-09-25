# Theory — Learning Rate

### 1. Simple Definition
The learning rate is a hyperparameter that controls how big of a step the optimizer takes downhill during each gradient descent parameter update.

### 2. Intuition
Think of taking steps down a staircase. Taking tiny baby steps (small $\eta$) takes hours to reach the bottom. Taking giant leap steps (large $\eta$) makes you overshoot the staircase and crash into the wall!

### 3. Mathematical Definition
For update $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta_t \nabla L(\mathbf{w}_t)$, maximum stable learning rate is bounded by top Hessian eigenvalue: $\eta_{max} < \frac{2}{\lambda_{max}(\mathbf{H})}$.

### 4. Notation
$\eta, \alpha, \text{lr}$. Cosine Annealing $\eta_t = \eta_{min} + \frac{1}{2}(\eta_{max} - \eta_{min})\left(1 + \cos\left(\frac{t}{T}\pi\right)\right)$.

### 5. Formula
$$\text{Exponential Decay: } \eta_t = \eta_0 \cdot \gamma^t, \quad \text{Step Decay: } \eta_t = \eta_0 \cdot \gamma^{\lfloor t / s \rfloor}$$

### 6. Symbol-by-Symbol Explanation
- \eta_0: Initial learning rate
- \gamma: Decay rate factor (e.g. 0.95)
- t: Current epoch/iteration
- s: Step size decay frequency

### 7. Step-by-Step Calculation
Optimize $L(w) = 5w^2$ (Hessian $H = 10 \implies \lambda_{max} = 10$).
- Max stable learning rate $\eta_{max} = 2 / 10 = 0.2$.
- Case 1 (Too Large $\eta = 0.25 > 0.2$): $w_0 = 1 \implies w_1 = 1 - 0.25(10) = -1.5 \implies w_2 = -1.5 - 0.25(-15) = +2.25 \implies$ DIVERGES TO $\infty$!
- Case 2 (Optimal $\eta = 0.1$): $w_0 = 1 \implies w_1 = 1 - 0.1(10) = 0 \implies$ Reaches minimum in 1 step!

### 8. Second Example
Calculate Step Decay after 100 epochs with $\eta_0 = 0.1, \gamma = 0.5, s = 50$:
$\eta_{100} = 0.1 \cdot (0.5)^{\lfloor 100 / 50 \rfloor} = 0.1 \cdot (0.5)^2 = 0.1 \cdot 0.25 = 0.025$.

### 9. Common Mistakes
Keeping learning rate fixed at a high value for the entire training run (prevents settling into fine-grained loss minima).

### 10. AI Connection
Transformers (BERT, GPT, LLaMA) require Learning Rate Warmup (increasing $\eta$ linearly for first 2000 steps) to prevent catastrophic gradient divergence during early training when Adam moment estimates are uncalibrated.

### 11. Algorithm Connection
SGD, AdamW, Cosine Annealing, ReduceLROnPlateau, Linear Warmup.

### 12. Practical Interpretation
A loss curve bouncing violently up and down or returning `NaN` indicates learning rate is TOO LARGE. A loss curve flatlining without progress indicates learning rate is TOO SMALL.

### 13. Interview Insight
Q: 'Why is Learning Rate Warmup critical when training Large Language Models with AdamW?' A: At the start of training, Adam's 2nd moment variance estimate $v_t$ is initialized to zero, causing adaptive step sizes to be uncontrollably large. Warmup scales $\eta$ gradually while $v_t$ calibrates.

### 14. Summary
Learning rate $\eta$ controls step size. Too large $\implies$ divergence ($
\infty$ / `NaN`); too small $\implies$ slow convergence. Learning rate schedules (Cosine Annealing, Warmup) adapt $\eta$ during training.
