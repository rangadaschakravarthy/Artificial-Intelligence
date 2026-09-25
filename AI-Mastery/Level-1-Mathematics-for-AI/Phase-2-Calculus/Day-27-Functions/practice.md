# Practice Exercises — Functions

## Level 1 — Basic Understanding
1. What is the domain and range of $f(x) = x^2$?
2. Evaluate Sigmoid function $\sigma(x) = \frac{1}{1+e^{-x}}$ at $x = 0$.
3. Evaluate ReLU function $f(x) = \max(0, x)$ for $x = -5$ and $x = 3$.
4. If $g(x) = x + 2$ and $f(u) = 3u$, calculate composite $f(g(4))$.
5. Why is $f(x) = \frac{1}{x}$ undefined at $x = 0$?

## Level 2 — Calculation
1. Find the domain of $f(x) = \sqrt{x - 4}$.
2. Find the domain of logarithmic function $f(x) = \ln(x)$.
3. Given $g(x) = x^2$ and $f(u) = \frac{1}{1+e^{-u}}$, write explicit formula for composite $(f \circ g)(x)$.
4. Compute Softmax for vector $\mathbf{z} = [1, 2]^T$ using formula $S_i = \frac{e^{z_i}}{e^{z_1} + e^{z_2}}$.
5. Is the LeakyReLU function $f(x) = \max(0.01x, x)$ linear or non-linear?

## Level 3 — Conceptual
1. Prove that the composition of two linear functions $f(x) = a x + b$ and $g(x) = c x + d$ is always linear.
2. Explain the Universal Approximation Theorem for neural networks.
3. Why does Log-Loss (Binary Cross-Entropy) use natural logarithm $\ln(p)$?
4. What is the vanishing gradient problem associated with the Sigmoid activation function at extreme values ($x = 10$ or $x = -10$)?
5. Compare ReLU vs GELU (Gaussian Error Linear Unit) activation functions.

## Level 4 — AI/ML Application
1. Plot or calculate Sigmoid $\sigma(x)$ for $x \in \{-5, -2, 0, 2, 5\}$. Show that $\sigma(-x) = 1 - \sigma(x)$.
2. A Binary Logistic Regression model outputs raw logit $z = \mathbf{w}^T \mathbf{x} + b = 2.197$. Calculate output probability $p = \sigma(z)$ using $e^{2.197} \approx 9.0$.
3. Explain how Softmax converts raw neural network logit vectors into a categorical probability distribution summing to 1.

## Level 5 — Interview Questions
1. Prove the Sigmoid identity $\sigma(-x) = 1 - \sigma(x)$.
2. Derive the inverse of Sigmoid function (Logit function) $x = \sigma^{-1}(p) = \ln\left(\frac{p}{1-p}\right)$.
3. Explain Swish activation function $f(x) = x \cdot \sigma(\beta x)$ developed by Google Brain.
4. What is a Lipschitz Continuous Function and how does Lipschitz constant $L$ bound neural network generalization error?
5. Explain Convex Functions ($f(\alpha x + (1-\alpha)y) \le \alpha f(x) + (1-\alpha)f(y)$) and why local minima equal global minima for convex functions.
