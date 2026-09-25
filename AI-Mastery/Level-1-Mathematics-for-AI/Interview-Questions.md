# Level 1 Mathematics for AI — 50 Master Technical Interview Questions

1. **Q**: What is the geometric interpretation of the dot product $\mathbf{u} \cdot \mathbf{v}$?
   **A**: It measures the directional alignment of two vectors, equal to the length of the projection of $\mathbf{u}$ onto $\mathbf{v}$ multiplied by the length of $\mathbf{v}$ ($\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$).

2. **Q**: Why is Cosine Similarity preferred over Euclidean distance for text embeddings?
   **A**: Cosine similarity measures angle rather than magnitude. In NLP, document length scales vector magnitude without changing semantic direction.

3. **Q**: What are the conditions for a matrix to be invertible?
   **A**: Square matrix ($n \times n$), non-zero determinant ($\det(A) \neq 0$), full rank ($	ext{rank}(A) = n$), linearly independent columns.

4. **Q**: Explain Eigenvalues and Eigenvectors in simple terms.
   **A**: An eigenvector $\mathbf{v}$ of a matrix $A$ is a special vector whose direction remains unchanged when multiplied by $A$; it only stretches or shrinks by scalar factor $\lambda$ (the eigenvalue): $A \mathbf{v} = \lambda \mathbf{v}$.

5. **Q**: How does PCA use Eigen-decomposition or SVD?
   **A**: PCA computes eigenvectors of the data covariance matrix $X^T X$. The eigenvectors with the largest eigenvalues form orthogonal axes of maximum data variance.

6. **Q**: What is Singular Value Decomposition (SVD)?
   **A**: Factorization of any $m \times n$ matrix $A$ into $U \Sigma V^T$, where $U$ and $V$ are orthogonal matrices containing singular vectors and $\Sigma$ is a diagonal matrix of singular values.

7. **Q**: Why do we use activations like ReLU instead of linear activations in deep neural networks?
   **A**: Composing multiple linear layers without non-linear activations collapses mathematically into a single linear transformation ($W_2 W_1 x = W_{net} x$), failing to learn complex non-linear functions.

8. **Q**: What is the derivative of the Sigmoid function $\sigma(z)$?
   **A**: $\sigma'(z) = \sigma(z)(1 - \sigma(z))$.

9. **Q**: Explain the Chain Rule in Backpropagation.
   **A**: Backpropagation evaluates gradient $\frac{\partial L}{\partial w}$ by repeatedly multiplying partial derivatives backward along computational graph paths using chain rule: $\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial z} \frac{\partial z}{\partial w}$.

10. **Q**: What is the Gradient Vector $\nabla f(\mathbf{x})$?
    **A**: Vector of partial derivatives $\left[ \frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_d} \right]^T$ pointing in the direction of steepest rate of increase of function $f$.

11. **Q**: What is a Jacobian Matrix?
    **A**: A matrix of all first-order partial derivatives of a vector-valued function $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$, where $J_{ij} = \frac{\partial f_i}{\partial x_j}$.

12. **Q**: What is a Hessian Matrix?
    **A**: A square matrix of all second-order partial derivatives $H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$, measuring local curvature of a scalar function.

13. **Q**: What is the difference between Batch Gradient Descent, SGD, and Mini-Batch Gradient Descent?
    **A**: Batch computes gradients over the full dataset ($N$); SGD computes over 1 random sample ($N=1$); Mini-Batch computes over small batches ($B$, e.g. 32-256).

14. **Q**: Why is Learning Rate $\eta$ crucial in Gradient Descent?
    **A**: Too large $\eta$ causes divergent overshooting; too small $\eta$ causes extremely slow convergence or trapping in sub-optimal local minima.

15. **Q**: Prove why minimizing MSE loss corresponds to Maximum Likelihood Estimation under Gaussian noise.
    **A**: Likelihood $P(y|x) = \mathcal{N}(y; f(x), \sigma^2) \propto \exp\left( -\frac{(y - f(x))^2}{2\sigma^2} \right)$. Negative log-likelihood yields $-\ln P(y|x) = \text{const} + \frac{1}{2\sigma^2} (y - f(x))^2$, identical to MSE.

