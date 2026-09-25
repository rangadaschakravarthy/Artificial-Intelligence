# Day 77 Theory: Maximum Likelihood Estimation (MLE)

### 1. Simple Definition
Maximum Likelihood Estimation (MLE) is a method of estimating the parameters of a probability distribution by maximizing a likelihood function, so that the observed sample data is most probable under the assumed model.

### 2. Intuition
Imagine flipping a coin 10 times and getting 8 Heads. What is your best guess for the probability of Heads p?
- If p = 0.1, getting 8 Heads is almost impossible.
- If p = 0.5, getting 8 Heads is somewhat unlikely.
- If p = 0.8, getting 8 Heads has maximum probability!
MLE systematically finds that parameter value (p = 0.8) which maximizes data likelihood!

### 3. Mathematical Definition
Given i.i.d. observations X = {x_1, ..., x_n} from probability density f(x; θ):
Likelihood Function:
L(θ; X) = prod_{i=1}^n f(x_i; θ)

Log-Likelihood Function:
ln L(θ; X) = sum_{i=1}^n ln f(x_i; θ)

MLE Estimator:
θ_hat_{MLE} = argmax_θ ln L(θ; X)

### 4. Mathematical Notation
- L(θ; X): Likelihood function of parameter θ given data X
- l(θ) = ln L(θ; X): Log-likelihood function
- NLL = -ln L(θ; X): Negative Log-Likelihood

### 5. Formula
Optimization Step:
d/dθ [ ln L(θ) ] = 0

Binary Cross-Entropy Loss (NLL for Bernoulli):
NLL = - sum_{i=1}^n [ y_i ln p_i + (1 - y_i) ln(1 - p_i) ]

Gaussian NLL (MSE Loss connection):
NLL = (n/2) ln(2π σ^2) + (1 / (2σ^2)) sum_{i=1}^n (y_i - f(x_i; w))^2

### 6. Symbol Explanation
- f(x_i; θ): Probability mass/density of x_i given parameter θ
- NLL: Negative Log-Likelihood (minimizing NLL is mathematically identical to maximizing Likelihood!)

### 7. Step-by-Step Calculation
Derive MLE for Poisson parameter λ given sample [x1, x2, ..., xn].
Step 1: Probability PMF: f(x; λ) = (λ^x e^(-λ)) / x!
Step 2: Likelihood L(λ) = prod_{i=1}^n [ (λ^{x_i} e^(-λ)) / x_i! ]
Step 3: Log-Likelihood ln L(λ) = sum [ x_i ln λ - λ - ln(x_i!) ] = (ln λ) sum x_i - n λ - sum ln(x_i!)
Step 4: Take derivative wrt λ: d/dλ [ ln L(λ) ] = (1/λ) sum x_i - n = 0
Step 5: Solve for λ: (1/λ) sum x_i = n => λ_hat = (1/n) sum x_i = x_bar.
Conclusion: MLE estimator for Poisson parameter λ is sample mean x_bar!

### 8. Second Concrete Example
Derive MLE for Gaussian Mean μ:
ln L(μ) = - (n/2) ln(2πσ^2) - (1/(2σ^2)) sum (x_i - μ)^2.
d/dμ [ ln L(μ) ] = (1/σ^2) sum (x_i - μ) = 0 => sum x_i - n μ = 0 => μ_hat = x_bar!

### 9. Common Mistakes
- Maximizing product of probabilities directly instead of taking log first (numerical underflow occurs when multiplying thousands of small probabilities!).
- Confusing Likelihood L(θ; X) with Probability P(X; θ). Probability evaluates data given parameters; Likelihood evaluates parameters given observed fixed data!

### 10. AI Connection
Virtually EVERY loss function in Machine Learning is derived from Maximum Likelihood Estimation:
- Minimizing MSE Loss in Linear Regression = Maximizing Gaussian Likelihood!
- Minimizing Binary Cross-Entropy Loss in Logistic Regression = Maximizing Bernoulli Likelihood!
- Minimizing Categorical Cross-Entropy Loss in Neural Nets = Maximizing Multinoulli Likelihood!

### 11. Algorithm Connection
- Logistic Regression weights are optimized via MLE using Gradient Descent / Newton-Raphson.
- Expectation-Maximization (EM) algorithm for GMMs and latent variable models.

### 12. Practical Interpretation
Maximizing likelihood selects the model parameters that make the training dataset most probable.

### 13. Interview Insight
Question: Why do we maximize Log-Likelihood instead of Likelihood directly?
Answer: 1) Products of small probabilities prod p_i cause underflow; taking log transforms products into stable sums sum ln p_i. 2) Derivatives of sums are far easier to compute than derivatives of long product chains!

### 14. Summary
MLE finds parameters maximizing observed data probability; minimizing Negative Log-Likelihood yields standard Deep Learning loss functions (MSE, Cross-Entropy).
