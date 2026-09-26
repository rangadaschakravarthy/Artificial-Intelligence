# Theory — Functions

### 1. Simple Definition
A function is a mathematical machine that takes an input $x$, applies a specific rule, and returns a single output $y = f(x)$.

### 2. Intuition
Think of a vending machine. Pressing button A1 (input) dispenses a soda (output). The vending machine is a function mapping button selections to items.

### 3. Mathematical Definition
A function $f: X \rightarrow Y$ is a relation that assigns to each element $x$ in domain $X$ exactly one element $y = f(x)$ in codomain/range $Y$.

### 4. Notation
$y = f(x)$. Domain $\text{Dom}(f) \subseteq \mathbb{R}^n$, Range $\text{Ran}(f) \subseteq \mathbb{R}^m$. Composite $(f \circ g)(x) = f(g(x))$.

### 5. Formula

$$
\text{Sigmoid: } \sigma(x) = \frac{1}{1 + e^{-x}}, \quad \text{ReLU: } f(x) = \max(0, x)
$$

### 6. Symbol-by-Symbol Explanation
- $x$: Input argument (independent variable)
- $e$: Euler's constant $\approx 2.71828$
- $\sigma(x)$: Output probability bounded in $(0, 1)$

### 7. Step-by-Step Calculation
Evaluate composite function $f(g(x))$ for $g(x) = 2x + 1$ and $f(u) = u^2$ at $x = 3$:
1. Inner function: $g(3) = 2(3) + 1 = 7$.
2. Outer function: $f(7) = 7^2 = 49$.
3. Thus $(f \circ g)(3) = 49$.

### 8. Second Example
Evaluate Sigmoid activation at $x = 0$:

$$
\sigma(0) = \frac{1}{1 + e^0} = \frac{1}{1 + 1} = \frac{1}{2} = 0.5
$$

### 9. Common Mistakes
Assuming a single input can have two different outputs in a valid function (fails vertical line test); confusing domain (valid inputs) with range (valid outputs).

### 10. AI Connection
Activation Functions introduce non-linearity. Without non-linear functions, a 100-layer neural network collapses into a simple 1-layer linear regression model!

### 11. Algorithm Connection
Universal Function Approximation Theorem, Neural Networks, Logistic Regression (Sigmoid), Softmax Classification.

### 12. Practical Interpretation
ReLU $f(x) = \max(0, x)$ outputs $x$ if positive, and 0 if negative, preventing negative signals from propagating.

### 13. Interview Insight
Q: 'Why can't a multi-layer neural network learn complex decision boundaries using only linear functions?' A: The composition of linear functions is always linear: $W_2(W_1 x + b_1) + b_2 = (W_2 W_1)x + (W_2 b_1 + b_2)$. Non-linear activations are required to fold space.

### 14. Summary
Functions map inputs to outputs. Deep learning stacks composite non-linear functions $f_L(\dots f_1(x))$ to approximate complex data relationships.
