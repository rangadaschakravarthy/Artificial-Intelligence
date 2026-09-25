# Solutions — Gradient Descent in Machine Learning

## Level 1 — Basic Understanding Solutions
### Question 1
1. Rescaling feature columns to have mean $= 0$ and standard deviation $= 1$.
### Question 2
2. $z = \frac{x - \mu}{\sigma}$.
### Question 3
3. Unscaled features create elongated elliptical loss contours, causing gradient vectors to oscillate sideways instead of stepping toward minimum.
### Question 4
4. $\nabla_{\mathbf{w}} L = \frac{1}{N} \mathbf{X}^T (\sigma(\mathbf{X}\mathbf{w}) - \mathbf{y})$.
### Question 5
5. Both training loss and validation loss remain high and refuse to decrease.

## Level 2 — Calculation Solutions
### Question 1
1. Mean $\mu = 5.0$. Variance $= \frac{(9+1+1+9)}{4} = 5.0 \implies \sigma = \sqrt{5.0} \approx 2.236$. $z = [\frac{-3}{2.236}, \frac{-1}{2.236}, \frac{1}{2.236}, \frac{3}{2.236}]^T = [-1.342, -0.447, 0.447, 1.342]^T$.
### Question 2
2. $z = 1.0(1.0) = 1.0 \implies \hat{y} = \sigma(1.0) \approx 0.7310$. Error $\hat{y} - y = 0.7310 - 0 = 0.7310$. Weight gradient $= (0.7310)(1.0) = 0.7310$.
### Question 3
3. Extremely narrow, highly stretched ellipses (ill-conditioned loss surface).
### Question 4
4. Scales values strictly into range $[0, 1]$.
### Question 5
5. When features have fixed bounded ranges (e.g. image pixel intensities $[0, 255]$) or when algorithms require non-negative inputs.

## Level 3 — Conceptual Solutions
### Question 1
1. Mean: $E[z] = E[\frac{x-\mu}{\sigma}] = \frac{E[x] - \mu}{\sigma} = \frac{\mu - \mu}{\sigma} = 0$. Variance: $\text{Var}(z) = \text{Var}(\frac{x-\mu}{\sigma}) = \frac{\text{Var}(x)}{\sigma^2} = \frac{\sigma^2}{\sigma^2} = 1$.
### Question 2
2. Standardizing sets all diagonal entries of covariance matrix to 1 (unit variance $\Sigma_{i,i} = 1$), leaving off-diagonal entries as Pearson correlation coefficients $r_{i,j}$.
### Question 3
3. Fitting scaler on test data leaks test set statistics (mean/std) into training process, distorting real-world generalization performance metrics.
### Question 4
4. Early stopping monitors validation loss after each epoch, saving model weights when val loss reaches minimum and stopping training if val loss increases for $P$ consecutive epochs (patience).
### Question 5
5. Decision trees split nodes using threshold inequalities ($x_i > \text{threshold}$), which depends only on monotonic order of values, completely unaffected by linear scaling.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Class `LogisticRegressionSGD`: initialize $w=0, b=0$. `fit()` standardizes $X$, runs mini-batch SGD loop, computes $\hat{y} = \sigma(X_b w + b)$, updates $w -= \eta \nabla w$, tracks BCE loss.
### Question 2
2. Unscaled features require 200+ epochs due to gradient side-to-side oscillation. Standardized features converge smoothly in < 20 epochs (10x faster!).
### Question 3
3. BatchNorm normalizes activations along mini-batch axis: $\hat{x} = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$. Learnable scale $\gamma$ and shift $\beta$ allow network to restore representation capacity while keeping loss surface well-conditioned.

## Level 5 — Interview Questions Solutions
### Question 1
1. Exponential family PDF $P(y|x) = \exp\left(\frac{y \theta - b(\theta)}{a(\phi)} + c(y, \phi)\right)$. Canonical link maps $\theta = \mathbf{w}^T \mathbf{x}$, mean $\hat{y} = b'(\theta)$. Log-likelihood gradient $\nabla_{\mathbf{w}} \ln P = \frac{y - b'(\theta)}{a(\phi)} \mathbf{x} = \frac{y - \hat{y}}{a(\phi)} \mathbf{x}$. Negative log-likelihood gradient is $\frac{1}{N} \mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y})$.
### Question 2
2. Hessian $\mathbf{H} = \frac{2}{N} \mathbf{X}^T \mathbf{X}$. Eigenvalues $\lambda_i$ of $\mathbf{H}$ are proportional to sample variances along principal component directions of $\mathbf{X}$. Large variance ratio $\frac{\sigma_{max}^2}{\sigma_{min}^2}$ causes condition number $\kappa(\mathbf{H}) \gg 1$, forcing small $\eta < \frac{2}{\lambda_{max}}$ and slow progress along $\lambda_{min}$.
### Question 3
3. SVM Hinge Loss $L(w) = \frac{1}{2} ||w||_2^2 + C \sum \max(0, 1 - y_i (w^T x_i + b))$. Gradient w.r.t $w$: $\nabla_w L = w - C \sum_{i \in \text{margin}} y_i x_i$, where margin condition is $y_i (w^T x_i + b) < 1$.
### Question 4
4. L-BFGS evaluates exact batch gradients and builds inverse Hessian approximation $B_t \approx \mathbf{H}^{-1}$. Takes quasi-Newton steps $\Delta w = -B_t \nabla L$, converging in < 20 iterations for moderate datasets fitting in RAM.
### Question 5
5. LayerNorm normalizes across features for each sample (NLP Transformers). InstanceNorm normalizes across spatial pixels for each channel/sample (Style Transfer). GroupNorm divides channels into groups normalizing within each group (small batch Vision models).
