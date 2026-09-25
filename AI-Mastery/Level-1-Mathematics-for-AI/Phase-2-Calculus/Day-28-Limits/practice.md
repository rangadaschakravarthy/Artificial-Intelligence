# Practice Exercises — Limits

## Level 1 — Basic Understanding
1. Evaluate $\lim_{x \to 5} (3x - 4)$.
2. Evaluate $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$.
3. What is an indeterminate form in calculus?
4. State L'Hôpital's Rule formula.
5. What is $\lim_{x \to \infty} \frac{1}{x^2}$?

## Level 2 — Calculation
1. Evaluate $\lim_{x \to 0} \frac{\sin(x)}{x}$ using L'Hôpital's Rule.
2. Evaluate $\lim_{x \to 0} \frac{e^x - 1}{x}$ using L'Hôpital's Rule.
3. Evaluate $\lim_{x \to \infty} \frac{3x^2 + 5}{2x^2 - 1}$.
4. Is $f(x) = \begin{cases} x^2 & x \neq 2 \\ 5 & x = 2 \end{cases}$ continuous at $x = 2$? Why or why not?
5. Why does $\lim_{x \to 0} \ln(x)$ fail to exist for real numbers?

## Level 3 — Conceptual
1. Prove that $\lim_{x \to 0} x \ln(x) = 0$ using L'Hôpital's Rule by rewriting as $\frac{\ln(x)}{1/x}$.
2. Explain why left-hand limit $\lim_{x \to 0^-} f(x)$ must equal right-hand limit $\lim_{x \to 0^+} f(x)$ for a 2-sided limit to exist.
3. Analyze continuity of ReLU function $f(x) = \max(0, x)$ at $x = 0$. Is it continuous? Is it differentiable at $x = 0$?
4. Explain why vanishing gradients occur in deep networks when derivative limits approach zero: $\lim_{L \to \infty} \prod_{l=1}^L w_l = 0$.
5. What is the limit of Sigmoid function $\sigma(x)$ as $x \to \infty$ and $x \to -\infty$?

## Level 4 — AI/ML Application
1. In Log-Loss $L = -y \ln(p) - (1-y)\ln(1-p)$, evaluate loss as predicted probability $p \to 0$ when true label $y = 1$. What numerical exception occurs in Python without clipping?
2. Demonstrate how Log-Sum-Exp identity $\ln \sum_{i=1}^K e^{z_i} = m + \ln \sum_{i=1}^K e^{z_i - m}$ where $m = \max(z)$ prevents numerical overflow.
3. Explain how Automatic Differentiation frameworks handle non-differentiable points (like $x=0$ in ReLU) using subgradients.

## Level 5 — Interview Questions
1. Prove using $\epsilon-\delta$ definition that $\lim_{x \to 3} (2x + 1) = 7$.
2. Evaluate $\lim_{x \to 0} (1 + x)^{1/x}$ and show it equals Euler's constant $e$.
3. Explain Taylor Series Expansion $f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x-a)^n$ as a limit of polynomial approximations.
4. What is the Big-O asymptotic notation definition in terms of upper bound limits?
5. Explain how Stochastic Gradient Descent convergence proofs rely on Robbins-Monro conditions $\sum \eta_t = \infty$ and $\sum \eta_t^2 < \infty$.
