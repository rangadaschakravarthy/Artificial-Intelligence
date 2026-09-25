# Theory — Gradient Descent in Machine Learning

### 1. Simple Definition
Applying Gradient Descent in ML means iteratively adjusting model weights along gradient vectors computed over data samples, with feature scaling used to make the loss surface easy to navigate.

### 2. Intuition
Imagine a steep narrow canyon. Without feature scaling, gradient descent bounces back and forth between the high canyon walls. Feature scaling widens the canyon into a round bowl so steps go straight to the bottom.

### 3. Mathematical Definition
Linear Regression Gradient: $\nabla_{\mathbf{w}} L = \frac{2}{N} \mathbf{X}^T (\mathbf{X}\mathbf{w} - \mathbf{y})$. Logistic Regression Gradient: $\nabla_{\mathbf{w}} L = \frac{1}{N} \mathbf{X}^T (\sigma(\mathbf{X}\mathbf{w}) - \mathbf{y})$. Feature Standardization: $x_{norm} = \frac{x - \mu}{\sigma}$.

### 4. Notation
$\mathbf{X}_{N \times d}$: Feature matrix. $\mathbf{w}$: Weight vector. $\sigma(z)$: Sigmoid function.

### 5. Formula
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \frac{1}{N} \mathbf{X}^T (\sigma(\mathbf{X}\mathbf{w}_t) - \mathbf{y})$$

### 6. Symbol-by-Symbol Explanation
- \mathbf{X}^T (\sigma(\mathbf{X}\mathbf{w}) - \mathbf{y}): Data-weighted residual error vector
- \eta: Learning rate hyperparameter

### 7. Step-by-Step Calculation
Logistic Regression update for 1 sample $x = 2$, label $y = 1$, weight $w = 0.5$, bias $b = 0$, $\eta = 0.1$:
1. Model output $z = 0.5(2) + 0 = 1.0 \implies \hat{y} = \sigma(1.0) \approx 0.7310$.
2. Residual error $\hat{y} - y = 0.7310 - 1.0 = -0.2690$.
3. Weight gradient $\frac{\partial L}{\partial w} = (-0.2690)(2) = -0.5380$.
4. Bias gradient $\frac{\partial L}{\partial b} = -0.2690$.
5. Weight update: $w_{new} = 0.5 - 0.1(-0.5380) = 0.5538$.

### 8. Second Example
Feature Standardization: Feature $x = [10, 20, 30]^T \implies \mu = 20, \sigma = \sqrt{66.67} \approx 8.165 \implies x_{norm} = [-1.225, 0, 1.225]^T$.

### 9. Common Mistakes
Forgetting to scale test data using training set mean $\mu$ and std $\sigma$ (data leakage!); fitting feature scaler on combined train+test set.

### 10. AI Connection
Batch Normalization in Deep Learning applies feature standardization at every hidden layer of a neural network, maintaining well-conditioned loss surfaces throughout deep architectures.

### 11. Algorithm Connection
Linear Regression, Logistic Regression, Batch Normalization, Layer Normalization, Feature Scalers.

### 12. Practical Interpretation
Condition Number $\kappa = \frac{\lambda_{max}}{\lambda_{min}}$ of $\mathbf{X}^T \mathbf{X}$. Unscaled features create $\kappa \gg 1000$ (ill-conditioned). Standardized features yield $\kappa \approx 1$ (perfect spherical bowl).

### 13. Interview Insight
Q: 'Why does Logistic Regression have the exact same gradient update form as Linear Regression?' A: Because both belong to the Exponential Family of Generalized Linear Models (GLMs) using canonical link functions, where negative log-likelihood gradients simplify to $\mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y})$.

### 14. Summary
SGD optimizes ML models via gradient updates $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L$. Feature standardization $z = \frac{x-\mu}{\sigma}$ conditions loss surfaces for fast convergence.
