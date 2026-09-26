# Theory — Derivatives

### 1. Simple Definition
The derivative measures how fast a function's output changes when you make a tiny change to its input. It is the exact slope of the tangent line at that point.

### 2. Intuition
If $f(x)$ is a hill altitude and $x$ is your position, the derivative $f'(x)$ is the steepness of the hill under your feet. Uphill is positive slope, downhill is negative slope, peak/valley is zero slope.

### 3. Mathematical Definition
The derivative of function $f: \mathbb{R} \rightarrow \mathbb{R}$ at point $x$ is defined by:

$$
f'(x) = \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

if this limit exists.

### 4. Notation
$f'(x), \frac{df}{dx}, \frac{d}{dx}[f(x)], D f(x)$. Value at $x=a$ denoted $f'(a)$ or $\left.\frac{df}{dx}\right|_{x=a}$.

### 5. Formula

$$
\frac{d}{dx}[x^n] = n x^{n-1}, \quad \frac{d}{dx}[e^x] = e^x, \quad \frac{d}{dx}[\ln(x)] = \frac{1}{x}
$$

### 6. Symbol-by-Symbol Explanation
- $x^n$: Power function
- $n$: Real exponent
- $e^x$: Exponential function (its own derivative!)
- $\ln(x)$: Natural logarithm

### 7. Step-by-Step Calculation
Find derivative of $f(x) = x^3$ at $x = 2$ using power rule:
1. Apply power rule formula: $f'(x) = 3 x^{3-1} = 3 x^2$.
2. Substitute $x = 2$: $f'(2) = 3(2)^2 = 3(4) = 12$.
Slope of tangent line at $x=2$ is 12!

### 8. Second Example
Numerical derivative of $f(x) = x^2$ at $x=3$ using Central Difference ($h=0.001$):

$$
f'(3) \approx \frac{f(3.001) - f(2.999)}{2(0.001)} = \frac{9.006001 - 8.994001}{0.002} = \frac{0.012}{0.002} = 6.000
$$

### 9. Common Mistakes
Forgetting that $\frac{d}{dx}[e^x] = e^x$; assuming $|x|$ is differentiable at $x=0$ (sharp kink means derivative does not exist).

### 10. AI Connection
Sensitivity Analysis: Derivative $\frac{\partial L}{\partial w} = -0.5$ means increasing $w$ by $0.01$ will DECREASE loss by $0.005$.

### 11. Algorithm Connection
Gradient Descent, Newton's Method, Backpropagation, Automatic Differentiation.

### 12. Practical Interpretation
Central difference approximation error is $O(h^2)$, whereas forward difference error is $O(h)$, making central difference far more accurate in practice.

### 13. Interview Insight
Q: 'Why is central difference formula $\frac{f(x+h) - f(x-h)}{2h}$ more accurate than forward difference $\frac{f(x+h) - f(x)}{h}$?' A: Taylor expansion cancels out the first-order error terms $O(h)$, reducing numerical error to second-order $O(h^2)$.

### 14. Summary
Derivative $f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$ is the instantaneous slope. Key derivatives: $\frac{d}{dx} x^n = n x^{n-1}$, $\frac{d}{dx} e^x = e^x$, $\frac{d}{dx} \ln x = \frac{1}{x}$.
