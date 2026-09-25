# Practice Exercises — Derivatives

## Level 1 — Basic Understanding
1. What is the derivative of $f(x) = x^5$?
2. What is the derivative of $f(x) = e^x$?
3. What is the derivative of $f(x) = \ln(x)$?
4. What is the derivative of a constant $f(x) = 7$?
5. State the central difference formula for numerical differentiation.

## Level 2 — Calculation
1. Calculate the derivative of $f(x) = 3x^4 - 2x^2 + 5x - 9$.
2. Evaluate the slope of $f(x) = x^3 - 3x$ at $x = 2$.
3. Compute derivative of $f(x) = \frac{1}{x} = x^{-1}$.
4. Compute derivative of $f(x) = \sqrt{x} = x^{1/2}$.
5. Compare numerical error of forward difference vs central difference for $f(x) = x^3$ at $x=2$ with $h=0.01$.

## Level 3 — Conceptual
1. Prove that the derivative of a constant function $f(x) = c$ is 0 using limit definition.
2. Why is the absolute value function $f(x) = |x|$ not differentiable at $x = 0$?
3. Explain why $\frac{d}{dx}[e^x] = e^x$ makes Euler's number $e$ special in calculus and differential equations.
4. What is the Second Derivative $f''(x)$ and what does it measure geometrically (concavity)?
5. Show that if $f''(x) > 0$, the function is convex (concave up) at $x$.

## Level 4 — AI/ML Application
1. Loss function for a single weight is $L(w) = (w - 3)^2$. Compute derivative $L'(w)$. Find $w$ where $L'(w) = 0$.
2. If $L'(w) = 4$ at $w = 5$, and learning rate $\eta = 0.1$, compute gradient descent update $w_{new} = w_{old} - \eta L'(w_{old})$.
3. Explain how Automatic Differentiation (Autograd) in PyTorch constructs a computational graph of elementary derivatives.

## Level 5 — Interview Questions
1. Derive $\frac{d}{dx}[\ln(x)] = \frac{1}{x}$ using implicit differentiation of $y = \ln(x) \implies e^y = x$.
2. Prove Power Rule $\frac{d}{dx}[x^n] = n x^{n-1}$ for positive integer $n$ using Binomial Theorem.
3. Explain Taylor Series first-order linear approximation $f(x+h) \approx f(x) + f'(x)h$.
4. What is the Complex Step Derivative method $f'(x) \approx \frac{\text{Im}(f(x + i h))}{h}$ and why avoids floating-point subtractive cancellation error?
5. Explain how Higher-Order Derivatives (Hessian matrix of second partial derivatives) are used in Newton's Optimization Method.
