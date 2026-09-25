# Solutions — Introduction to Calculus

## Level 1 — Basic Understanding Solutions
### Question 1
1. Differential calculus measures rates of change (slopes/derivatives). Integral calculus measures accumulated areas under curves.
### Question 2
2. $f(1) = 1, f(4) = 16 \implies \text{Slope} = \frac{16-1}{4-1} = \frac{15}{3} = 5$.
### Question 3
3. A secant line connects two distinct points on a curve.
### Question 4
4. A tangent line touches a curve at exactly one local point, matching the curve's instantaneous slope.
### Question 5
5. Decrease the weight! (Since positive slope means increasing weight increases loss).

## Level 2 — Calculation Solutions
### Question 1
1. $f(2) = 9, f(2.1) = 2(4.41)+1 = 9.82 \implies \text{Slope} = \frac{9.82 - 9}{0.1} = 8.2$.
### Question 2
2. $f(2.001) = 2(4.004001)+1 = 9.008002 \implies \text{Slope} = \frac{0.008002}{0.001} = 8.002$. Approaching slope $= 8.0$.
### Question 3
3. Linear function has constant slope $= -4$ everywhere.
### Question 4
4. $L(2) = (2-4)^2 = 4$. $L(4) = (4-4)^2 = 0$. Yes, error decreases from 4 to 0!
### Question 5
5. Zero ($0.0$).

## Level 3 — Conceptual Solutions
### Question 1
1. As the two points on the secant line move infinitely close together ($h \to 0$), the secant line rotates until it touches the curve at a single point, becoming the tangent line.
### Question 2
2. Average rate of change over an interval ignores local curvature and can misguide weight updates if the interval is too large.
### Question 3
3. A derivative of 0 means a flat stationary point: a local minimum, local maximum, or saddle point.
### Question 4
4. A local minimum is the lowest point in a nearby region. A global minimum is the absolute lowest point across the entire domain.
### Question 5
5. Step functions have zero slope almost everywhere, providing zero gradient signal to update weights. Continuous functions provide non-zero gradients everywhere.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $L(0)=9, L(1)=4, L(2)=1, L(3)=0, L(4)=1, L(5)=4$. Minimum point is at $w=3$ where $L(3)=0$.
### Question 2
2. $L(5) = 4$. $L(5.001) = (2.001)^2 = 4.004001$. Slope $\approx \frac{0.004001}{0.001} = 4.001 > 0$. Positive slope!
### Question 3
3. Steering acceleration is the second derivative of position $a(t) = s''(t)$. Calculus computes smooth trajectory adjustments to prevent sudden jerks.

## Level 5 — Interview Questions Solutions
### Question 1
1. $f'(x) = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h} = \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = \lim_{h \to 0} (2x + h) = 2x$.
### Question 2
2. Step function derivative is 0 for all $x \neq 0$. Perceptron gradient update $\nabla w = 0$ almost everywhere, leaving weights stuck without learning signals.
### Question 3
3. Sigmoid $\sigma(x) = \frac{1}{1+e^{-x}}$ has continuous non-zero derivative $\sigma'(x) = \sigma(x)(1-\sigma(x))$, supplying smooth non-zero gradient updates during backpropagation.
### Question 4
4. Subgradients extend derivatives to non-differentiable sharp points (kinks like $|x|$ at $x=0$). Any line staying below the function is a valid subgradient (e.g. any value in $[-1, 1]$ for $|x|$ at $x=0$).
### Question 5
5. Area Under the Receiver Operating Characteristic curve (AUC-ROC) evaluates model classification performance by integrating true positive rate over false positive rate thresholds using definite integrals.
