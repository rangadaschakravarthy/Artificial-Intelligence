# Theory — Loss Functions

### 1. Simple Definition
A loss function is a mathematical score that measures how far off an AI model's prediction is from the true target value. Optimization strives to drive this loss score down to zero.

### 2. Intuition
Think of target shooting. Loss measures how far your arrow lands from the bullseye. If you hit 5 inches to the right, loss measures that distance error so you can aim better next time.

### 3. Mathematical Definition
MSE: $L_{MSE}(y, \hat{y}) = (y - \hat{y})^2$. BCE: $L_{BCE}(y, \hat{y}) = -y \ln(\hat{y}) - (1-y) \ln(1-\hat{y})$ for $y \in \{0, 1\}, \hat{y} \in (0, 1)$. CCE: $L_{CCE}(\mathbf{y}, \hat{\mathbf{y}}) = -\sum_{c=1}^C y_c \ln(\hat{y}_c)$.

### 4. Notation
$L(y, \hat{y})$ for single sample loss. $J(\mathbf{w}) = \frac{1}{N} \sum_{i=1}^N L(y_i, \hat{y}_i)$ for total dataset cost.

### 5. Formula

$$
\frac{\partial L_{MSE}}{\partial \hat{y}} = -2(y - \hat{y}), \quad \frac{\partial L_{BCE}}{\partial \hat{y}} = \frac{\hat{y} - y}{\hat{y}(1-\hat{y})}
$$

### 6. Symbol-by-Symbol Explanation
- $y$: True ground truth target label
- \hat{y}: Model predicted output probability/value
- $N$: Number of samples
- $C$: Number of categories

### 7. Step-by-Step Calculation
Calculate MSE and BCE loss for true label $y = 1$ and prediction $\hat{y} = 0.8$:
1. MSE: $L_{MSE} = (1 - 0.8)^2 = (0.2)^2 = 0.04$.
2. BCE: $L_{BCE} = -[1 \cdot \ln(0.8) + 0 \cdot \ln(0.2)] = -\ln(0.8) \approx -(-0.2231) = 0.2231$.
3. Derivative $\frac{\partial L_{MSE}}{\partial \hat{y}} = -2(1 - 0.8) = -0.4$.

### 8. Second Example
Calculate Huber Loss ($d = y - \hat{y}$, threshold $\delta = 1.0$):

$$
\text{Huber}(d) = \begin{cases} \frac{1}{2} d^2 & \text{if } |d| \le \delta \\ \delta(|d| - \frac{1}{2}\delta) & \text{if } |d| > \delta \end{cases}
$$

For small error $d=0.5 \le 1.0 \implies \frac{1}{2}(0.25) = 0.125$. For large outlier error $d=5.0 > 1.0 \implies 1.0(5.0 - 0.5) = 4.5$ (Linear penalty instead of quadratic 12.5!).

### 9. Common Mistakes
Using MSE for classification (causes non-convex loss surfaces with flat zero-gradient regions); forgetting natural log $\ln$ in cross-entropy.

### 10. AI Connection
Loss selection dictates model behavior: MSE penalizes large errors quadratically (sensitive to outliers). MAE penalizes errors linearly (robust). BCE uses maximum likelihood estimation for probabilities.

### 11. Algorithm Connection
Linear Regression (MSE), Logistic Regression (BCE), Multi-class Classifiers (CCE), Robust Regression (Huber).

### 12. Practical Interpretation
Combining Softmax output with Categorical Cross-Entropy produces a clean simplified gradient $\frac{\partial L}{\partial \mathbf{z}} = \hat{\mathbf{y}} - \mathbf{y}$.

### 13. Interview Insight
Q: 'Why is Cross-Entropy preferred over MSE for binary classification with Sigmoid activations?' A: Using MSE with Sigmoid produces a non-convex loss surface with vanishing gradients. Cross-entropy cancels out the Sigmoid denominator, yielding a strictly convex loss function with strong linear gradient signals $\hat{y} - y$.

### 14. Summary
Loss functions quantify error: MSE for regression ($y-\hat{y})^2$, BCE for binary classification $-[y \ln \hat{y} + (1-y)\ln(1-\hat{y})]$, CCE for multi-class. Huber loss combines L1 and L2 for outlier robustness.
