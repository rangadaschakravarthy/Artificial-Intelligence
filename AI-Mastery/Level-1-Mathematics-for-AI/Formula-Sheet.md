# Level 1 Mathematics for AI — Ultimate Master Formula Sheet

## 1. Linear Algebra Formulas
- **Vector Dot Product**: $\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^d u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta)$
- **Cosine Similarity**: $\text{sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$
- **Vector Norms**:
  - $L_1$ Norm (Manhattan): $\|\mathbf{x}\|_1 = \sum_{i=1}^d |x_i|$
  - $L_2$ Norm (Euclidean): $\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^d x_i^2}$
  - $L_\infty$ Norm (Max): $\|\mathbf{x}\|_\infty = \max_i |x_i|$
- **Matrix Multiplication**: $(AB)_{ij} = \sum_{k} A_{ik} B_{kj}$
- **Matrix Determinant (2x2)**: 

$$\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

- **Matrix Inverse (2x2)**: 

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

- **Eigenvalue Equation**: $A \mathbf{v} = \lambda \mathbf{v} \implies (A - \lambda I) \mathbf{v} = \mathbf{0} \implies \det(A - \lambda I) = 0$
- **Singular Value Decomposition (SVD)**: $A = U \Sigma V^T$
- **Linear Regression Normal Equation**: \mathbf{w} = (X^T X)^{-1} X^T \mathbf{y}

## 2. Calculus Formulas
- **Power Rule**: $\frac{d}{dx}[x^n] = n x^{n-1}$
- **Product Rule**: $\frac{d}{dx}[u v] = u' v + u v'$
- **Quotient Rule**: $\frac{d}{dx}\left[\frac{u}{v}\right] = \frac{u' v - u v'}{v^2}$
- **Chain Rule**: $\frac{d}{dx}[f(g(x))] = f'(g(x)) g'(x)$
- **Sigmoid Function**: $\sigma(z) = \frac{1}{1 + e^{-z}}, \quad \sigma'(z) = \sigma(z)(1 - \sigma(z))$
- **Softmax Function**: $\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$
- **Gradient Vector**: $\nabla f(\mathbf{x}) = \left[ \frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_d} \right]^T$
- **Gradient Descent Update**: \mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \eta \nabla f(\mathbf{w}^{(t)})
- **Mean Squared Error (MSE)**: $L_{\text{MSE}} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$
- **Binary Cross-Entropy (BCE)**: $L_{\text{BCE}} = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \ln \hat{y}_i + (1 - y_i) \ln(1 - \hat{y}_i) \right]$

## 3. Probability Formulas
- **Addition Rule**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Conditional Probability**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
- **Bayes' Theorem**: $P(H|E) = \frac{P(E|H) P(H)}{P(E)} = \frac{P(E|H) P(H)}{P(E|H)P(H) + P(E|H^c)P(H^c)}$
- **Discrete Expectation & Variance**: $E[X] = \sum x p(x), \quad \text{Var}(X) = E[X^2] - (E[X])^2$
- **Continuous Expectation & Variance**: $E[X] = \int x f(x) dx, \quad \text{Var}(X) = \int (x - \mu)^2 f(x) dx$
- **Linearity of Expectation**: $E[aX + bY + c] = a E[X] + b E[Y] + c$
- **Variance Scaling**: $\text{Var}(aX + b) = a^2 \text{Var}(X)$
- **Covariance**: $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$
- **Pearson Correlation**: $\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$
- **Gaussian Normal PDF**: $f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right)$
- **Binomial PMF**: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
- **Poisson PMF**: $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$

## 4. Statistics Formulas
- **Sample Mean**: $\bar{x} = \frac{1}{n} \sum x_i$
- **Sample Variance (Bessel's)**: $s^2 = \frac{1}{n-1} \sum (x_i - \bar{x})^2$
- **$Z$-Score Standardization**: $Z = \frac{x - \mu}{\sigma} \sim \mathcal{N}(0, 1)$
- **Standard Error of Mean**: $SE(\bar{X}) = \frac{\sigma}{\sqrt{n}} \approx \frac{s}{\sqrt{n}}$
- **Standard Error of Proportion**: $SE(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
- **Confidence Interval (Z)**: $\bar{x} \pm Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$
- **Confidence Interval (t)**: $\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$
- **1-Sample $t$-Statistic**: $t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$
- **Chi-Square Statistic**: $\chi^2 = \sum \frac{(O - E)^2}{E}$
- **Cohen's $d$ Effect Size**: $d = \frac{\bar{x}_B - \bar{x}_A}{s_{\text{pooled}}}$
- **F1-Score**: $F_1 = \frac{2 \cdot P \cdot R}{P + R}$
- **Intersection over Union (IoU)**: $\text{IoU} = \frac{|A \cap B|}{|A \cup B|}$
