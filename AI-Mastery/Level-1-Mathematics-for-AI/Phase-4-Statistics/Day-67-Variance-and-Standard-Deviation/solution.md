# Day 67 Solutions: Variance and Standard Deviation

## Level 1: Basic Concepts
1. Average squared deviation from mean.
2. Square root of variance.
3. Using n-1 denominator in sample variance to correct for bias.
4. Simple sum of deviations sum(x_i - x_bar) is always zero.
5. Mean = 0, Standard Deviation = 1.

## Level 2: Calculation
6. Mean = 8. Squared devs: [16, 0, 16]. Sum = 32. s^2 = 32/2 = 16. s = 4.
7. Population σ^2 = 32/3 = 10.67.
8. Var(5 X - 3) = 5^2 Var(X) = 25 * 16 = 400.
9. z = (110 - 100) / 15 = 10 / 15 = +0.67.
10. s^2 = 180 / 10 = 18. s = sqrt(18) ≈ 4.24.

## Level 3: Conceptual
11. Sample mean x_bar absorbs 1 degree of freedom; expected value of sample sum of squares equals (n-1)σ^2. Dividing by n-1 cancels bias.
12. Var(aX + b) = E[((aX+b) - (aμ+b))^2] = E[(a(X-μ))^2] = a^2 E[(X-μ)^2] = a^2 Var(X).
13. Var(X) = E[(X - μ)^2] = E[X^2 - 2μX + μ^2] = E[X^2] - 2μ E[X] + μ^2 = E[X^2] - 2μ^2 + μ^2 = E[X^2] - μ^2.
14. Taking square root of squared units returns unit dimension back to original scale (e.g. sqrt(m^2) = m).
15. Shifting all points shifts mean by c, leaving relative distances (x_i - μ) identical.

## Level 4: AI Applications
16. Standardizing creates spherical loss contours, allowing isotropic gradient steps towards minimum.
17. Prevents division by zero when feature batch variance σ^2 is zero or near zero.
18. High predictive variance across ensemble models indicates unconfident/uncertain samples.
19. High-variance features dominate Euclidean distance calculations regardless of importance.
20. Maintains signal variance across network layers to prevent vanishing/exploding activations.

## Level 5: Interview Solutions
21. Var(X) = E[(X - μ)^2] = E[X^2 - 2μX + μ^2] = E[X^2] - 2μ E[X] + μ^2 = E[X^2] - (E[X])^2.
22. See `code.py`.
23. Keeps variance of outputs equal to variance of inputs across forward and backward passes.
