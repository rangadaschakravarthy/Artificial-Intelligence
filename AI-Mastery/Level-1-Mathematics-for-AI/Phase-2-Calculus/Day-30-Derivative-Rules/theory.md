# Theory — Derivative Rules

### 1. Simple Definition
Derivative rules are algebraic shortcuts that allow us to quickly find the derivative of complex functions built by adding, multiplying, or dividing simpler functions.

### 2. Intuition
Instead of computing limits from scratch every time, derivative rules give us a toolbox: the derivative of a sum is the sum of derivatives, but the derivative of a product requires a special cross-term pattern.

### 3. Mathematical Definition
For differentiable functions $u(x), v(x)$ and constant $c \in \mathbb{R}$:
1) $(c u)' = c u'$
2) $(u \pm v)' = u' \pm v'$
3) $(u v)' = u' v + u v'$
4) $\left(\frac{u}{v}\right)' = \frac{u' v - u v'}{v^2}$.

### 4. Notation
$\frac{d}{dx}[u \cdot v] = u' v + u v'$. $\frac{d}{dx}\left[\frac{u}{v}\right] = \frac{u' v - u v'}{v^2}$.

### 5. Formula
$$\text{Sigmoid Derivative: } \sigma'(x) = \sigma(x) (1 - \sigma(x))$$

### 6. Symbol-by-Symbol Explanation
- $u(x), v(x)$: Differentiable functions
- $u', v'$: Respective derivatives
- $\sigma(x)$: Sigmoid function $\frac{1}{1+e^{-x}}$

### 7. Step-by-Step Calculation
Derive Sigmoid derivative using Quotient Rule $\sigma(x) = \frac{1}{1 + e^{-x}}$:
1. Let $u = 1 \implies u' = 0$. Let $v = 1 + e^{-x} \implies v' = -e^{-x}$.
2. Quotient Rule: $\sigma'(x) = \frac{0(1 + e^{-x}) - 1(-e^{-x})}{(1 + e^{-x})^2} = \frac{e^{-x}}{(1 + e^{-x})^2}$.
3. Split fraction: $\frac{1}{1 + e^{-x}} \cdot \frac{e^{-x}}{1 + e^{-x}} = \sigma(x) \left(\frac{(1 + e^{-x}) - 1}{1 + e^{-x}}\right) = \sigma(x) (1 - \sigma(x))$. Done!

### 8. Second Example
Product Rule for $f(x) = x^2 e^x$:
Let $u = x^2 \implies u' = 2x$. Let $v = e^x \implies v' = e^x$.
$f'(x) = u'v + uv' = 2x e^x + x^2 e^x = x e^x (2 + x)$.

### 9. Common Mistakes
Writing derivative of product as product of derivatives: $(u v)' = u' v'$ (WRONG! Must use Product Rule $u'v + uv'$).

### 10. AI Connection
Sigmoid derivative $\sigma'(x) = \sigma(x)(1 - \sigma(x))$ is used directly in Logistic Regression gradient updates and neural network backpropagation.

### 11. Algorithm Connection
Logistic Regression, Backpropagation, Neural Network Activations, SymPy Symbolic Math.

### 12. Practical Interpretation
Max value of Sigmoid derivative $\sigma'(0) = 0.5(1 - 0.5) = 0.25$. Since $0.25 < 1$, stacking many Sigmoid layers causes gradients to shrink by $0.25$ each layer (vanishing gradient!).

### 13. Interview Insight
Q: 'Why does Sigmoid cause vanishing gradients in deep networks?' A: Because its derivative maxes out at $0.25$. Multiplying numbers $\le 0.25$ across 10 layers shrinks gradients to $0.25^{10} \approx 10^{-7}$, stopping learning.

### 14. Summary
Derivative rules simplify complex calculus: Sum $(u+v)'=u'+v'$, Product $(uv)'=u'v+uv'$, Quotient $(u/v)'=\frac{u'v-uv'}{v^2}$. Key ML result: $\sigma'(x) = \sigma(x)(1-\sigma(x))$.
