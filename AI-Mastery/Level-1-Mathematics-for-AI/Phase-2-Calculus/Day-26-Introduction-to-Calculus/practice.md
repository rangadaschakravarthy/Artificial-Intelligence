# Practice Exercises — Introduction to Calculus

## Level 1 — Basic Understanding
1. What is the difference between differential calculus and integral calculus?
2. What is the average rate of change of $f(x) = x^2$ from $x=1$ to $x=4$?
3. What does a secant line connect on a curve?
4. What does a tangent line touch on a curve?
5. If the slope of a loss curve is positive, should we increase or decrease the weight to lower loss?

## Level 2 — Calculation
1. Compute average rate of change for $f(x) = 2x^2 + 1$ between $x=2$ and $x=2.1$.
2. Shrink the interval for $f(x) = 2x^2 + 1$ between $x=2$ and $x=2.001$. What value is the slope approaching?
3. Compute average slope of linear function $f(x) = -4x + 7$ between $x=10$ and $x=20$.
4. If $L(w) = (w-4)^2$, evaluate $L(w)$ at $w=2$ and $w=4$. Is error decreasing?
5. What is the slope of a horizontal line $y = 5$?

## Level 3 — Conceptual
1. Explain intuitively how taking the limit as interval $\Delta x \to 0$ turns a secant line into a tangent line.
2. Why is average rate of change insufficient for gradient descent optimization?
3. What does a derivative of 0 ($\ me=0$) signify on a smooth loss function curve?
4. Explain the difference between local minimum and global minimum on a non-convex loss surface.
5. Why do continuous activation functions (like Sigmoid or GELU) require calculus derivatives, whereas step functions fail?

## Level 4 — AI/ML Application
1. A model's loss function is $L(w) = w^2 - 6w + 9$. Compute loss for $w = 0, 1, 2, 3, 4, 5$. Identify the minimum point.
2. Estimate the instantaneous slope of $L(w) = w^2 - 6w + 9$ at $w=5$ using $\frac{L(5.001) - L(5)}{0.001}$. Is it positive or negative?
3. Explain how autonomous vehicle self-driving controllers use calculus derivatives to compute steering acceleration.

## Level 5 — Interview Questions
1. Derive the formal limit definition of derivative $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$ for $f(x) = x^2$.
2. Why does the step function (Heaviside function) have derivative 0 everywhere except at $x=0$ where it is undefined? Why did this cause Perceptron training to fail?
3. Explain how smooth approximations (Sigmoid, Softplus) solved the zero-gradient problem in early neural networks.
4. What is Non-smooth Optimization and subgradients for functions like $|x|$ or $\text{ReLU}(x)$?
5. Explain the relationship between the Fundamental Theorem of Calculus and AUC-ROC curve evaluation in machine learning.
