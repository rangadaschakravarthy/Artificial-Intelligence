# Worked Examples — Independence

## Example 1: Verifying Discrete Independence
**Problem**: Joint PMF $p(x,y)$ for $x \in \{0,1\}, y \in \{0,1\}$: $p(0,0)=0.1, p(0,1)=0.3, p(1,0)=0.2, p(1,1)=0.4$. Are $X$ and $Y$ independent?
**Solution**:
1. Marginals: $p_X(0) = 0.1+0.3=0.4, p_X(1) = 0.2+0.4=0.6$.
2. Marginals: $p_Y(0) = 0.1+0.2=0.3, p_Y(1) = 0.3+0.4=0.7$.
3. Check $p(0,0)$: $p_X(0)p_Y(0) = 0.4 	imes 0.3 = 0.12 
eq 0.10$.
4. Since $0.10 
eq 0.12$, $X$ and $Y$ are NOT independent.

## Example 2: Continuous PDF Factorization
**Problem**: Joint PDF $f(x, y) = 4 x y$ for $0 \le x \le 1, 0 \le y \le 1$. Determine if $X$ and $Y$ are independent.
**Solution**:
1. $f_X(x) = \int_0^1 4 x y dy = 4x \left[ rac{y^2}{2} ight]_0^1 = 2x$.
2. $f_Y(y) = \int_0^1 4 x y dx = 4y \left[ rac{x^2}{2} ight]_0^1 = 2y$.
3. Check product: $f_X(x) f_Y(y) = (2x)(2y) = 4 x y = f(x, y)$.
4. Yes! $X$ and $Y$ are independent continuous random variables.

## Example 3: Expectation Product Rule
**Problem**: Independent $X, Y$ have $E[X] = 5$ and $E[Y] = 8$. Compute $E[3 X Y + 4]$.
**Solution**:
1. $E[3 X Y + 4] = 3 E[X Y] + 4$.
2. Since $X \perp \!\!\! \perp Y$, $E[X Y] = E[X] E[Y] = 5 	imes 8 = 40$.
3. Result $= 3(40) + 4 = 120 + 4 = 124$.

## Example 4: Variance of Independent Sum
**Problem**: $X_1, X_2, X_3$ are i.i.d. with variance $\sigma^2 = 4$. Compute $	ext{Var}(2 X_1 - X_2 + 3 X_3)$.
**Solution**:
1. Because variables are independent, cross-covariance terms vanish.
2. $	ext{Var}(2 X_1 - X_2 + 3 X_3) = 2^2 	ext{Var}(X_1) + (-1)^2 	ext{Var}(X_2) + 3^2 	ext{Var}(X_3)$.
3. $= 4(4) + 1(4) + 9(4) = 16 + 4 + 36 = 56$.

## Example 5: Log-Likelihood Factorization under i.i.d.
**Problem**: Given 3 independent Bernoulli observations $x_1=1, x_2=1, x_3=0$ with probability $p$. Write log-likelihood $\ln L(p)$.
**Solution**:
1. $L(p) = P(x_1) P(x_2) P(x_3) = p \cdot p \cdot (1-p) = p^2 (1-p)$.
2. $\ln L(p) = 2 \ln(p) + \ln(1-p)$.
