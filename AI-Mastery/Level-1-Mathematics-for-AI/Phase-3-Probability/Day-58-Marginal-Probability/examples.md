# Worked Examples — Marginal Probability

## Example 1: Discrete Marginalization
**Problem**: Joint PMF $p(1,1)=0.2, p(1,2)=0.3, p(2,1)=0.1, p(2,2)=0.4$. Compute marginal PMF $p_X(x)$.
**Solution**:
1. $p_X(1) = p(1,1) + p(1,2) = 0.2 + 0.3 = 0.5$.
2. $p_X(2) = p(2,1) + p(2,2) = 0.1 + 0.4 = 0.5$.
3. Check sum: $p_X(1) + p_X(2) = 0.5 + 0.5 = 1.0$.

## Example 2: Continuous Marginal PDF Derivation
**Problem**: Joint PDF $f(x, y) = 6 x$ for $0 \le x \le y \le 1$. Derive marginal PDF $f_Y(y)$.
**Solution**:
1. Domain limits: For a fixed $y$, $x$ ranges from $0$ to $y$.
2. $f_Y(y) = \int_0^y 6 x dx = \left[ 3 x^2 ight]_0^y = 3 y^2$ for $0 \le y \le 1$.

## Example 3: Deriving Marginal $f_X(x)$ from Same PDF
**Problem**: For $f(x, y) = 6 x$ on $0 \le x \le y \le 1$, derive marginal PDF $f_X(x)$.
**Solution**:
1. Domain limits: For a fixed $x$, $y$ ranges from $x$ to $1$.
2. $f_X(x) = \int_x^1 6 x dy = 6 x [y]_x^1 = 6 x (1 - x) = 6 x - 6 x^2$ for $0 \le x \le 1$.
3. Check integral: $\int_0^1 (6 x - 6 x^2) dx = [3 x^2 - 2 x^3]_0^1 = 3 - 2 = 1.0$.

## Example 4: Marginal Distribution of Bivariate Gaussian
**Problem**: Multivariate Gaussian $\mathbf{X} \sim \mathcal{N}\left( egin{bmatrix} 5 \ 10 \end{bmatrix}, egin{bmatrix} 4 & 1 \ 1 & 9 \end{bmatrix} ight)$. State marginal distribution of $X_1$.
**Solution**:
1. A key property of Joint Gaussian distributions is that marginals are ALWAYS Gaussian.
2. Mean of $X_1$: $\mu_1 = 5$.
3. Variance of $X_1$: $\Sigma_{11} = 4$.
4. Marginal distribution $X_1 \sim \mathcal{N}(5, 4)$.

## Example 5: Marginal Expectation
**Problem**: Compute $E[X]$ directly from marginal $f_X(x) = 6 x (1 - x)$ on $[0, 1]$.
**Solution**:
1. $E[X] = \int_0^1 x (6 x - 6 x^2) dx = \int_0^1 (6 x^2 - 6 x^3) dx$.
2. $= \left[ 2 x^3 - 1.5 x^4 ight]_0^1 = 2 - 1.5 = 0.50$.
