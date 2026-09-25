# Theory — Chain Rule

### 1. Simple Definition
The Chain Rule tells us how to find the derivative of a composite function (a function inside another function) by multiplying the derivatives of each step together.

### 2. Intuition
Imagine gear wheels. If Gear A turns 2x faster than Gear B, and Gear B turns 3x faster than Gear C, then Gear A turns $2 \times 3 = 6\text{x}$ faster than Gear C! Chain rule multiplies the ratios.

### 3. Mathematical Definition
Single-variable: If $y = f(u)$ and $u = g(x)$, then $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = f'(g(x)) g'(x)$.
Multi-variable: If $z = f(u, v)$ with $u = u(t), v = v(t)$, then $\frac{dz}{dt} = \frac{\partial z}{\partial u} \frac{du}{dt} + \frac{\partial z}{\partial v} \frac{dv}{dt}$.

### 4. Notation
$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$ or $(f \circ g)'(x) = f'(g(x)) g'(x)$.

### 5. Formula
$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial z} \cdot \frac{\partial z}{\partial w} \quad \text{(Backpropagation Chain)}$$

### 6. Symbol-by-Symbol Explanation
- $L$: Loss function output
- $y$: Model prediction
- $z$: Pre-activation value ($w x + b$)
- $w$: Model weight parameter

### 7. Step-by-Step Calculation
Differentiate $y = (3x^2 + 1)^4$:
1. Outer function $y = u^4 \implies \frac{dy}{du} = 4 u^3$.
2. Inner function $u = 3x^2 + 1 \implies \frac{du}{dx} = 6x$.
3. Chain Rule: $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = 4 u^3 (6x) = 4(3x^2 + 1)^3 (6x) = 24x(3x^2 + 1)^3$.

### 8. Second Example
Neural layer derivative $\frac{d}{dw}[\sigma(w x + b)]$: Let $z = w x + b \implies \frac{dz}{dw} = x$. Output $y = \sigma(z) \implies \frac{dy}{dz} = \sigma(z)(1-\sigma(z))$. Chain Rule: $\frac{dy}{dw} = \sigma(z)(1-\sigma(z)) x$.

### 9. Common Mistakes
Forgetting to multiply by the derivative of the inner function (the 'inside' derivative).

### 10. AI Connection
Backpropagation: To compute gradient $\frac{\partial Loss}{\partial W_1}$ for Layer 1 weights, we multiply gradients backward through Layer 3, Layer 2, and Layer 1 via Chain Rule.

### 11. Algorithm Connection
Backpropagation, Reverse-Mode Automatic Differentiation, PyTorch Autograd, TensorFlow GradientTape.

### 12. Practical Interpretation
Chain rule multiplies local derivatives along paths in computational graphs. Multiple paths sum their chain derivatives together.

### 13. Interview Insight
Q: 'Why is Reverse-Mode Automatic Differentiation (Backprop) faster than Forward-Mode for deep neural networks?' A: Forward-mode computes derivatives w.r.t 1 input parameter per pass ($O(N_{inputs})$ passes). Reverse-mode computes derivatives w.r.t ALL parameters in 1 single backward pass ($O(1)$ pass).

### 14. Summary
Chain Rule $\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}$ multiplies intermediate derivatives. Multi-variable chain rule sums across parallel paths. It is the mathematical core of Backpropagation.
