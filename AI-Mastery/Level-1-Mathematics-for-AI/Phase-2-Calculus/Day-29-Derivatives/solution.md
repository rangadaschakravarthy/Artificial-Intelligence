# Solutions — Derivatives

## Level 1 — Basic Understanding Solutions
### Question 1
1. $5 x^4$.
### Question 2
2. $e^x$.
### Question 3
3. $\frac{1}{x}$.
### Question 4
4. 0 (Derivative of any constant is zero).
### Question 5
5. $f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$.

## Level 2 — Calculation Solutions
### Question 1
1. $12 x^3 - 4x + 5$.
### Question 2
2. $f'(x) = 3x^2 - 3 \implies f'(2) = 3(4) - 3 = 9$.
### Question 3
3. $\frac{d}{dx}[x^{-1}] = -1 x^{-2} = -\frac{1}{x^2}$.
### Question 4
4. $\frac{d}{dx}[x^{1/2}] = \frac{1}{2} x^{-1/2} = \frac{1}{2\sqrt{x}}$.
### Question 5
5. True $f'(2) = 12$. Forward diff: $\frac{2.01^3 - 8}{0.01} = 12.0601$ (error 0.0601). Central diff: $\frac{2.01^3 - 1.99^3}{0.02} = 12.0001$ (error 0.0001). Central diff is 600x more accurate!

## Level 3 — Conceptual Solutions
### Question 1
1. $f'(x) = \lim_{h \to 0} \frac{c - c}{h} = \lim_{h \to 0} \frac{0}{h} = 0$.
### Question 2
2. Left derivative as $h \to 0^-$ is $-1$, right derivative as $h \to 0^+$ is $+1$. Since left and right derivatives do not match, derivative does not exist at 0.
### Question 3
3. $e^x$ is the unique function (up to scaling) equal to its own derivative, serving as the eigenfunction of differentiation operator $\frac{d}{dx}$.
### Question 4
4. Second derivative $f''(x)$ measures rate of change of slope (curvature/concavity). Positive $f''(x) > 0$ means concave up (bowl shape), negative $f''(x) < 0$ means concave down.
### Question 5
5. $f''(x) > 0$ means slope is increasing, forming a bowl shape where tangent line lies below function graph (convex).

## Level 4 — AI/ML Application Solutions
### Question 1
1. $L'(w) = 2(w - 3)$. Setting $L'(w) = 0 \implies 2w - 6 = 0 \implies w = 3$ (minimum of loss!).
### Question 2
2. $w_{new} = 5 - 0.1(4) = 5 - 0.4 = 4.6$. Moves closer to minimum $w=3$!
### Question 3
3. Autograd tracks operations during forward pass, storing primitive node derivatives in a Directed Acyclic Graph (DAG), then applies chain rule backward.

## Level 5 — Interview Questions Solutions
### Question 1
1. $e^y = x \implies \frac{d}{dx}[e^y] = \frac{d}{dx}[x] \implies e^y \frac{dy}{dx} = 1 \implies \frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}$.
### Question 2
2. $(x+h)^n = x^n + n x^{n-1} h + \frac{n(n-1)}{2} x^{n-2} h^2 + \dots$. Subtract $x^n$ and divide by $h$: $\frac{f(x+h)-f(x)}{h} = n x^{n-1} + O(h)$. Limit $h \to 0$ gives $n x^{n-1}$.
### Question 3
3. Taylor expansion $f(x+h) = f(x) + f'(x)h + \frac{f''(x)}{2}h^2 + \dots$. Truncating after 1st derivative yields linear approximation $f(x+h) \approx f(x) + f'(x)h$.
### Question 4
4. Taylor expansion with imaginary step $i h$: $f(x + i h) = f(x) + i h f'(x) - \frac{h^2}{2} f''(x) + O(h^3)$. Taking imaginary part: $\text{Im}(f(x+ih)) = h f'(x) \implies f'(x) = \frac{\text{Im}(f(x+ih))}{h}$. No subtraction involved, eliminating floating-point cancellation error completely!
### Question 5
5. Newton's optimization method uses 2nd derivative: $w_{new} = w_{old} - \frac{f'(w_{old})}{f''(w_{old})}$, taking exact steps to minimum for quadratic loss functions in 1 step.
