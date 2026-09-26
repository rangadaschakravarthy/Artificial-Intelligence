# Theory — Introduction to Calculus

### 1. Simple Definition
Calculus is the branch of mathematics that studies how things change continuously. Differential calculus measures instant rates of change (slopes), while integral calculus measures accumulated totals (areas).

### 2. Intuition
Imagine driving a car. Your speedometer doesn't show your average speed over the whole trip—it shows your INSTANTANEOUS speed at that exact millisecond. Differential calculus computes that instantaneous speed!

### 3. Mathematical Definition
Differential calculus computes the derivative $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$, which measures the instantaneous rate of change of function $f(x)$ at point $x$.

### 4. Notation
$\frac{dy}{dx}, f'(x), \dot{y}$. Instantaneous rate of change of $y$ with respect to $x$.

### 5. Formula

$$
\text{Average Rate of Change (Secant)} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}
$$

$$
\text{Instantaneous Rate of Change (Tangent)} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}
$$

### 6. Symbol-by-Symbol Explanation
- $f(x)$: Objective function (e.g. Loss/Error curve)
- $\Delta x$: Small change in input parameter
- $\Delta y$: Resulting change in output error

### 7. Step-by-Step Calculation
Calculate average rate of change of $f(x) = x^2$ from $x_1 = 2$ to $x_2 = 4$:
1. $f(2) = 2^2 = 4$
2. $f(4) = 4^2 = 16$
3. $\text{Slope} = \frac{16 - 4}{4 - 2} = \frac{12}{2} = 6$.
Now shrink interval: $x_1 = 2, x_2 = 2.01 \implies f(2.01) = 4.0401 \implies \text{Slope} = \frac{4.0401 - 4}{0.01} = 4.01 \approx 4$.

### 8. Second Example
Instantaneous rate of change of $f(x) = 3x + 5$: Slope is constant $= 3$ at all points $x$.

### 9. Common Mistakes
Confusing average rate of change over a wide interval with instantaneous derivative at a point.

### 10. AI Connection
Loss curve optimization: Model error $L(w)$ is a curve. Calculus tells us if increasing weight $w$ increases or decreases error $L$.

### 11. Algorithm Connection
Gradient Descent, Backpropagation, Adam Optimizer, Support Vector Machines.

### 12. Practical Interpretation
Negative slope $\implies$ increasing $x$ decreases $y$. Positive slope $\implies$ increasing $x$ increases $y$. Zero slope $\implies$ flat minimum/maximum point!

### 13. Interview Insight
Q: 'Why do we need differential calculus in machine learning?' A: Because ML model weights are optimized iteratively by following the negative slope (derivative) of the loss function toward the lowest point (minimum error).

### 14. Summary
Calculus measures continuous change. Differential calculus finds instantaneous slopes $\frac{df}{dx}$, allowing AI algorithms to adjust parameters to minimize loss.
