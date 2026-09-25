# Quick Revision — Level 1 Mathematics for AI

## Phase 1: Linear Algebra (Days 1–25)
- **Vector Operations**: $\mathbf{u} \cdot \mathbf{v} = \sum u_i v_i$, Cosine Similarity $\frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$.
- **Norms**: $L_1 = \sum |x_i|$, $L_2 = \sqrt{\sum x_i^2}$.
- **Matrices**: Multiplication $(AB)_{ij} = \sum A_{ik} B_{kj}$, Transpose $(AB)^T = B^T A^T$, Determinant $\det(A) \neq 0 \implies$ Invertible.
- **Eigenvalues**: $A \mathbf{v} = \lambda \mathbf{v}$. PCA computes eigenvectors of covariance matrix $X^T X$.
- **SVD**: $A = U \Sigma V^T$. Recommender systems and dimensionality reduction.

## Phase 2: Calculus (Days 26–43)
- **Derivatives**: Power rule, Product rule, Quotient rule, Chain rule.
- **Activations**: Sigmoid $\sigma(z) = \frac{1}{1+e^{-z}}$, Softmax $\frac{e^{z_i}}{\sum e^{z_j}}$.
- **Gradients**: $\nabla f = [\partial f / \partial x_i]^T$. Steepest descent direction.
- **Backpropagation**: Repeated application of chain rule backward through computational graphs.
- **Optimization**: SGD, Mini-Batch, Adam. Loss functions: MSE, BCE, Cross-Entropy.

## Phase 3: Probability (Days 44–62)
- **Rules**: $P(A \cup B) = P(A)+P(B)-P(A \cap B)$, $P(A|B) = \frac{P(A \cap B)}{P(B)}$.
- **Bayes' Theorem**: $P(H|E) = \frac{P(E|H)P(H)}{P(E)}$. Naive Bayes: $P(Y|X) \propto P(Y) \prod P(X_i|Y)$.
- **Distributions**: Bernoulli, Binomial, Poisson, Uniform, Gaussian Normal $\mathcal{N}(\mu, \sigma^2)$.
- **Moments**: $E[X] = \sum x p(x)$, $\text{Var}(X) = E[X^2] - (E[X])^2$, $SE = \frac{\sigma}{\sqrt{n}}$.
- **Covariance**: $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$, Correlation $\rho = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$.

## Phase 4: Statistics (Days 63–85)
- **Descriptive**: Mean, Median, Mode, Variance $s^2 = \frac{1}{n-1}\sum(x_i-\bar{x})^2$, $IQR = Q_3 - Q_1$.
- **Normal & Z-Scores**: $Z = \frac{x-\mu}{\sigma} \sim \mathcal{N}(0, 1)$, Empirical rule 68-95-99.7.
- **CLT**: Sample mean $\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$ for $n \ge 30$.
- **CIs**: $\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$.
- **Hypothesis Testing**: 5-step framework, $p \le \alpha \implies$ Reject $H_0$. Type I error $\alpha$, Type II error $\beta$, Power $1-\beta$.
- **Tests**: $Z$-test, $t$-test (1-sample, 2-sample, paired), Chi-Square test of independence.
