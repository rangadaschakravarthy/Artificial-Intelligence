# Theory — Day 275: Regularization (Ridge, Lasso & ElasticNet)

### 6.1 Definition
Regularization (Ridge, Lasso & ElasticNet) is a fundamental pillar of supervised regression modeling. Controlling model complexity via $L_1$ and $L_2$ weight penalties, coefficient shrinkage, and feature selection.

### 6.2 Intuition
Imagine fitting a straight line (or multi-dimensional plane) through a cloud of data points such that the total vertical distance (residuals) between the line and the actual data points is minimized.

### 6.3 Why It Exists
Continuous target prediction (e.g., forecasting real estate prices, stock returns, temperature, or sales volume) requires quantitative functions that map input features to real-valued targets.

### 6.4 Real-World Analogy
Adjusting the dial on a furnace: Every degree increase in the dial (feature $x$) leads to a predictable, continuous rise in room temperature (target $y$).

### 6.5 Formal Definition
Given dataset $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^n$, the linear model assumes:

$$
y = \mathbf{x}^T \boldsymbol{\beta} + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2)
$$

### 6.6 Mathematical Representation
- **Hypothesis**:
  

$$
\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_d x_d = \mathbf{X}\boldsymbol{\beta}
$$

- **Loss Function (Mean Squared Error)**:
  

$$
\text{MSE}(\boldsymbol{\beta}) = \frac{1}{n} \sum_{i=1}^n (y_i - \mathbf{x}_i^T \boldsymbol{\beta})^2 = \frac{1}{n} \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2_2
$$

- **Normal Equation Closed-Form Solution**:
  

$$
\boldsymbol{\beta}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}
$$

- **Regularized Objectives**:
  - **Ridge ($L_2$)**: $\mathcal{L}_{\text{Ridge}} = \text{MSE} + \alpha \|\boldsymbol{\beta}\|_2^2$
  - **Lasso ($L_1$)**: $\mathcal{L}_{\text{Lasso}} = \text{MSE} + \alpha \|\boldsymbol{\beta}\|_1$

### 6.7 Worked Example
Given 3 points $(1, 2), (2, 3), (3, 5)$:
- $\bar{x} = 2, \bar{y} = 3.33$.
- $\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{(1-2)(2-3.33) + (2-2)(3-3.33) + (3-2)(5-3.33)}{(1-2)^2 + (2-2)^2 + (3-2)^2} = \frac{1.33 + 0 + 1.67}{1 + 0 + 1} = \frac{3}{2} = 1.5$.
- $\beta_0 = \bar{y} - \beta_1 \bar{x} = 3.33 - 1.5(2) = 0.33$.
- Model: $\hat{y} = 1.5 x + 0.33$.

### 6.8 ML Example
Predicting house prices: $\hat{y} = 150(\text{sqft}) + 12000(\text{bedrooms}) + 25000$.

### 6.9 Python Example
Scratch NumPy implementation using Normal Equation.

### 6.10 scikit-learn Example
`from sklearn.linear_model import LinearRegression, Ridge, Lasso`.

### 6.11 Common Mistakes
- Not standardizing features before applying $L_1/L_2$ regularization.
- Assuming linear relationships without inspecting residual plots.

### 6.12 Strengths
Highly interpretable, fast training/inference, analytical closed-form solution exists.

### 6.13 Weaknesses
Sensitive to outliers, struggles with complex non-linear relationships without feature engineering.

### 6.14 Real-World Applications
Real estate appraisal, demand forecasting, algorithmic trading, financial risk modeling.

### 6.15 Interview Insight
Be ready to derive the OLS Normal Equation $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ using matrix calculus ($\frac{\partial \text{MSE}}{\partial \boldsymbol{\beta}} = 0$).

### 6.16 Summary
Regularization (Ridge, Lasso & ElasticNet) models continuous quantitative targets through error minimization and parameter optimization.
