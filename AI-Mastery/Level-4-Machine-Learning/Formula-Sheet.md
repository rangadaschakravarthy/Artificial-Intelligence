# Machine Learning Formula Sheet

## 1. Regression & Linear Models
- **Linear Regression Hypothesis**: $\hat{y} = \mathbf{x}^T \boldsymbol{\beta} = \beta_0 + \beta_1 x_1 + \dots + \beta_d x_d$
- **Mean Squared Error (MSE)**: $\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2$
- **OLS Normal Equation**: $\boldsymbol{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$
- **Ridge Regression ($L_2$) Loss**: $\mathcal{L}_{\text{Ridge}} = \frac{1}{n} \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \alpha \|\boldsymbol{\beta}\|_2^2$
- **Lasso Regression ($L_1$) Loss**: $\mathcal{L}_{\text{Lasso}} = \frac{1}{n} \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \alpha \|\boldsymbol{\beta}\|_1$
- **Gradient Descent Parameter Update**: $\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} - \alpha \nabla_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}^{(t)})$

## 2. Classification & Probability
- **Sigmoid Activation Function**: $\sigma(z) = \frac{1}{1 + e^{-z}} = \frac{e^z}{1 + e^z}$
- **Binary Cross-Entropy Loss**: $\mathcal{L} = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$
- **Bayes Theorem**: $P(Y = c \mid \mathbf{x}) = \frac{P(\mathbf{x} \mid Y = c) P(Y = c)}{P(\mathbf{x})}$
- **Entropy**: $\text{Entropy}(S) = -\sum_{i=1}^K p_i \log_2(p_i)$
- **Gini Impurity**: $\text{Gini}(S) = 1 - \sum_{i=1}^K p_i^2$

## 3. Unsupervised Learning
- **K-Means Inertia**: $\text{Inertia} = \sum_{k=1}^K \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \boldsymbol{\mu}_k\|^2$
- **Sample Covariance Matrix**: $\boldsymbol{\Sigma} = \frac{1}{n-1} \mathbf{X}^T \mathbf{X}$
- **PCA Eigen-Equation**: $\boldsymbol{\Sigma} \mathbf{v}_j = \lambda_j \mathbf{v}_j$
- **Lift**: $\text{Lift}(X \to Y) = \frac{P(X \cap Y)}{P(X) P(Y)}$

## 4. Reinforcement Learning
- **Discounted Cumulative Return**: $G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$
- **Q-Learning Temporal Difference Update**:
  

$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha \left[ R_{t+1} + \gamma \max_a Q(S_{t+1}, a) - Q(S_t, A_t) \right]
$$

