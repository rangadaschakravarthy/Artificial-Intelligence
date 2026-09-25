# Practice Exercises — Gradient Descent in Machine Learning

## Level 1 — Basic Understanding
1. What is feature standardization?
2. Formula for z-score standardization $z$.
3. Why do unscaled features slow down Gradient Descent?
4. What is the gradient equation for Logistic Regression?
5. How do you detect if a model is underfitting from loss curves?

## Level 2 — Calculation
1. Standardize dataset feature column $x = [2, 4, 6, 8]^T$ (Compute mean $\mu$ and std $\sigma$).
2. Given 1 Logistic Regression sample $x = 1.0, y = 0$, weight $w = 1.0, b = 0$, compute prediction $\hat{y} = \sigma(1.0)$ and weight gradient.
3. If feature 1 ranges $[0, 1]$ and feature 2 ranges $[0, 1000000]$, describe the shape of loss contour lines.
4. What is Min-Max Normalization $x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}$?
5. When is Min-Max normalization preferred over Z-score Standardization?

## Level 3 — Conceptual
1. Prove that feature standardization sets sample mean to 0 and variance to 1.
2. Show how feature covariance matrix $\mathbf{\Sigma}$ changes when features are standardized.
3. Explain Data Leakage: why feature scalers MUST be fit ONLY on training data $\mathbf{X}_{train}$ and then applied to $\mathbf{X}_{test}$.
4. Explain Early Stopping regularization using validation loss monitoring.
5. Why is Tree-based algorithms (Random Forest, XGBoost) immune to feature scale, unlike Gradient Descent models?

## Level 4 — AI/ML Application
1. Implement Logistic Regression SGD from scratch in Python with mini-batching and feature standardization. Train on synthetic binary classification data.
2. Benchmark convergence speed (number of epochs to reach loss $< 0.1$) for scaled vs unscaled features in Python.
3. Explain Batch Normalization $\hat{x} = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$, $y = \gamma \hat{x} + \beta$ inside neural networks.

## Level 5 — Interview Questions
1. Prove that Generalized Linear Models (GLMs) with canonical link functions always yield gradient $\nabla_{\mathbf{w}} L = \frac{1}{N} \mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y})$.
2. Explain Hessian conditioning for unscaled features: $\mathbf{H} = \frac{2}{N} \mathbf{X}^T \mathbf{X}$, showing ratio $\frac{\lambda_{max}}{\lambda_{min}}$ scales with feature variance ratios.
3. Derive exact mathematical formulation for Soft-Margin Support Vector Machine SGD updates (Hinge Loss gradient).
4. Explain Second-Order Optimization (L-BFGS) for Logistic Regression when dataset fits in RAM.
5. Explain Layer Normalization vs Group Normalization vs Instance Normalization in Vision and NLP Transformers.
