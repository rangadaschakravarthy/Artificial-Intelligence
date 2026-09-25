# Solutions — Limits

## Level 1 — Basic Understanding Solutions
### Question 1
1. $3(5) - 4 = 15 - 4 = 11$.
### Question 2
2. $\frac{(x-2)(x+2)}{x-2} \implies \lim_{x \to 2} (x+2) = 4$.
### Question 3
3. An expression whose value cannot be determined directly by substitution, such as $0/0$ or $\infty/\infty$.
### Question 4
4. $\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}$ when form is $0/0$ or $\infty/\infty$.
### Question 5
5. $0.0$.

## Level 2 — Calculation Solutions
### Question 1
1. $\lim_{x \to 0} \frac{\cos(x)}{1} = \frac{\cos(0)}{1} = \frac{1}{1} = 1$.
### Question 2
2. Form $0/0$. Differentiate top/bottom: $\lim_{x \to 0} \frac{e^x}{1} = \frac{1}{1} = 1$.
### Question 3
3. Divide top and bottom by $x^2$: $\lim_{x \to \infty} \frac{3 + 5/x^2}{2 - 1/x^2} = \frac{3 + 0}{2 - 0} = \frac{3}{2} = 1.5$.
### Question 4
4. No! $\lim_{x \to 2} f(x) = 4$, but $f(2) = 5$. Since $\lim_{x \to 2} f(x) \neq f(2)$, it is discontinuous at $x = 2$.
### Question 5
5. Because $\ln(x)$ is only defined for positive numbers $x > 0$. As $x \to 0^+$, $\ln(x) \to -\infty$.

## Level 3 — Conceptual Solutions
### Question 1
1. Form $\infty/\infty$. Apply L'Hôpital: $\lim_{x \to 0^+} \frac{\ln(x)}{1/x} = \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$.
### Question 2
2. If left and right paths approach different values, there is a jump/break in the graph, so no single limit $L$ exists.
### Question 3
3. $\lim_{x \to 0^-} \text{ReLU}(x) = 0$, $\lim_{x \to 0^+} \text{ReLU}(x) = 0$. Since $\lim = f(0) = 0$, it is CONTINUOUS. However, left derivative is 0 and right derivative is 1, so it is NOT differentiable at $x = 0$.
### Question 4
4. In a deep network, chain rule multiplies derivatives across layers. If weights $w_l < 1$, product $\prod_{l=1}^L w_l \to 0$ as $L \to \infty$, causing gradients to vanish.
### Question 5
5. As $x \to \infty$, $\sigma(x) \to 1$. As $x \to -\infty$, $\sigma(x) \to 0$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. As $p \to 0$, $-\ln(p) \to +\infty$. Python throws `ZeroDivisionError` or returns `-inf`, crashing loss computation. Fix: `p = np.clip(p, 1e-7, 1 - 1e-7)`.
### Question 2
2. Subtracting $m = \max(z)$ ensures exponents $z_i - m \le 0$, so $e^{z_i - m} \le 1$. Exponents never exceed 1, preventing floating-point overflow (`Inf`).
### Question 3
3. Frameworks define default subgradient conventions at sharp kinks (e.g. setting $\text{ReLU}'(0) = 0$), allowing automatic differentiation to proceed smoothly.

## Level 5 — Interview Questions Solutions
### Question 1
1. Want $|(2x+1) - 7| < \epsilon \implies |2x - 6| < \epsilon \implies 2|x - 3| < \epsilon \implies |x - 3| < \frac{\epsilon}{2}$. Choose $\delta = \frac{\epsilon}{2}$. Q.E.D.
### Question 2
2. Let $y = (1+x)^{1/x} \implies \ln(y) = \frac{\ln(1+x)}{x}$. Limit as $x \to 0$ is $0/0$. L'Hôpital: $\lim_{x \to 0} \frac{1/(1+x)}{1} = 1$. Since $\ln(y) = 1 \implies y = e^1 = e$.
### Question 3
3. Taylor series represents function $f(x)$ as the limit of an infinite polynomial sum of $n$-th order derivatives at point $a$, matching local curvature.
### Question 4
4. $f(x) = O(g(x))$ means there exist positive constants $C$ and $x_0$ such that $|f(x)| \le C |g(x)|$ for all $x \ge x_0$ (formal limit upper bound).
### Question 5
5. Robbins-Monro conditions guarantee SGD convergence: $\sum \eta_t = \infty$ ensures step sizes are large enough to travel any distance to minimum, while $\sum \eta_t^2 < \infty$ ensures step sizes shrink fast enough to suppress random gradient noise.
