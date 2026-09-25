# Solutions — Functions

## Level 1 — Basic Understanding Solutions
### Question 1
1. Domain: all real numbers $\mathbb{R}$. Range: non-negative real numbers $[0, \infty)$.
### Question 2
2. $\sigma(0) = \frac{1}{1+e^0} = \frac{1}{1+1} = 0.5$.
### Question 3
3. For $x=-5$: $\text{ReLU}(-5) = \max(0, -5) = 0$. For $x=3$: $\text{ReLU}(3) = \max(0, 3) = 3$.
### Question 4
4. $g(4) = 4+2 = 6$. $f(6) = 3(6) = 18$.
### Question 5
5. Division by zero is mathematically undefined.

## Level 2 — Calculation Solutions
### Question 1
1. $x - 4 \ge 0 \implies x \ge 4$. Domain: $[4, \infty)$.
### Question 2
2. Logarithm requires strictly positive inputs. Domain: $(0, \infty)$.
### Question 3
3. $(f \circ g)(x) = \frac{1}{1 + e^{-x^2}}$.
### Question 4
4. $e^1 \approx 2.718, e^2 \approx 7.389$. Sum $= 10.107$. $S_1 = 2.718/10.107 \approx 0.269, S_2 = 7.389/10.107 \approx 0.731$. Sum $= 1.0$.
### Question 5
5. Non-linear (it is piecewise linear with a bend/kink at $x=0$).

## Level 3 — Conceptual Solutions
### Question 1
1. $(f \circ g)(x) = f(c x + d) = a(c x + d) + b = (ac) x + (ad + b)$. This is of form $A x + B$, which is strictly linear.
### Question 2
2. Universal Approximation Theorem states that a feedforward neural network with a single hidden layer containing a finite number of non-linear neurons can approximate any continuous function on compact subsets of $\mathbb{R}^n$.
### Question 3
3. $\ln(p)$ penalizes confident wrong predictions severely (as $p \to 0$, $\ln(p) \to -\infty$), providing large gradient signals to correct model weights quickly.
### Question 4
4. For $|x| > 5$, Sigmoid flattens out with near-zero derivative $\sigma'(x) \approx 0$. During backpropagation, multiplying by near-zero gradients causes weight updates to freeze (vanishing gradient).
### Question 5
5. ReLU is $f(x) = \max(0, x)$ with sharp kink at 0. GELU is smooth $x \Phi(x)$ (where $\Phi$ is Gaussian CDF), allowing small negative gradients.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\sigma(-5) \approx 0.0067, \sigma(-2) \approx 0.1192, \sigma(0) = 0.5, \sigma(2) \approx 0.8808, \sigma(5) \approx 0.9933$. Notice $\sigma(-2) = 0.1192 = 1 - 0.8808 = 1 - \sigma(2)$.
### Question 2
2. $p = \frac{1}{1 + e^{-2.197}} = \frac{1}{1 + 1/9} = \frac{1}{10/9} = \frac{9}{10} = 0.90$ (90% confidence!).
### Question 3
3. Softmax exponentiates logits $e^{z_i} > 0$ to force positive values, then divides each by total sum $\sum e^{z_j}$, producing a normalized output vector summing to 1.0.

## Level 5 — Interview Questions Solutions
### Question 1
1. Proof: $1 - \sigma(x) = 1 - \frac{1}{1+e^{-x}} = \frac{1+e^{-x} - 1}{1+e^{-x}} = \frac{e^{-x}}{1+e^{-x}} = \frac{1}{e^x(1+e^{-x})} = \frac{1}{e^x+1} = \sigma(-x)$.
### Question 2
2. Let $p = \frac{1}{1+e^{-x}} \implies p(1+e^{-x}) = 1 \implies p + p e^{-x} = 1 \implies p e^{-x} = 1-p \implies e^{-x} = \frac{1-p}{p} \implies e^x = \frac{p}{1-p} \implies x = \ln\left(\frac{p}{1-p}\right)$.
### Question 3
3. Swish $f(x) = x \cdot \sigma(\beta x)$ is smooth, non-monotonic, self-gated activation function that outperforms ReLU on deep Vision Transformers and ResNets.
### Question 4
4. Function $f$ is $L$-Lipschitz continuous if $|f(x) - f(y)| \le L ||x - y||_2$. Small $L$ guarantees model outputs cannot explode when inputs are slightly perturbed (adversarial robustness).
### Question 5
5. A function is convex if line segment between any two points on graph lies above or on graph. For convex functions, any local minimum $\nabla f(x^*) = 0$ is guaranteed to be a global minimum.
