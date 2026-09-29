# Worked Examples — Joint Probability Distributions

## Example 1: Discrete Joint PMF Table
**Problem**: Given 2D discrete joint PMF table $p(x,y)$:
- $p(0,0)=0.1, p(0,1)=0.2$
- $p(1,0)=0.3, p(1,1)=0.4$
Compute $P(X + Y \ge 1)$.
**Solution**:
1. Pairs satisfying $x + y \ge 1$: $(0,1), (1,0), (1,1)$.
2. $P(X + Y \ge 1) = p(0,1) + p(1,0) + p(1,1) = 0.2 + 0.3 + 0.4 = 0.90$.

## Example 2: Normalization Constant $c$
**Problem**: Find constant $c$ for joint PDF $f(x, y) = c x y$ on $0 \le x \le 2, 0 \le y \le 2$.
**Solution**:
1. $\int_0^2 \int_0^2 c x y dx dy = 1$.
2. $c \left( \int_0^2 x dx 
ight) \left( \int_0^2 y dy 
ight) = c \left[ \frac{x^2}{2} 
ight]_0^2 \left[ \frac{y^2}{2} 
ight]_0^2 = c (2) (2) = 4c = 1 \implies c = 0.25$.

## Example 3: Continuous Triangular Region Integration
**Problem**: Let $f(x, y) = 6 x$ for $0 \le x \le y \le 1$. Verify $\int \int f(x, y) dx dy = 1$.
**Solution**:
1. Integration limits: $x$ goes from $0$ to $y$; $y$ goes from $0$ to $1$.
2. $\int_0^1 \int_0^y 6 x dx dy = \int_0^1 \left[ 3 x^2 
ight]_0^y dy = \int_0^1 3 y^2 dy = \left[ y^3 
ight]_0^1 = 1.0$.

## Example 4: Bivariate Normal PDF Peak Height
**Problem**: A 2D uncorrelated Gaussian has $oldsymbol{\mu} = [0, 0]^T$ and $oldsymbol{\Sigma} = 	ext{diag}(1, 4)$. Compute peak height $f(0, 0)$.
**Solution**:
1. $|oldsymbol{\Sigma}| = 1 	imes 4 = 4 \implies |oldsymbol{\Sigma}|^{1/2} = 2$.
2. Exponent at $(0,0)$ is zero $\implies e^0 = 1$.
3. $f(0, 0) = \frac{1}{2\pi (2)} = \frac{1}{4\pi} pprox 0.0796$.

## Example 5: Continuous Joint CDF to PDF
**Problem**: Given joint CDF $F(x, y) = (1 - e^{-x})(1 - e^{-y})$ for $x \ge 0, y \ge 0$. Derive joint PDF $f(x, y)$.
**Solution**:
1. $f(x, y) = \frac{\partial^2}{\partial x \partial y} F(x, y)$.
2. $\frac{\partial}{\partial y} F(x, y) = (1 - e^{-x}) e^{-y}$.
3. $\frac{\partial^2}{\partial x \partial y} F(x, y) = e^{-x} e^{-y}$.
4. $f(x, y) = e^{-(x+y)}$ for $x \ge 0, y \ge 0$.
