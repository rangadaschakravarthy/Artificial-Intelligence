# Solutions — Loss Functions

## Level 1 — Basic Understanding Solutions
### Question 1
1. Loss function computes error for 1 data sample $L(y_i, \hat{y}_i)$. Cost function averages loss across entire dataset batch $J(\mathbf{w}) = \frac{1}{N} \sum L_i$.
### Question 2
2. $\text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$.
### Question 3
3. $\text{BCE} = -\frac{1}{N} \sum_{i=1}^N [y_i \ln(\hat{y}_i) + (1-y_i) \ln(1-\hat{y}_i)]$.
### Question 4
4. Errors are squared $(y - \hat{y})^2$, so large outlier errors produce exponentially larger loss penalties.
### Question 5
5. Categorical Cross-Entropy (CCE).

## Level 2 — Calculation Solutions
### Question 1
1. Errors: $(3-2)=1, (5-6)=-1, (8-7)=1$. Squared errors: $1, 1, 1$. MSE $= (1+1+1)/3 = 1.0$.
### Question 2
2. Absolute errors: $1, 1, 1$. MAE $= (1+1+1)/3 = 1.0$.
### Question 3
3. $y=0, \hat{y}=0.2 \implies L = -[0 + 1 \cdot \ln(1 - 0.2)] = -\ln(0.8) \approx 0.2231$.
### Question 4
4. $\frac{\partial L}{\partial \hat{y}} = \frac{d}{d\hat{y}}[(y - \hat{y})^2] = 2(y - \hat{y})(-1) = -2(y - \hat{y})$.
### Question 5
5. $|d| = 4.0 > \delta = 1.0 \implies \text{Huber} = 1.0(4.0 - 0.5(1.0)) = 3.5$.

## Level 3 — Conceptual Solutions
### Question 1
1. Bernoulli likelihood $P(y|p) = p^y (1-p)^{1-y}$. Negative log likelihood $-\ln P(y|p) = -\ln(p^y (1-p)^{1-y}) = -[y \ln(p) + (1-y)\ln(1-p)]$. This is exact BCE loss!
### Question 2
2. Gaussian likelihood $P(y|x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(y - \hat{y})^2}{2\sigma^2}\right)$. Negative log likelihood $-\ln P = \frac{(y - \hat{y})^2}{2\sigma^2} + \text{const}$. Minimizing NLL is equivalent to minimizing MSE $(y - \hat{y})^2$.
### Question 3
3. Chain rule: $\frac{\partial L}{\partial z} = \frac{\partial L}{\partial \hat{y}} \frac{\partial \hat{y}}{\partial z} = \left(\frac{\hat{y} - y}{\hat{y}(1-\hat{y})}\right) \left(\hat{y}(1-\hat{y})\right) = \hat{y} - y$. Outstanding algebraic simplification!
### Question 4
4. L2 loss gradient $2(y - \hat{y})$ shrinks linearly to 0 as error approaches 0 (smooth convergence). L1 loss gradient $\text{sign}(y - \hat{y}) = \pm 1$ maintains constant magnitude, causing oscillation around 0 unless learning rate decays.
### Question 5
5. Focal Loss $L_{FL} = -(1 - p_t)^\gamma \ln(p_t)$ adds modulating factor $(1 - p_t)^\gamma$ ($\gamma \approx 2$). Down-weights loss for easy well-classified examples ($p_t \to 1$), focusing gradient capacity on hard misclassified samples.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Implement Huber piecewise logic: `np.where(np.abs(d) <= delta, 0.5 * d**2, delta * (np.abs(d) - 0.5 * delta))`. Plot shows quadratic bowl near 0 and linear sides for $|d| > 1$.
### Question 2
2. Multi-Label Classification requires Independent Binary Cross-Entropy (BCE) applied to each output node independently with Sigmoid activation (since classes are not mutually exclusive).
### Question 3
3. Triplet loss pulls anchor vector $a$ closer to positive vector $p$ while pushing negative vector $n$ away by at least margin $m$: $L = \max(0, ||a - p||_2^2 - ||a - n||_2^2 + m)$.

## Level 5 — Interview Questions Solutions
### Question 1
1. $\frac{\partial L}{\partial z_j} = \sum_i \frac{\partial L}{\partial S_i} \frac{\partial S_i}{\partial z_j} = \sum_i \left(-\frac{y_i}{S_i}\right) S_i (\delta_{i,j} - S_j) = -y_j + S_j \sum y_i = S_j - y_j$. Matrix form: $\nabla_{\mathbf{z}} L = \mathbf{S} - \mathbf{y}$.
### Question 2
2. $H(P, Q) = -\sum P(x) \ln Q(x) = -\sum P(x) \ln P(x) + \sum P(x) \ln\left(\frac{P(x)}{Q(x)}\right) = H(P) + D_{KL}(P \parallel Q)$. Since true distribution entropy $H(P)$ is constant, minimizing Cross-Entropy $H(P, Q)$ directly minimizes KL Divergence $D_{KL}(P \parallel Q)$.
### Question 3
3. Kantorovich-Rubinstein duality defines Wasserstein distance $W(P_r, P_g) = \sup_{||f||_L \le 1} E_{x \sim P_r}[f(x)] - E_{y \sim P_g}[f(y)]$. Unlike Jensen-Shannon divergence which saturates to $\ln 2$ when distributions do not overlap, Wasserstein distance provides continuous linear gradients everywhere.
### Question 4
4. Softmax with hard one-hot targets $[0, 1, 0]$ forces logits $z_1 \to \infty$, causing overconfidence and poor generalization. Label smoothing replaces targets with $y_{smooth} = 0.9$ and $0.05$, bounding logit magnitudes and regularizing weights.
### Question 5
5. ArcFace adds angular margin penalty $m$ directly to target class angle: $L = -\ln \frac{e^{s \cos(\theta_{y_i} + m)}}{e^{s \cos(\theta_{y_i} + m)} + \sum_{j \neq y_i} e^{s \cos(\theta_j)}}$, forcing inter-class cosine feature embeddings to be distinct and hyper-separable on unit hypersphere.
