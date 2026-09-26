# Theory — Limits

### 1. Simple Definition
A limit is the value that a function approaches as the input gets closer and closer to a specific point, even if the function is not defined at that exact point.

### 2. Intuition
Imagine walking toward a destination point. Even if there is a hole in the ground at the exact destination mark, your path steps clearly point toward that target location. That target location is the limit!

### 3. Mathematical Definition
Formal $\epsilon-\delta$ definition: $\lim_{x \to c} f(x) = L$ means for every $\epsilon > 0$, there exists $\delta > 0$ such that $0 < |x - c| < \delta \implies |f(x) - L| < \epsilon$.

### 4. Notation
$\lim_{x \to c} f(x) = L$. Read: 'The limit of $f(x)$ as $x$ approaches $c$ is $L$'.

### 5. Formula

$$
\text{L'Hôpital's Rule: If } \lim_{x \to c} \frac{f(x)}{g(x)} = \frac{0}{0} \text{ or } \frac{\pm \infty}{\pm \infty} \implies \lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}
$$

### 6. Symbol-by-Symbol Explanation
- $c$: Point being approached by $x$
- $L$: Target limit output value
- $f'(x), g'(x)$: Derivatives of numerator and denominator

### 7. Step-by-Step Calculation
Evaluate $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$:
1. Direct substitution: $\frac{2^2 - 4}{2 - 2} = \frac{0}{0}$ (Indeterminate form!).
2. Factor numerator: $\frac{(x-2)(x+2)}{x-2} = x + 2$ for $x \neq 2$.
3. Take limit: $\lim_{x \to 2} (x + 2) = 2 + 2 = 4$.

### 8. Second Example
Solve same limit using L'Hôpital's Rule:
$\lim_{x \to 2} \frac{\frac{d}{dx}(x^2 - 4)}{\frac{d}{dx}(x - 2)} = \lim_{x \to 2} \frac{2x}{1} = 2(2) = 4$. Same answer!

### 9. Common Mistakes
Assuming a limit doesn't exist just because direct substitution gives $0/0$ (you MUST simplify or use L'Hôpital's Rule!).

### 10. AI Connection
Computing Binary Cross-Entropy Loss: $\log(y)$ as $y \to 0$ approaches $-\infty$. AI frameworks use clipping $\text{clip}(y, \epsilon, 1-\epsilon)$ with $\epsilon = 10^{-7}$ to avoid `NaN` overflow.

### 11. Algorithm Connection
Log-Sum-Exp Trick, Softmax Stability, Automatic Differentiation, Continuous Optimization.

### 12. Practical Interpretation
A function is continuous at $x = c$ if $\lim_{x \to c} f(x) = f(c)$. Smooth continuous functions allow gradient descent to take continuous steps.

### 13. Interview Insight
Q: 'What is the Log-Sum-Exp trick in Softmax and why is it used?' A: Exponentiating large logits $e^{1000}$ causes numerical overflow ($
\infty$). We subtract $\max(z)$ using identity $\lim \log \sum e^{z_i - z_{max}} + z_{max}$, maintaining exact values safely.

### 14. Summary
Limits evaluate function behavior as inputs approach a point $\lim_{x \to c} f(x) = L$. Indeterminate forms $0/0$ are solved via factoring or L'Hôpital's Rule $\lim \frac{f'}{g'}$.