16. **Q**: Prove why minimizing Binary Cross-Entropy corresponds to MLE under Bernoulli likelihood.
    **A**: Likelihood $P(y|x) = \hat{y}^y (1-\hat{y})^{1-y}$. Negative log-likelihood yields $-\ln P = -[y \ln \hat{y} + (1-y) \ln(1-\hat{y})]$, which is BCE loss.

17. **Q**: What are Kolmogorov's Axioms of Probability?
    **A**: 1) Non-negativity $P(A) \ge 0$, 2) Unitarity $P(\Omega) = 1$, 3) Countable Additivity for disjoint events $P(\bigcup A_i) = \sum P(A_i)$.

18. **Q**: What is the difference between Frequentist and Bayesian views of probability?
    **A**: Frequentist treats probability as long-run limiting frequency of repeatable events with fixed unknown parameters; Bayesian treats probability as degree of belief updated via evidence ($P(\theta|D)$).

19. **Q**: State Bayes' Theorem and identify its four components.
    **A**: $P(H|E) = \frac{P(E|H)P(H)}{P(E)}$. Posterior $P(H|E)$, Likelihood $P(E|H)$, Prior $P(H)$, Evidence $P(E)$.

20. **Q**: What is the Base Rate Fallacy?
    **A**: Ignoring the prior probability $P(H)$ when computing posterior probability $P(H|E)$, leading to severe overestimation of posterior probability for rare events.

21. **Q**: What is the Naive Bayes assumption?
    **A**: Assumes features $X_1, \dots, X_d$ are conditionally independent of each other given the class label $Y$: $P(X_1, \dots, X_d | Y) = \prod P(X_i | Y)$.

22. **Q**: Why is Laplace Smoothing used in Naive Bayes?
    **A**: Adds pseudo-counts $\alpha > 0$ to prevent unseen word counts from producing zero probabilities ($P=0$) that zero out entire document likelihood products.

23. **Q**: What is the difference between PMF and PDF?
    **A**: PMF $p(x) = P(X=x) \le 1$ gives point probabilities for discrete random variables. PDF $f(x)$ gives probability density for continuous variables where $P(X=x) = 0$ and $\int_a^b f(x) dx = P(a \le X \le b)$.

24. **Q**: What is Linearity of Expectation? Does it require independence?
    **A**: $E[aX + bY + c] = a E[X] + b E[Y] + c$. It holds for ALL random variables, dependent or independent!

25. **Q**: What is the formula for Variance in terms of Expectations?
    **A**: $\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$.

26. **Q**: What is $\text{Var}(aX + b)$?
    **A**: $a^2 \text{Var}(X)$.

27. **Q**: When does $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ hold?
    **A**: When $X$ and $Y$ are uncorrelated ($\text{Cov}(X,Y) = 0$), such as when independent.

28. **Q**: What is Pearson Correlation Coefficient $\rho_{X,Y}$?
    **A**: $\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$, bounded in $[-1, 1]$.

29. **Q**: Does zero correlation ($\rho = 0$) imply independence?
    **A**: No. Zero correlation only rules out linear association. Non-linear dependencies (e.g. $Y = X^2$ for symmetric $X$) can have $\rho = 0$. (Exception: Jointly Gaussian variables where $\rho=0 \implies$ independence).

30. **Q**: What is Marginalization?
    **A**: Summing or integrating out nuisance variables from a joint distribution to obtain a marginal distribution: $f_X(x) = \int f(x,y) dy$.

31. **Q**: What is the 68-95-99.7 Empirical Rule for Normal distributions?
    **A**: $\mu \pm 1\sigma \approx 68.27\%$, $\mu \pm 2\sigma \approx 95.45\%$, $\mu \pm 3\sigma \approx 99.73\%$ of data.

32. **Q**: How do you compute a $Z$-score?
    **A**: $Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$.

