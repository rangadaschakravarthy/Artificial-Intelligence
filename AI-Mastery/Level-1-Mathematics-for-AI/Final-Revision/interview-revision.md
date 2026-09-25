# Top 10 High-Frequency Technical Interview Questions — Level 1 Revision

1. **Q**: Why do we use Cosine Similarity over Euclidean Distance for text embeddings?
   **A**: Cosine similarity measures angle rather than magnitude, preventing document length from distorting semantic similarity.

2. **Q**: Explain the Chain Rule in Neural Network Backpropagation.
   **A**: Evaluates loss gradient $\frac{\partial L}{\partial w}$ by multiplying partial derivatives backward along computational graph paths: $\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial z} \frac{\partial z}{\partial w}$.

3. **Q**: Prove why MSE loss corresponds to MLE under Gaussian noise.
   **A**: $-\ln P(y|x) = -\ln \mathcal{N}(y; f(x), \sigma^2) = \text{const} + \frac{1}{2\sigma^2} (y - f(x))^2 \propto \text{MSE}$.

4. **Q**: What is the Naive Bayes assumption?
   **A**: Assumes features $X_i$ are conditionally independent given class label $Y$: $P(X_1, \dots, X_d | Y) = \prod P(X_i | Y)$.

5. **Q**: Why is Laplace Smoothing used in Naive Bayes?
   **A**: Adds pseudo-counts $\alpha > 0$ to prevent unseen word counts from producing zero probabilities ($P=0$) that zero out entire document likelihood products.

6. **Q**: Why does sample variance use $n-1$ instead of $n$ (Bessel's Correction)?
   **A**: Dividing by $n-1$ corrects for sample bias, making $s^2$ an unbiased estimator of population variance ($E[s^2] = \sigma^2$).

7. **Q**: What is the Central Limit Theorem (CLT)?
   **A**: The sampling distribution of the sample mean $\bar{X}$ approaches a Normal distribution $\mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$ as sample size $n \ge 30$ increases, regardless of population shape.

8. **Q**: Correctly interpret a 95% Confidence Interval.
   **A**: In repeated sampling under identical conditions, 95% of constructed confidence intervals will contain the true population parameter $\mu$.

9. **Q**: What is Type I Error ($\alpha$) and Type II Error ($\beta$)?
   **A**: Type I error is rejecting $H_0$ when $H_0$ is true (False Positive). Type II error is failing to reject $H_0$ when $H_0$ is false (False Negative).

10. **Q**: What is a $p$-value?
    **A**: The probability of obtaining a test statistic as or more extreme than observed, assuming $H_0$ is true. If $p \le \alpha$, reject $H_0$.
