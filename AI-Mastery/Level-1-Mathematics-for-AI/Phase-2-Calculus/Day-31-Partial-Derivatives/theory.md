# Theory — Partial Derivatives

### 1. Simple Definition
A partial derivative measures how a multi-variable function changes when you tweak one specific variable while holding all other variables completely fixed.

### 2. Intuition
Imagine standing on a mountain slope. Moving North changes your elevation at a certain rate; moving East changes your elevation at a different rate. The North slope is $\frac{\partial f}{\partial y}$, and the East slope is $\frac{\partial f}{\partial x}$.

### 3. Mathematical Definition
For function $f(x, y)$, the partial derivative with respect to $x$ is defined as:

$$
\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}
$$

Variable $y$ is held constant.

### 4. Notation
\frac{\partial f}{\partial x}, f_x, \partial_x f. Curly 'd' $\partial$ denotes partial derivative.

### 5. Formula

$$
\text{Clairaut's Theorem: } \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} \quad \text{(if 2nd derivatives are continuous)}
$$

### 6. Symbol-by-Symbol Explanation
- $\partial$: Partial derivative symbol (curly d)
- $f_x, f_y$: Partial derivatives with respect to $x$ and $y$
- $f_{xy}$: Mixed second partial derivative

### 7. Step-by-Step Calculation
Calculate partial derivatives of $f(x, y) = 3x^2 y + 5y^3 - 4x$:
1. Partial w.r.t $x$ (treat $y$ as constant): $\frac{\partial f}{\partial x} = 3(2x)y + 0 - 4 = 6x y - 4$.
2. Partial w.r.t $y$ (treat $x$ as constant): $\frac{\partial f}{\partial y} = 3x^2(1) + 5(3y^2) - 0 = 3x^2 + 15y^2$.

### 8. Second Example
Verify Clairaut's Theorem for $f(x, y) = x^2 y^3$:
- $f_x = 2x y^3 \implies f_{xy} = \frac{\partial}{\partial y}[2x y^3] = 6x y^2$.
- $f_y = 3x^2 y^2 \implies f_{yx} = \frac{\partial}{\partial x}[3x^2 y^2] = 6x y^2$.
$f_{xy} = f_{yx} = 6x y^2$. Equal!

### 9. Common Mistakes
Accidentally differentiating non-target variables instead of holding them constant; confusing partial derivative $\frac{\partial f}{\partial x}$ with total derivative $\frac{df}{dx}$.

### 10. AI Connection
Loss function gradients: $L(w_1, w_2) = (w_1 x_1 + w_2 x_2 - y)^2$. To update $w_1$, we compute partial derivative $\frac{\partial L}{\partial w_1} = 2(w_1 x_1 + w_2 x_2 - y) x_1$.

### 11. Algorithm Connection
Gradient Descent, Backpropagation, Multi-Variable Optimization, Partial Differential Equations (PDEs).

### 12. Practical Interpretation
Partial derivatives allow multi-dimensional parameter optimization to be decomposed into independent scalar slope evaluations for each weight parameter.

### 13. Interview Insight
Q: 'What does $\frac{\partial L}{\partial w_i} = 0$ mean during neural network training?' A: It means the loss function is flat along the dimension of weight $w_i$, so updating $w_i$ alone will not immediately change the loss.

### 14. Summary
Partial derivative $\frac{\partial f}{\partial x_i}$ measures rate of change along variable $x_i$ while holding all other variables constant. Mixed partials match $f_{xy} = f_{yx}$.
