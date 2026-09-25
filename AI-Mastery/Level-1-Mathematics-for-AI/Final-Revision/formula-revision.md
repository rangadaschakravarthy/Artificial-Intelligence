# Formula Revision Cheat-Sheet — Level 1 Mathematics for AI

- **Cosine Similarity**: $\text{sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$
- **Normal Equation**: \mathbf{w} = (X^T X)^{-1} X^T \mathbf{y}
- **Sigmoid Derivative**: $\sigma'(z) = \sigma(z)(1 - \sigma(z))$
- **Gradient Descent**: \mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \eta \nabla f(\mathbf{w}^{(t)})
- **BCE Loss**: $L = -\frac{1}{N} \sum [y_i \ln \hat{y}_i + (1-y_i) \ln(1-\hat{y}_i)]$
- **Bayes' Theorem**: $P(H|E) = \frac{P(E|H) P(H)}{P(E)}$
- **Naive Bayes Rule**: $\hat{y} = \arg\max_c [ \ln P(Y=c) + \sum \ln P(X_i | Y=c) ]$
- **Laplace Smoothing**: $\hat{P}(X_i | c) = \frac{N_{c,i} + \alpha}{N_c + \alpha D}$
- **Gaussian PDF**: $f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$
- **Bessel's Sample Variance**: $s^2 = \frac{1}{n-1} \sum (x_i - \bar{x})^2$
- **Z-Score**: $Z = \frac{x - \mu}{\sigma}$
- **Standard Error**: $SE(\bar{X}) = \frac{s}{\sqrt{n}}$
- **Confidence Interval**: $\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$
- **Chi-Square Statistic**: $\chi^2 = \sum \frac{(O - E)^2}{E}$
- **Cohen's d Effect Size**: $d = \frac{\bar{x}_B - \bar{x}_A}{s_{\text{pooled}}}$
- **F1-Score**: $F_1 = \frac{2 \cdot P \cdot R}{P + R}$
- **Intersection over Union (IoU)**: $\text{IoU} = \frac{|A \cap B|}{|A \cup B|}$