33. **Q**: What is the difference between $L_1$ (Lasso) and $L_2$ (Ridge) regularization from a MAP perspective?
    **A**: $L_2$ regularization corresponds to MAP estimation under a Gaussian prior $\mathbf{w} \sim \mathcal{N}(0, \tau^2 I)$; $L_1$ regularization corresponds to MAP under a Laplacian prior.

34. **Q**: What is the difference between Descriptive and Inferential Statistics?
    **A**: Descriptive statistics summarizes observed sample features; Inferential statistics uses sample statistics to draw conclusions about unknown population parameters.

35. **Q**: What is the NOIR framework for data measurement scales?
    **A**: Nominal (unranked categories), Ordinal (ranked categories), Interval (equal intervals, no true zero), Ratio (equal intervals, absolute true zero).

36. **Q**: Why is Median preferred over Mean for skewed distributions with outliers?
    **A**: Median is positional (50th percentile) and robust to extreme values, whereas Mean incorporates exact outlier magnitudes, distorting central tendency.

37. **Q**: What is the Harmonic Mean, and where is it used in AI?
    **A**: $H = \frac{N}{\sum \frac{1}{x_i}}$. Used in F1-score metric $F_1 = \frac{2 P R}{P + R}$ to heavily penalize extreme imbalances between Precision and Recall.

38. **Q**: What is Bessel's Correction in sample variance, and why is it used?
    **A**: Using $n-1$ instead of $n$ in sample variance $s^2 = \frac{1}{n-1} \sum (x_i - \bar{x})^2$. It produces an unbiased estimator of population variance ($E[s^2] = \sigma^2$).

39. **Q**: What is the Boxplot outlier rule?
    **A**: Outliers are points below $Q_1 - 1.5 \times IQR$ or above $Q_3 + 1.5 \times IQR$.

40. **Q**: What is Skewness?
    **A**: 3rd standardized moment measuring asymmetry. Positive (right) skew has long right tail (Mode < Median < Mean); Negative (left) skew has long left tail (Mean < Median < Mode).

41. **Q**: What is Excess Kurtosis?
    **A**: 4th standardized moment minus 3 ($K_{\text{excess}} = K - 3$). Measures tail heaviness relative to Normal distribution.

42. **Q**: What is the Central Limit Theorem (CLT)?
    **A**: The sampling distribution of the sample mean $\bar{X}$ approaches a Normal distribution $\mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$ as sample size $n \ge 30$ increases, regardless of underlying population shape.

43. **Q**: What is Standard Error of the Mean ($SE$)?
    **A**: The standard deviation of the sampling distribution of the mean: $SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}$.

44. **Q**: What is the Square Root Law of sample size?
    **A**: Halving standard error ($SE \to SE/2$) requires quadrupling sample size ($n \to 4n$).

45. **Q**: Correctly interpret a $95\%$ Confidence Interval $[90, 100]$.
    **A**: In repeated sampling under identical conditions, $95\%$ of constructed intervals will contain the true population parameter $\mu$.

46. **Q**: What is Type I Error ($\alpha$) and Type II Error ($\beta$)?
    **A**: Type I error is rejecting $H_0$ when $H_0$ is true (False Positive). Type II error is failing to reject $H_0$ when $H_0$ is false (False Negative).

47. **Q**: What is Statistical Power?
    **A**: $\text{Power} = 1 - \beta$ (probability of correctly rejecting $H_0$ when a true effect exists). Target power is $\ge 80\%$.

48. **Q**: What is a $p$-value?
    **A**: The probability of obtaining a test statistic as or more extreme than observed, assuming $H_0$ is true. If $p \le \alpha$, reject $H_0$.

49. **Q**: When should you use a Welch's t-test over a Student's t-test?
    **A**: Use Welch's t-test when comparing means of two independent groups with unequal sample variances (heteroscedasticity).

50. **Q**: What is the difference between Statistical Significance and Practical Significance?
    **A**: Statistical significance ($p \le \alpha$) confirms an effect is unlikely due to chance; Practical significance (Effect size, Cohen's $d$) measures whether the effect magnitude is large enough to matter in real-world application.
