# Solutions — Derivative Rules

## Level 1 — Basic Understanding Solutions
### Question 1
1. $(u v)' = u' v + u v'$.
### Question 2
2. $\left(\frac{u}{v}\right)' = \frac{u' v - u v'}{v^2}$.
### Question 3
3. $12 x^2 + 4x - 7$.
### Question 4
4. $5 e^x$.
### Question 5
5. $\sigma'(x) = \sigma(x)(1 - \sigma(x))$.

## Level 2 — Calculation Solutions
### Question 1
1. $u=x^3 \implies u'=3x^2; v=e^x \implies v'=e^x$. $f'(x) = 3x^2 e^x + x^3 e^x = x^2 e^x (3 + x)$.
### Question 2
2. $u=x^2 \implies u'=2x; v=\ln x \implies v'=1/x$. $f'(x) = 2x \ln x + x^2(1/x) = 2x \ln x + x = x(2\ln x + 1)$.
### Question 3
3. $u=e^x \implies u'=e^x; v=x \implies v'=1$. $f'(x) = \frac{e^x x - e^x(1)}{x^2} = \frac{e^x(x - 1)}{x^2}$.
### Question 4
4. $\sigma'(2) = \sigma(2)(1 - \sigma(2)) \approx 0.8808(1 - 0.8808) = 0.8808(0.1192) \approx 0.1050$.
### Question 5
5. $u=x^2+1 \implies u'=2x; v=x-1 \implies v'=1$. $f'(x) = \frac{2x(x-1) - (x^2+1)(1)}{(x-1)^2} = \frac{2x^2 - 2x - x^2 - 1}{(x-1)^2} = \frac{x^2 - 2x - 1}{(x-1)^2}$.

## Level 3 — Conceptual Solutions
### Question 1
1. $\sigma(x) = (1+e^{-x})^{-1}$. Chain/Power Rule: $\sigma'(x) = -1(1+e^{-x})^{-2} (-e^{-x}) = \frac{e^{-x}}{(1+e^{-x})^2} = \frac{1}{1+e^{-x}} \frac{e^{-x}}{1+e^{-x}} = \sigma(x)(1-\sigma(x))$.
### Question 2
2. $f(x) = \ln(1+e^x)$. Chain rule: $f'(x) = \frac{1}{1+e^x} \frac{d}{dx}(1+e^x) = \frac{e^x}{1+e^x} = \frac{1}{e^{-x}(1+e^x)} = \frac{1}{e^{-x}+1} = \sigma(x)$. Softplus derivative is Sigmoid!
### Question 3
3. $u=x \implies u'=1; v=\sigma(x) \implies v'=\sigma(x)(1-\sigma(x))$. $f'(x) = 1 \cdot \sigma(x) + x \sigma(x)(1-\sigma(x)) = \sigma(x) + x \sigma(x)(1-\sigma(x))$.
### Question 4
4. $\sigma'(x) = \sigma(1-\sigma)$. Let $p = \sigma \in (0, 1)$. Function $g(p) = p(1-p) = p - p^2$. Derivative $g'(p) = 1 - 2p = 0 \implies p = 0.5$. At $p=0.5$ ($x=0$), max value is $0.5(1-0.5) = 0.25$.
### Question 5
5. $f(x) = \frac{1-e^{-x}}{1+e^{-x}}$. Derivative $f'(x) = \frac{e^{-x}(1+e^{-x}) - (1-e^{-x})(-e^{-x})}{(1+e^{-x})^2} = \frac{2e^{-x}}{(1+e^{-x})^2}$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Let $\hat{y} = \sigma(w x)$. $\frac{dL}{dw} = -y \frac{1}{\hat{y}} \hat{y}(1-\hat{y})x - (1-y)\frac{1}{1-\hat{y}} (-\hat{y}(1-\hat{y})x) = -y(1-\hat{y})x + (1-y)\hat{y}x = (-y + y\hat{y} + \hat{y} - y\hat{y})x = (\hat{y} - y)x$. Clean gradient!
### Question 2
2. Autograd breaks complex expressions into primitive nodes ($+, *, \exp, \ln$). Each primitive node registers its derivative rule. Backward pass traverses nodes applying stored derivative rules via chain rule.
### Question 3
3. Let $u = -x^2/2 \implies u' = -x$. Chain rule: $\frac{d}{dx}[e^{-x^2/2}] = e^{-x^2/2} (-x) = -x e^{-x^2/2}$.

## Level 5 — Interview Questions Solutions
### Question 1
1. $\text{tanh}(x) = \frac{\sinh(x)}{\cosh(x)}$. Quotient Rule: $\text{tanh}'(x) = \frac{\cosh(x)\cosh(x) - \sinh(x)\sinh(x)}{\cosh^2(x)} = \frac{\cosh^2(x) - \sinh^2(x)}{\cosh^2(x)} = \frac{1}{\cosh^2(x)} = 1 - \text{tanh}^2(x)$.
### Question 2
2. Group $(uv)w$. Product Rule: $((uv)w)' = (uv)' w + (uv) w' = (u'v + uv')w + uv w' = u'vw + uv'w + uvw'$.
### Question 3
3. Write $\frac{u}{v} = u \cdot v^{-1}$. Product rule: $(u v^{-1})' = u' v^{-1} + u (-1 v^{-2} v') = \frac{u'}{v} - \frac{u v'}{v^2} = \frac{u' v - u v'}{v^2}$. Q.E.D.
### Question 4
4. Case $i=j$: Quotient rule on $\frac{e^{z_i}}{S_{sum}} \implies \frac{e^{z_i} S_{sum} - e^{z_i} e^{z_i}}{S_{sum}^2} = S_i - S_i^2 = S_i(1 - S_i)$. Case $i \neq j$: $\frac{0 - e^{z_i} e^{z_j}}{S_{sum}^2} = -S_i S_j$. Combined: $\frac{\partial S_i}{\partial z_j} = S_i (\delta_{i,j} - S_j)$.
### Question 5
5. Dual numbers represent numbers as $a + b\epsilon$ with $\epsilon^2 = 0$. Evaluating $f(a + b\epsilon) = f(a) + f'(a)b\epsilon$ propagates exact derivative in imaginary component $b\epsilon$ without symbolic expansion.
