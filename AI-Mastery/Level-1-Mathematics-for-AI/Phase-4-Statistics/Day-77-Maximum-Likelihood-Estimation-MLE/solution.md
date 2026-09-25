# Day 77 Solutions: Maximum Likelihood Estimation (MLE)

## Level 1: Basic Concepts
1. Estimating parameters by maximizing probability density of observed data.
2. Turns products into sums (prevents underflow and simplifies differentiation).
3. Probability integrates over data X given fixed θ; Likelihood evaluates parameter θ given fixed data X.
4. NLL = -ln L(θ). Minimizing NLL maximizes Likelihood.
5. Mean Squared Error (MSE).

## Level 2: Calculation
6. L(p) = p^k (1-p)^{n-k} => l(p) = k ln p + (n-k) ln(1-p). dl/dp = k/p - (n-k)/(1-p) = 0 => p_hat = k/n.
7. x_bar = 50 / 10 = 5. λ_hat = 1 / 5 = 0.20.
8. L = (0.75)^3 * (0.25)^1 = 0.421875 * 0.25 = 0.10547. ln L = ln(0.10547) = -2.249.
9. n/λ - sum x_i = 0 => n/λ = sum x_i => λ_hat = n / sum x_i = 1 / x_bar.
10. For U(0, θ), f(x) = 1/θ for 0 <= x <= θ. L(θ) = 1/θ^n provided θ >= max(x_i). To maximize 1/θ^n, choose smallest possible θ => θ_hat = max(x_i) = 9.

## Level 3: Conceptual
11. ln L(w) = - (n/2) ln(2πσ^2) - (1/(2σ^2)) sum (y_i - w^T x_i)^2. Dropping constants leaves - sum (y_i - w^T x_i)^2. Maximizing this is minimizing MSE.
12. ln L(w) = sum [ y_i ln p_i + (1-y_i) ln(1-p_i) ]. Negating gives Binary Cross-Entropy.
13. As n -> infty, MLE converges to true parameter (consistent), errors become Gaussian (asymptotically Normal), and achieves CRLB lower bound (efficient).
14. Differentiating wrt σ^2 gives σ^2_MLE = (1/n) sum (x_i - x_bar)^2. Its expectation is ((n-1)/n) σ^2 < σ^2. Biased!
15. MLE maximizes L(θ) = P(X|θ). MAP maximizes Posterior P(θ|X) = P(X|θ) P(θ), incorporating prior distribution over parameters.

## Level 4: AI Applications
16. Choice of output distribution PMF/PDF dictates the loss function via NLL (-ln P(Y|X)).
17. MSE for classification causes vanishing gradients due to sigmoid saturation; Cross-Entropy produces steep linear gradients.
18. EM algorithm alternates between E-step (computing latent responsibilities) and M-step (maximizing expected complete log-likelihood).
19. Gaussian prior P(w) = N(0, τ^2) adds -||w||^2 / (2τ^2) to log-likelihood, which is L2 Ridge penalty!
20. MLE fits observed sample noise perfectly without prior constraints.

## Level 5: Interview Solutions
21. d/dμ [ ln L ] = 0 => μ_hat = x_bar. d/dσ^2 [ ln L ] = -n/(2σ^2) + (1/(2σ^4)) sum (x_i - x_bar)^2 = 0 => σ^2_hat = (1/n) sum (x_i - x_bar)^2.
22. See `code.py`.
23. MAP: argmax P(θ|X) = argmax [ P(X|θ) P(θ) / P(X) ] = argmax [ ln P(X|θ) + ln P(θ) ] = MLE + Log-Prior.
