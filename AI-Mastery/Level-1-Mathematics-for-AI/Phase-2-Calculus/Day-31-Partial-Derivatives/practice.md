# Practice Exercises — Partial Derivatives

## Level 1 — Basic Understanding
1. What is a partial derivative?
2. Given $f(x, y) = 4x^3 y^2$, find $\frac{\partial f}{\partial x}$.
3. Given $f(x, y) = 4x^3 y^2$, find $\frac{\partial f}{\partial y}$.
4. What is Clairaut's Theorem on mixed partial derivatives?
5. How do you treat variable $y$ when computing $\frac{\partial f}{\partial x}$?

## Level 2 — Calculation
1. Compute $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ for $f(x, y) = x^2 y + \sin(x) + e^y$.
2. Evaluate $\frac{\partial f}{\partial x}$ at point $(1, 3)$ for $f(x, y) = 5x^2 y - 2x y^3$.
3. Compute second partial derivatives $f_{xx}$ and $f_{yy}$ for $f(x, y) = x^3 y^4$.
4. Verify $f_{xy} = f_{yx}$ for $f(x, y) = x^3 y^4$.
5. Given loss function $L(w_1, w_2) = w_1^2 + 3w_2^2 - 4w_1 w_2$, compute $\frac{\partial L}{\partial w_1}$ and $\frac{\partial L}{\partial w_2}$.

## Level 3 — Conceptual
1. Calculate all first and second-order partial derivatives for $f(x, y) = e^{x y}$.
2. Explain why total differential $df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy$ predicts function changes across all variables.
3. Find critical points where $\frac{\partial f}{\partial x} = 0$ and $\frac{\partial f}{\partial y} = 0$ for $f(x, y) = x^2 + y^2 - 4x - 6y + 13$.
4. Why is computing partial derivatives essential for backpropagation in deep neural networks?
5. What is a Directional Derivative $D_{\mathbf{u}} f(\mathbf{x})$ and how does it extend partial derivatives along an arbitrary unit vector $\mathbf{u}$?

## Level 4 — AI/ML Application
1. For a 2-parameter linear regression MSE loss $L(w, b) = \frac{1}{N} \sum_{i=1}^N (w x_i + b - y_i)^2$, derive partial derivatives $\frac{\partial L}{\partial w}$ and $\frac{\partial L}{\partial b}$.
2. Set $\frac{\partial L}{\partial w} = 0$ and $\frac{\partial L}{\partial b} = 0$ to derive the 2D linear regression normal system of equations.
3. Explain how PyTorch computes partial derivatives for millions of parameters independently during `loss.backward()`.

## Level 5 — Interview Questions
1. Prove Clairaut's Theorem $f_{xy} = f_{yx}$ using double limits definition under hypothesis of continuous 2nd derivatives.
2. Explain the Hessian Matrix $H_{i,j} = \frac{\partial^2 f}{\partial x_i \partial x_j}$ of all second-order partial derivatives.
3. How does the Second Partial Derivative Test ($D = f_{xx} f_{yy} - (f_{xy})^2$) classify critical points as local minima, local maxima, or saddle points?
4. Explain Partial Differential Equations (PDEs) in Physics-Informed Neural Networks (PINNs) like Navier-Stokes or Schrödinger equations.
5. What is a Subgradient for multi-variable non-differentiable loss functions like $L(w_1, w_2) = |w_1| + |w_2|$?
