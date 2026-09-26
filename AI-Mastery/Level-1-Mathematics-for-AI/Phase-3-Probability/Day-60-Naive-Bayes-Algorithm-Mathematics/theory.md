# Theory — Naive Bayes Algorithm Mathematics

## 1. Simple Definition
The Naive Bayes classifier is a probabilistic machine learning algorithm that applies Bayes' Theorem with the "naive" assumption that all input features are conditionally independent of each other given the class label.

## 2. Intuition
To classify an email as Spam or Ham based on words $W_1, W_2, W_3$, Naive Bayes multiplies the prior probability of Spam by the individual likelihood of seeing each word in Spam emails.

## 3. Mathematical Decision Rule
$$\hat{y} = rg\max_{y \in \mathcal{Y}} P(Y=y \mid X_1, \dots, X_d) = rg\max_{y \in \mathcal{Y}} \left[ P(Y=y) \prod_{i=1}^d P(X_i \mid Y=y) 
ight]$$

In Log-Domain (prevents floating point underflow):
$$\hat{y} = rg\max_{y \in \mathcal{Y}} \left[ \ln P(Y=y) + \sum_{i=1}^d \ln P(X_i \mid Y=y) 
ight]$$

## 4. Variants of Naive Bayes
1. **Gaussian Naive Bayes (Continuous Features)**:
   $$P(X_i = x_i \mid Y=c) = rac{1}{\sqrt{2\pi \sigma_{c,i}^2}} \exp\left( -rac{(x_i - \mu_{c,i})^2}{2\sigma_{c,i}^2} 
ight)$$
2. **Multinomial Naive Bayes (Word Counts)**:
   

$$
P(X_i = x_i \mid Y=c) = rac{N_{c,i} + lpha}{N_c + lpha D}
$$

3. **Bernoulli Naive Bayes (Binary Features)**:
   

$$
P(X_i \mid Y=c) = P_{c,i}^{x_i} (1 - P_{c,i})^{1 - x_i}
$$

## 5. Laplace Smoothing (Add-$lpha$ Smoothing)
If a word never appeared in Spam during training ($N_{c,i} = 0$), raw probability becomes $P(X_i|c) = 0$, multiplying the entire product to 0!
Laplace smoothing adds pseudo-counts $lpha > 0$ (typically $lpha = 1$):

$$
\hat{P}(X_i \mid Y=c) = rac{N_{c,i} + lpha}{N_c + lpha D}
$$

## 6. Notation
- $N_{c,i}$: Count of feature $i$ in class $c$.
- $N_c$: Total count of all features in class $c$.
- $D$: Total number of features (vocabulary size).
- $lpha$: Smoothing parameter (Laplace smoothing if $lpha=1$).

## 7. Step-by-Step Calculation
Classification: 2 classes (Spam, Ham). Vocabulary size $D = 3$.
- Priors: $P(	ext{Spam}) = 0.5, P(	ext{Ham}) = 0.5$.
- Word counts in Spam ($N_{	ext{Spam}} = 100$): $N_{S,1} = 50, N_{S,2} = 30, N_{S,3} = 20$.
Laplace smoothed likelihood for Word 1 in Spam ($lpha=1$):

$$
P(W_1 \mid 	ext{Spam}) = rac{50 + 1}{100 + 1(3)} = rac{51}{103} pprox 0.4951
$$

## 8. Second Example (Gaussian Naive Bayes)
Feature $X_1$ (Height in cm) for Class $c$ (Male): $\mu_{c,1} = 175, \sigma_{c,1} = 10$.
Evaluate likelihood for observed height $x_1 = 180$:
$$P(X_1=180 \mid 	ext{Male}) = rac{1}{10 \sqrt{2\pi}} \exp\left( -rac{(180 - 175)^2}{2(100)} 
ight) = rac{1}{25.1327} e^{-25/200} = 0.0398 	imes e^{-0.125} pprox 0.0351$$

## 9. Common Mistakes
- Omitting Laplace smoothing, resulting in zero-probability zeroing out entire products.
- Computing products of raw probabilities instead of sums of log-probabilities for large $d$ ($> 100$ features), causing floating point underflow to 0.

## 10. AI Connection
Serves as the standard fast baseline for text classification, sentiment analysis, and spam filtering in industrial ML pipelines.

## 11. Algorithm Connection
- **Scikit-Learn**: `GaussianNB`, `MultinomialNB`, `BernoulliNB`.

## 12. Practical Interpretation
Despite violating independence assumptions, Naive Bayes yields linear decision boundaries that are highly effective when feature dimensions exceed sample size ($d \gg N$).

## 13. Interview Insight
**Q**: Why do we use Log-Probabilities $\sum \ln P(X_i|Y)$ in Naive Bayes implementation?
**A**: Multiplying hundreds of probabilities $p_i \in (0, 1)$ causes floating point numerical underflow to absolute zero. Logarithms transform multiplication into addition of stable negative numbers.

## 14. Summary
Naive Bayes combines Bayes' Theorem, feature conditional independence, Laplace smoothing, and log-domain sums for ultra-fast classification.
