# Worked Examples — Naive Bayes Algorithm Mathematics

## Example 1: Laplace Smoothed Probability
**Problem**: In 1,000 Ham emails (total word count 50,000 across vocabulary $D = 10,000$), word "Crypto" appears $0$ times. Compute Laplace smoothed $P(	ext{"Crypto"}|	ext{Ham})$ with $lpha = 1$.
**Solution**:
1. $P(	ext{"Crypto"}|	ext{Ham}) = \frac{N_{c,i} + 1}{N_c + 1 	imes D} = \frac{0 + 1}{50000 + 10000} = \frac{1}{60000} pprox 0.00001667$.
2. (Without Laplace smoothing, it would be $0/50000 = 0$).

## Example 2: Log-Domain Score Comparison
**Problem**: Class 0: $\ln P(Y=0) = -0.693$, $\sum \ln P(X_i|0) = -12.45$. Class 1: $\ln P(Y=1) = -0.693$, $\sum \ln P(X_i|1) = -8.30$. Determine predicted class.
**Solution**:
1. Score(Class 0) $= -0.693 + (-12.45) = -13.143$.
2. Score(Class 1) $= -0.693 + (-8.30) = -8.993$.
3. Since $-8.993 > -13.143$, predicted class is Class 1.

## Example 3: Gaussian Naive Bayes Prediction
**Problem**: Class 0: $X_1 \sim \mathcal{N}(0, 1)$. Class 1: $X_1 \sim \mathcal{N}(3, 1)$. Priors are equal ($0.5$). Classify point $x_1 = 2.0$.
**Solution**:
1. Likelihood Class 0: $f_0(2) = \frac{1}{\sqrt{2\pi}} e^{-(2-0)^2 / 2} = \frac{1}{\sqrt{2\pi}} e^{-2} pprox 0.3989 	imes 0.1353 pprox 0.0540$.
2. Likelihood Class 1: $f_1(2) = \frac{1}{\sqrt{2\pi}} e^{-(2-3)^2 / 2} = \frac{1}{\sqrt{2\pi}} e^{-0.5} pprox 0.3989 	imes 0.6065 pprox 0.2419$.
3. Since $f_1(2) > f_0(2)$, predicted class is Class 1.

## Example 4: Bernoulli Naive Bayes Likelihood
**Problem**: Binary feature $X_1$ (has attachment). For Spam ($c=1$), $P(X_1=1|1) = 0.80$. For Ham ($c=0$), $P(X_1=1|0) = 0.10$. Evaluate likelihood term $P(X_1=x_1 | c)$ for an email without attachment ($x_1 = 0$).
**Solution**:
1. For Spam ($c=1$): $P(X_1=0|1) = 1 - 0.80 = 0.20$.
2. For Ham ($c=0$): $P(X_1=0|0) = 1 - 0.10 = 0.90$.

## Example 5: Softmax Normalized Posterior Scores
**Problem**: Unnormalized log posteriors for 2 classes are $S_0 = -10.0$ and $S_1 = -8.0$. Compute normalized posterior probabilities $P(Y=0|X)$ and $P(Y=1|X)$.
**Solution**:
1. Max log-score offset: $S_{\max} = -8.0$.
2. Exponents: $e^{-10 - (-8)} = e^{-2} pprox 0.1353$. $e^{-8 - (-8)} = e^0 = 1.0$.
3. Sum $= 1.1353$.
4. $P(Y=0|X) = \frac{0.1353}{1.1353} pprox 0.1192 = 11.92\%$.
5. $P(Y=1|X) = \frac{1.0}{1.1353} pprox 0.8808 = 88.08\%$.
