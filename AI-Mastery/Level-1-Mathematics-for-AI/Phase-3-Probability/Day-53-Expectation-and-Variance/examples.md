# Worked Examples — Expectation and Variance

## Example 1: Discrete Expectation & Variance
**Problem**: Roll a fair 6-sided die ($X$). Calculate $E[X]$ and $	ext{Var}(X)$.
**Solution**:
1. $E[X] = \sum_{x=1}^6 x \left(\frac{1}{6}
ight) = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$.
2. $E[X^2] = \sum_{x=1}^6 x^2 \left(\frac{1}{6}
ight) = \frac{1+4+9+16+25+36}{6} = \frac{91}{6} pprox 15.1667$.
3. $	ext{Var}(X) = 15.1667 - (3.5)^2 = 15.1667 - 12.25 = 2.9167$.

## Example 2: Linearity of Expectation (Sum of Dice)
**Problem**: Roll 10 fair 6-sided dice. Let $S = \sum_{i=1}^{10} X_i$ be the sum. Find $E[S]$.
**Solution**:
1. By Linearity of Expectation: $E[S] = \sum_{i=1}^{10} E[X_i]$.
2. Each $E[X_i] = 3.5$.
3. $E[S] = 10 	imes 3.5 = 35.0$.

## Example 3: Variance Scaling Rule
**Problem**: Let $X$ have $	ext{Var}(X) = 5$. Compute $	ext{Var}(3X - 7)$.
**Solution**:
1. $	ext{Var}(aX + b) = a^2 	ext{Var}(X)$.
2. Here $a = 3, b = -7$.
3. $	ext{Var}(3X - 7) = 3^2 	ext{Var}(X) = 9 	imes 5 = 45$.

## Example 4: Continuous Expectation (Uniform)
**Problem**: $X \sim 	ext{Uniform}(0, 4)$. Calculate $E[X^2]$.
**Solution**:
1. $f(x) = 0.25$ for $x \in [0, 4]$.
2. $E[X^2] = \int_0^4 x^2 (0.25) dx = 0.25 \left[ \frac{x^3}{3} 
ight]_0^4 = 0.25 \left( \frac{64}{3} 
ight) = \frac{16}{3} pprox 5.3333$.

## Example 5: AI Bias-Variance Decomposition
**Problem**: A model has $	ext{Bias} = 0.2$, $	ext{Variance} = 0.15$, and irreducible noise $\sigma_{	ext{noise}}^2 = 0.05$. Calculate Total Expected Error.
**Solution**:
1. Total Error $= 	ext{Bias}^2 + 	ext{Variance} + \sigma_{	ext{noise}}^2$.
2. $	ext{Bias}^2 = (0.2)^2 = 0.04$.
3. Total Error $= 0.04 + 0.15 + 0.05 = 0.24$.
