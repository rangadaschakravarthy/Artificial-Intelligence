# Day 77 Worked Examples: Maximum Likelihood Estimation (MLE)

## Example 1: Very Easy — Coin Flip MLE
Flip coin 10 times, get k = 7 Heads.
Likelihood L(p) = p^7 (1-p)^3.
Log-likelihood l(p) = 7 ln(p) + 3 ln(1-p).
dl/dp = 7/p - 3/(1-p) = 0 => 7(1-p) = 3p => 7 = 10p => p_hat = 0.70.

## Example 2: Beginner — Exponential Distribution MLE
PMF: f(x; λ) = λ e^(-λ x).
ln L(λ) = n ln(λ) - λ sum x_i.
d/dλ [ ln L ] = n/λ - sum x_i = 0 => λ_hat = n / sum x_i = 1 / x_bar.

## Example 3: Intermediate — MLE Equivalence to Least Squares (MSE)
Given y_i = w^T x_i + ε_i where ε_i ~ N(0, σ^2).
L(w) = prod (1 / sqrt(2π σ^2)) exp( - (y_i - w^T x_i)^2 / (2σ^2) ).
ln L(w) = Const - (1 / (2σ^2)) sum (y_i - w^T x_i)^2.
Maximizing ln L(w) is equivalent to MINIMIZING sum (y_i - w^T x_i)^2 (MSE Loss!).

## Example 4: AI Focus — Logistic Regression Binary Cross-Entropy
Model output p_i = σ(w^T x_i).
Bernoulli Likelihood: L(w) = prod p_i^{y_i} (1 - p_i)^{1 - y_i}.
Negative Log-Likelihood NLL(w) = - sum [ y_i ln p_i + (1 - y_i) ln(1 - p_i) ].
This is exact Binary Cross-Entropy Loss!

## Example 5: Real-World AI — LLM Next-Token Prediction
Large Language Models (GPT-4) predict next token probability distribution P(w_t | w_1...w_{t-1}). Model training optimizes MLE over trillions of tokens using Cross-Entropy loss.
