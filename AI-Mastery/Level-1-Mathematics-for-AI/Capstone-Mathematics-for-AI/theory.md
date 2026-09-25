# Theory — Capstone Mathematics for AI Engine Architecture

## 1. System Components
The Capstone system integrates all 4 curriculum phases:
1. **Phase 1 (Linear Algebra)**: Vectorized layer matrices $W^{(1)}, W^{(2)}$, dot products, activation matrix multiplication.
2. **Phase 2 (Calculus)**: Sigmoid non-linearities, loss gradients $\nabla_W L$, chain rule backpropagation, SGD updates.
3. **Phase 3 (Probability)**: Softmax probability conversion, Binary Cross-Entropy (Negative Log-Likelihood) loss, Naive Bayes likelihood updates.
4. **Phase 4 (Statistics)**: $Z$-score data standardization (`StandardScaler`), 2-sample Welch's t-test evaluation, Cohen's $d$ effect size, $95\%$ confidence intervals.

## 2. Mathematical Equations
- Forward Pass: $Z^{(1)} = X W^{(1)} + b^{(1)}, A^{(1)} = \text{ReLU}(Z^{(1)}), Z^{(2)} = A^{(1)} W^{(2)} + b^{(2)}, \hat{Y} = \sigma(Z^{(2)})$.
- Backprop Gradients: $\delta^{(2)} = \hat{Y} - Y, \nabla_{W^{(2)}} L = \frac{1}{m} (A^{(1)})^T \delta^{(2)}, \delta^{(1)} = (\delta^{(2)} (W^{(2)})^T) \odot I(Z^{(1)} > 0), \nabla_{W^{(1)}} L = \frac{1}{m} X^T \delta^{(1)}$.
