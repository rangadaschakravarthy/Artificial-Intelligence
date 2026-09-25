# Practice Exercises — Gradients

## Level 1 — Basic Understanding
1. What is the gradient vector $\nabla f(\mathbf{x})$?
2. In which direction does the gradient vector $\nabla f$ point?
3. In which direction does the negative gradient vector $-\nabla f$ point?
4. Compute the gradient vector for $f(x, y) = 5x^2 + 2y^3$.
5. What is the gradient vector at a local minimum point?

## Level 2 — Calculation
1. Compute $\nabla f(x, y)$ for $f(x, y) = x^2 y - 3x + 4y^2$. Evaluate at point $(1, 2)$.
2. Find the steepest descent direction vector at $(1, 2)$ for $f(x, y) = x^2 y - 3x + 4y^2$.
3. Compute directional derivative of $f(x, y) = 2x^2 + 3y^2$ at point $(1, 1)$ along direction $\mathbf{u} = [0.6, 0.8]^T$.
4. Find all critical points where $\nabla f(x, y) = \mathbf{0}$ for $f(x, y) = x^2 + y^2 - 6x + 4y + 12$.
5. Given loss $L(w_1, w_2) = w_1^2 + 2w_2^2$, compute gradient $\nabla L(3, 2)$ and perform 1 step of Gradient Descent with $\eta = 0.1$.

## Level 3 — Conceptual
1. Prove that directional derivative $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$ is maximized when unit vector $\mathbf{u}$ points in same direction as $\nabla f$.
2. Prove that gradient vector $\nabla f$ is orthogonal to the tangent plane of level set $f(x, y) = C$.
3. Explain why gradient descent steps oscillate back and forth in narrow steep valleys (Rosennbrock function problem).
4. How does Momentum ($\mathbf{v}_{t+1} = \beta \mathbf{v}_t + \eta \nabla L$) accelerate gradient descent through steep valleys?
5. Compute gradient of matrix quadratic form $f(\mathbf{x}) = \frac{1}{2} \mathbf{x}^T \mathbf{A} \mathbf{x} - \mathbf{b}^T \mathbf{x}$ for symmetric matrix $\mathbf{A}$.

## Level 4 — AI/ML Application
1. For multi-variable MSE loss $L(\mathbf{w}) = \frac{1}{N} ||\mathbf{X}\mathbf{w} - \mathbf{y}||_2^2$, derive gradient vector $\nabla_{\mathbf{w}} L = \frac{2}{N} \mathbf{X}^T (\mathbf{X}\mathbf{w} - \mathbf{y})$.
2. Implement a gradient calculation check in Python comparing analytical gradient $\nabla f_{exact}$ against numerical central difference gradient $\nabla f_{num}$.
3. Explain how Adam optimizer uses first moment (mean gradient) and second moment (uncentered variance gradient) estimates.

## Level 5 — Interview Questions
1. Derive gradient vector of Softmax Cross-Entropy Loss $L = -\sum y_i \ln(S_i)$ with respect to logit vector $\mathbf{z}$, showing $\nabla_{\mathbf{z}} L = \mathbf{S} - \mathbf{y}$.
2. What is Stochastic Gradient Noise and why does mini-batch SGD gradient variance help escape shallow local minima?
3. Explain Natural Gradient Descent and how Fisher Information Matrix $F = E[\nabla \log p \nabla \log p^T]$ defines steepest descent on probability manifolds.
4. Explain Gradient Clipping (by norm and by value) to prevent exploding gradients in Recurrent Neural Networks.
5. What is Gradient Vanishing in Deep Networks and how do residual connections $y = f(x) + x$ enforce $\nabla_{\mathbf{x}} y = \nabla_{\mathbf{x}} f + \mathbf{I}$?
