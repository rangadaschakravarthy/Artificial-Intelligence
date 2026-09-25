# Practice Exercises — Derivative Rules

## Level 1 — Basic Understanding
1. What is the Product Rule for $\frac{d}{dx}[u(x) v(x)]$?
2. What is the Quotient Rule for $\frac{d}{dx}\left[\frac{u(x)}{v(x)}\right]$?
3. Calculate derivative of $f(x) = 4x^3 + 2x^2 - 7x$.
4. Calculate derivative of $f(x) = 5 e^x$.
5. State the derivative formula for Sigmoid function $\sigma(x)$.

## Level 2 — Calculation
1. Compute derivative of $f(x) = x^3 e^x$ using Product Rule.
2. Compute derivative of $f(x) = x^2 \ln(x)$ using Product Rule.
3. Compute derivative of $f(x) = \frac{e^x}{x}$ using Quotient Rule.
4. Evaluate Sigmoid derivative $\sigma'(x)$ at $x = 2$ given $\sigma(2) \approx 0.8808$.
5. Find derivative of $f(x) = \frac{x^2 + 1}{x - 1}$.

## Level 3 — Conceptual
1. Step-by-step derivation of $\sigma'(x) = \sigma(x)(1 - \sigma(x))$ starting from $\sigma(x) = (1 + e^{-x})^{-1}$.
2. Derive the derivative of Softplus function $f(x) = \ln(1 + e^x)$ and show it equals Sigmoid $\sigma(x)$.
3. Compute derivative of $f(x) = x \sigma(x)$ (Swish activation building block) using Product Rule.
4. Explain why the maximum value of Sigmoid derivative is $0.25$ at $x = 0$.
5. Compute derivative of $f(x) = \frac{1 - e^{-x}}{1 + e^{-x}}$ (Tanh variant).

## Level 4 — AI/ML Application
1. In Logistic Regression, binary cross-entropy loss is $L(w) = -y \ln(\sigma(w x)) - (1-y)\ln(1-\sigma(w x))$. Use derivative rules and Sigmoid derivative to show $\frac{d L}{d w} = (\sigma(w x) - y) x$.
2. Explain how PyTorch Autograd uses symbolic/numerical primitive derivative rules for reverse-mode automatic differentiation.
3. Compute derivative of Gaussian function $f(x) = e^{-x^2/2}$.

## Level 5 — Interview Questions
1. Derive the derivative of Hyperbolic Tangent $\text{tanh}(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ and show $\text{tanh}'(x) = 1 - \text{tanh}^2(x)$.
2. Derive Product Rule for 3 functions: $\frac{d}{dx}[u v w] = u' v w + u v' w + u v w'$.
3. Prove Quotient Rule using Product Rule and Power Rule on $u(x) [v(x)]^{-1}$.
4. What is the derivative of Softmax function $S_i = \frac{e^{z_i}}{\sum e^{z_k}}$ with respect to logit $z_j$? Show $\frac{\partial S_i}{\partial z_j} = S_i (\delta_{i,j} - S_j)$.
5. Explain how Automatic Differentiation avoids symbolic expression explosion using Dual Numbers ($a + b \epsilon$ where $\epsilon^2 = 0$).
