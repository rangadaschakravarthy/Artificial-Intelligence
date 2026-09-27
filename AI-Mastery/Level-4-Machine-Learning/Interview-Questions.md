# Machine Learning Comprehensive Interview Questions & Solutions

## 1. Fundamentals & Workflow
- **Q**: What is the difference between traditional software engineering and Machine Learning?
- **A**: Traditional programming takes Data + Rules to generate Answers ($y = f(x, \text{rules})$). Machine Learning ingests Data + Sample Answers to learn the mapping rules automatically ($\hat{f} = \arg\min \mathcal{L}(f(X), y)$).

- **Q**: Explain the Bias-Variance Tradeoff.
- **A**: Bias is error from overly simple assumptions (underfitting). Variance is error from extreme sensitivity to training noise (overfitting). Total Expected Error = $\text{Bias}^2 + \text{Variance} + \text{Irreducible Error}$. Optimal ML balances model capacity to minimize total error.

## 2. Regression & Regularization
- **Q**: Derive the OLS Normal Equation $\boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$.
- **A**: Set the gradient of MSE loss to zero: $\frac{\partial}{\partial \boldsymbol{\beta}} \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2 = -2\mathbf{X}^T(\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) = 0 \implies \mathbf{X}^T\mathbf{X}\boldsymbol{\beta} = \mathbf{X}^T\mathbf{y} \implies \boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$.

- **Q**: How do Ridge ($L_2$) and Lasso ($L_1$) regularization differ?
- **A**: Ridge adds penalty $\alpha \sum \beta_j^2$, shrinking weights continuously towards zero without setting them strictly to zero. Lasso adds penalty $\alpha \sum |\beta_j|$, producing sparse models by driving uninformative feature weights exactly to zero (performing feature selection).

## 3. Classification & Metrics
- **Q**: Why is Logistic Regression called regression if it is used for classification?
- **A**: It fits a continuous linear regression model to the log-odds $\log\left(\frac{p}{1-p}\right) = \mathbf{w}^T\mathbf{x} + b$, which is then mapped through the Sigmoid function to output valid probabilities.

- **Q**: Explain Precision vs Recall and state when you would prioritize each.
- **A**: Precision ($\frac{TP}{TP+FP}$) measures positive prediction accuracy; prioritize when False Positives are costly (e.g., Spam filter). Recall ($\frac{TP}{TP+FN}$) measures positive case coverage; prioritize when False Negatives are fatal (e.g., Cancer detection).

## 4. Unsupervised & Reinforcement Learning
- **Q**: How does PCA compute principal components?
- **A**: PCA standardizes data, computes sample covariance matrix $\boldsymbol{\Sigma} = \frac{1}{n-1}\mathbf{X}^T\mathbf{X}$, and performs eigen-decomposition $\boldsymbol{\Sigma}\mathbf{v}_j = \lambda_j \mathbf{v}_j$. Eigenvectors represent orthogonal principal axes, and eigenvalues quantify variance explained along each axis.

- **Q**: What is the Bellman Optimality Equation in Q-Learning?
- **A**: $Q^*(s, a) = R(s, a) + \gamma \sum_{s'} P(s'|s,a) \max_{a'} Q^*(s', a')$. Q-learning approximates this via temporal difference updates: $Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s,a)]$.
