# Solutions — Linear Algebra for Machine Learning

## Level 1 — Basic Understanding Solutions
### Question 1
1. Dot product $\mathbf{w}^T \mathbf{x}$ (or matrix multiplication $\mathbf{X}\mathbf{w}$).
### Question 2
2. $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$.
### Question 3
3. $\mathbf{w}^T \mathbf{x} + b = 0$.
### Question 4
4. Matrix multiplication $\mathbf{Z} = \mathbf{X}\mathbf{W} + \mathbf{b}$.
### Question 5
5. Eigendecomposition of covariance matrix (or SVD of mean-centered data).

## Level 2 — Calculation Solutions
### Question 1
1. $y = 0.4(2) + (-0.2)(5) + 1.0 = 0.8 - 1.0 + 1.0 = 0.8$.
### Question 2
2. $\mathbf{w} = [3, 4]^T \implies ||\mathbf{w}||_2 = \sqrt{9+16} = 5$. Numerator $= |3(3)+4(4)-5| = |9+16-5| = 20$. Distance $= 20 / 5 = 4.0$.
### Question 3
3. $\mathbf{X}$ is $500 \times 20$. $\mathbf{X}^T \mathbf{X}$ is $20 \times 20$. $\mathbf{w}^*$ is $20 \times 1$.
### Question 4
4. $\mathbf{H}_1 = \sigma_1(\mathbf{X}\mathbf{W}_1 + \mathbf{b}_1)$, $\mathbf{H}_2 = \sigma_2(\mathbf{H}_1\mathbf{W}_2 + \mathbf{b}_2)$, $\mathbf{Y} = \sigma_3(\mathbf{H}_2\mathbf{W}_3 + \mathbf{b}_3)$.
### Question 5
5. Ridge loss adds penalty term $\frac{\lambda}{2} ||\mathbf{w}||_2^2 = \frac{\lambda}{2} \mathbf{w}^T \mathbf{w}$, penalizing large L2 weight vector magnitudes.

## Level 3 — Conceptual Solutions
### Question 1
1. MSE Loss $J(\mathbf{w}) = (\mathbf{X}\mathbf{w} - \mathbf{y})^T (\mathbf{X}\mathbf{w} - \mathbf{y}) = \mathbf{w}^T \mathbf{X}^T \mathbf{X} \mathbf{w} - 2 \mathbf{w}^T \mathbf{X}^T \mathbf{y} + \mathbf{y}^T \mathbf{y}$. Gradient $\nabla_{\mathbf{w}} J = 2 \mathbf{X}^T \mathbf{X} \mathbf{w} - 2 \mathbf{X}^T \mathbf{y} = \mathbf{0} \implies \mathbf{X}^T \mathbf{X} \mathbf{w} = \mathbf{X}^T \mathbf{y} \implies \mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$.
### Question 2
2. Margin between parallel hyperplanes $\mathbf{w}^T \mathbf{x} + b = 1$ and $\mathbf{w}^T \mathbf{x} + b = -1$ is $\frac{2}{||\mathbf{w}||_2}$. Maximizing margin is equivalent to minimizing $||\mathbf{w}||_2^2 / 2$.
### Question 3
3. If $f(x) = x$, layer 1 is $X W_1$, layer 2 is $(X W_1) W_2 = X (W_1 W_2) = X W_{combined}$. $N$ linear layers collapse into a single equivalent 1-layer linear model.
### Question 4
4. A 2D convolution kernel $K_{k \times k}$ slides across input image patch $P_{k \times k}$, computing element-wise product sum $\sum K_{i,j} P_{i,j}$, which is a dot product of flattened vectors.
### Question 5
5. Softmax computes $P(y=i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$, exponentiating each component of logit vector $\mathbf{z}$ and dividing by L1 sum to normalize to a valid probability distribution.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Input $\mathbf{X}_{32 \times 784} \rightarrow \mathbf{Z}_1 = \mathbf{X} \mathbf{W}_{1(784 \times 128)} + \mathbf{b}_{1(1 \times 128)} \rightarrow \mathbf{H}_{1(32 \times 128)} = \text{ReLU}(\mathbf{Z}_1) \rightarrow \mathbf{Z}_2 = \mathbf{H}_1 \mathbf{W}_{2(128 \times 10)} + \mathbf{b}_{2(1 \times 10)} \rightarrow \mathbf{P}_{32 \times 10} = \text{Softmax}(\mathbf{Z}_2)$.
### Question 2
2. Singularity occurs when feature columns are collinear ($|\mathbf{X}^T \mathbf{X}| = 0$). Ridge adds $\lambda \mathbf{I}_d$, ensuring $\det(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I}) > 0$, guaranteeing invertibility.
### Question 3
3. Query $Q_{B \times S \times D}$, Key $K_{B \times S \times D}$, Value $V_{B \times S \times D}$. Attention matrix $A = \text{Softmax}\left(\frac{Q K^T}{\sqrt{D}}\right) \in \mathbb{R}^{B \times S \times S}$. Output $O = A V \in \mathbb{R}^{B \times S \times D}$ computes weighted linear combination of Value vectors.

## Level 5 — Interview Questions Solutions
### Question 1
1. Gauss-Markov theorem states that under zero-mean error $E[e]=0$ and homoscedastic un-correlated variance $E[e e^T] = \sigma^2 I$, the OLS estimator $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ has minimum variance among all linear unbiased estimators.
### Question 2
2. Using SVD $\mathbf{X} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$, pseudoinverse is $\mathbf{X}^+ = \mathbf{V}\mathbf{\Sigma}^+\mathbf{U}^T$. OLS solution $\mathbf{w} = \mathbf{X}^+ \mathbf{y}$ computes minimum-norm solution even when $\mathbf{X}$ is rank-deficient or non-square.
### Question 3
3. Let $L$ be scalar loss, $\mathbf{Z} = \mathbf{X}\mathbf{W} + \mathbf{b}$. Chain rule: $\frac{\partial L}{\partial W_{i,j}} = \sum_k \frac{\partial L}{\partial Z_{k,j}} \frac{\partial Z_{k,j}}{\partial W_{i,j}} = \sum_k X_{k,i} \delta_{k,j} = (\mathbf{X}^T \delta)_{i,j} \implies \frac{\partial L}{\partial \mathbf{W}} = \mathbf{X}^T \frac{\partial L}{\partial \mathbf{Z}}$.
### Question 4
4. Mercer's Theorem proves that any symmetric positive semi-definite kernel function $k(x, y)$ implicitly defines an inner product in a high-dimensional feature space $\mathcal{H}$: $k(x, y) = \langle \phi(x), \phi(y) \rangle_{\mathcal{H}}$, allowing non-linear decision boundaries via linear algebra in $\mathcal{H}$.
### Question 5
5. LoRA freezes pre-trained weight matrix $\mathbf{W}_0 \in \mathbb{R}^{d \times k}$ and injects trainable rank-$r$ decomposition $\Delta \mathbf{W} = \mathbf{B}_{d \times r} \mathbf{A}_{r \times k}$ where $r \ll \min(d, k)$. Forward pass $h = W_0 x + \frac{\alpha}{r} B A x$ updates models using 0.1% parameters.
