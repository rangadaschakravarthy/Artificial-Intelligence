# Solutions — Learning Rate

## Level 1 — Basic Understanding Solutions
### Question 1
1. A scalar hyperparameter controlling the step size taken downhill along the gradient vector per update.
### Question 2
2. Training is extremely slow; optimizer can get trapped in high-loss local minima or flat plateaus.
### Question 3
3. Optimizer overshoots the minimum, oscillates wildly, and loss diverges to $\infty$ or returns `NaN`.
### Question 4
4. A rule that dynamically alters the learning rate $\eta_t$ during the course of training.
### Question 5
5. Gradually increases learning rate from near-zero to target $\eta_{max}$ during early training steps to stabilize initial gradient updates.

## Level 2 — Calculation Solutions
### Question 1
1. Second derivative $f''(w) = 8 \implies \eta_{max} = 2 / 8 = 0.25$.
### Question 2
2. $w_0 = 1.0$. Step 1: $w_1 = 1 - 0.3(8) = 1 - 2.4 = -1.4$. Step 2: $w_2 = -1.4 - 0.3(-11.2) = -1.4 + 3.36 = +1.96$. Step 3: $w_3 = 1.96 - 0.3(15.68) = 1.96 - 4.704 = -2.744$. Absolute value grows $|1.0| \to |1.4| \to |1.96| \to |2.744| \implies$ DIVERGES!
### Question 3
3. $\eta_{30} = 0.1 \times (0.95)^{30} \approx 0.1 \times 0.2146 = 0.02146$.
### Question 4
4. At $t = T/2$, $\cos(\pi/2) = 0 \implies \eta = 0 + \frac{1}{2}(0.1 - 0)(1 + 0) = 0.05$.
### Question 5
5. `torch.optim.lr_scheduler.ReduceLROnPlateau`.

## Level 3 — Conceptual Solutions
### Question 1
1. Quadratic error evolution: $e_{t+1} = (\mathbf{I} - \eta \mathbf{H}) e_t$. For error to shrink $||e_{t+1}|| < ||e_t||$, matrix spectral radius $|1 - \eta \lambda_i| < 1 \implies 0 < \eta \lambda_{max} < 2 \implies \eta < \frac{2}{\lambda_{max}}$.
### Question 2
2. LR Finder plots Loss vs $\eta$ over 1 epoch. Identifies $\eta_{min}$ where loss starts dropping rapidly and $\eta_{max}$ where loss starts exploding, selecting optimal $\eta$ in the steep decline zone.
### Question 3
3. Step Decay drops $\eta$ by constant factor at fixed epoch thresholds. Exponential Decay decays $\eta$ continuously each step. Cosine Annealing with Warm Restarts periodically resets $\eta$ back to $\eta_{max}$ to escape local minima.
### Question 4
4. Adam divides gradients by root second moment $\sqrt{v_t}$. Effective step sizes are unscaled by gradient magnitude, making large $\eta$ values cause massive instability.
### Question 5
5. Increasing batch size $B$ by $K$ reduces gradient variance by $K$. To maintain equivalent progress per epoch, step size $\eta$ must scale linearly $\eta \to K \eta$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Warmup linearly increases $\eta$ from $0 \to \eta_{max}$ for $T_{warm}$ epochs, then Cosine Annealing smoothly decays $\eta \to \eta_{min}$: $\eta_t = \eta_{min} + 0.5(\eta_{max}-\eta_{min})(1 + \cos(\frac{t - T_{warm}}{T - T_{warm}} \pi))$.
### Question 2
2. Small $\eta=0.01$ takes 500 steps. Optimal $\eta=0.1$ reaches minimum in 20 steps. Overshooting $\eta=0.3$ bounces back and forth across valley. Divergent $\eta=0.55$ explodes to infinity.
### Question 3
3. Early in ViT training, self-attention maps are uniform random noise, generating huge initial gradients. Large $\eta$ destroys randomly initialized projection weights. Warmup holds $\eta$ small until attention maps form basic spatial structures.

## Level 5 — Interview Questions Solutions
### Question 1
1. In 1 epoch of SGD with batch size $B$, we take $N/B$ steps with covariance $\text{Cov}(\nabla L_B) = \frac{\sigma^2}{B}$. Total weight drift covariance over 1 epoch is $\frac{N}{B} \eta^2 \frac{\sigma^2}{B} = N \sigma^2 \left(\frac{\eta}{B}\right)^2$. For weight drift variance to remain invariant when $B \to K B$, we must set $\eta \to K \eta$.
### Question 2
2. LARS (Layer-wise Adaptive Rate Scaling) computes separate learning rate for each layer $l$: $\eta_l = \gamma \frac{||\mathbf{w}_l||_2}{||\nabla L(\mathbf{w}_l)||_2 + \beta ||\mathbf{w}_l||_2}$, preventing layer weight explosion when training with $B = 32,768$.
### Question 3
3. Minimize $g(\eta) = f(\mathbf{x} - \eta \mathbf{g}) \approx f(\mathbf{x}) - \eta \mathbf{g}^T \mathbf{g} + \frac{1}{2} \eta^2 \mathbf{g}^T \mathbf{H} \mathbf{g}$. Differentiating w.r.t $\eta$: $-\mathbf{g}^T \mathbf{g} + \eta \mathbf{g}^T \mathbf{H} \mathbf{g} = 0 \implies \eta^* = \frac{||\mathbf{g}||_2^2}{\mathbf{g}^T \mathbf{H} \mathbf{g}}$.
### Question 4
4. SWA runs SGD with high cyclic learning rate. Every $K$ epochs, weights enter wide flat minima. SWA averages these checkpoint weights $\mathbf{w}_{SWA} = \frac{1}{M} \sum_{m=1}^M \mathbf{w}_{m}$, placing model directly in the geometric center of flat low-loss regions.
### Question 5
5. Hypergradient descent updates learning rate $\eta$ via gradient descent on $\eta$ itself: $\eta_{t+1} = \eta_t - \beta \frac{\partial L_{t+1}}{\partial \eta_t} = \eta_t + \beta (\nabla L_t \cdot \nabla L_{t-1})$, accelerating $\eta$ when consecutive gradients align and slowing down when gradients reverse.
