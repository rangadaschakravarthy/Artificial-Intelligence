# Solutions — Continuous Random Variables

## Level 1
1. 1) $f(x) \ge 0$ for all $x$, 2) $\int_{-\infty}^{\infty} f(x) dx = 1$.
2. $0.0$.
3. $f(x) = rac{d}{dx} F(x) = F'(x)$.
4. True. PDF measures density, which can exceed 1 as long as total area integral is 1.
5. $F(-\infty) = 0.0$.

## Level 2
6. $P(X \le 0.5) = \int_0^{0.5} 3 x^2 dx = [x^3]_0^{0.5} = (0.5)^3 = 0.125$.
7. $P(0.2 \le X \le 0.8) = [x^3]_{0.2}^{0.8} = (0.8)^3 - (0.2)^3 = 0.512 - 0.008 = 0.504$.
8. $\int_0^1 k(1-x)dx = k \left[ x - rac{x^2}{2} ight]_0^1 = k \left( 1 - 0.5 ight) = 0.5 k = 1 \implies k = 2$.
9. $F(x) = \int_0^x 2(1-t)dt = \left[ 2t - t^2 ight]_0^x = 2x - x^2$.
10. For Uniform$[10, 20]$, median $m = rac{10 + 20}{2} = 15$.

## Level 3
11. $E[X] = \int_0^1 x (3 x^2) dx = \int_0^1 3 x^3 dx = \left[ rac{3}{4} x^4 ight]_0^1 = 0.75$.
12. $E[X^2] = \int_0^1 x^2 (3 x^2) dx = \int_0^1 3 x^4 dx = \left[ rac{3}{5} x^5 ight]_0^1 = 0.60$. $	ext{Var}(X) = E[X^2] - (E[X])^2 = 0.60 - (0.75)^2 = 0.60 - 0.5625 = 0.0375$.
13. $P(a \le X \le b) = P(X=a) + P(a < X < b) + P(X=b)$. Since $P(X=a) = P(X=b) = 0$ for continuous RVs, $P(a \le X \le b) = P(a < X < b)$.
14. PDF: $f(x) = rac{1}{b-a}$ for $x \in [a, b]$. CDF: $F(x) = rac{x-a}{b-a}$ for $x \in [a, b]$.
15. $F_Y(y) = P(Y \le y) = P(e^X \le y) = P(X \le \ln y) = \ln y$ for $y \in [1, e]$. $f_Y(y) = rac{d}{dy}(\ln y) = rac{1}{y}$ for $y \in [1, e]$.

## Level 4
16. Variance $\sigma^2 = 0.01 \implies \sigma = \sqrt{0.01} = 0.10$.
17. $z = rac{0.02 - 0}{0.10} = 0.20$. $P(-0.2 \le Z \le 0.2) = \Phi(0.2) - \Phi(-0.2) pprox 0.5793 - 0.4207 = 0.1586$.
18. Higher $\sigma^2$ increases spread of noise density, blurring image content and reducing Signal-to-Noise Ratio (SNR).
19. Continuous latent space allows smooth gradient propagation via reparameterization trick $z = \mu + \sigma \odot \epsilon$.
20. Continuous policy PDF provides probability density $f(\mathbf{a}|s)$ used to compute log-likelihood gradients $
abla_	heta \log \pi_	heta(\mathbf{a}|s)$ in Policy Gradient algorithms (SAC, PPO).

## Level 5
21. PMF $p(x) = P(X=x) \le 1$ gives point probabilities for discrete outcomes. PDF $f(x)$ gives probability density per unit length for continuous variables where $P(X=x)=0$ and $\int f(x)dx = 1$.
22. $E[X] = \int_a^b x rac{1}{b-a} dx = rac{b^2 - a^2}{2(b-a)} = rac{a+b}{2}$. $E[X^2] = \int_a^b x^2 rac{1}{b-a} dx = rac{b^3 - a^3}{3(b-a)} = rac{a^2 + ab + b^2}{3}$. $	ext{Var}(X) = rac{a^2 + ab + b^2}{3} - rac{(a+b)^2}{4} = rac{(b-a)^2}{12}$.
23. If $U \sim 	ext{Uniform}(0, 1)$, then $X = F^{-1}(U)$ follows CDF $F_X$. Proof: $P(X \le x) = P(F^{-1}(U) \le x) = P(U \le F(x)) = F(x)$. This is Inverse Transform Sampling.
