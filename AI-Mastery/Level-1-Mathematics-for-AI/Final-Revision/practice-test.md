# Final Practice Test — Level 1 Mathematics for AI (50 Questions)

## Linear Algebra (Questions 1–12)
1. Compute the dot product of $\mathbf{u} = [2, 3]$ and $\mathbf{v} = [4, -1]$.
2. Compute $L_2$ norm of $\mathbf{x} = [3, 4]$.
3. Compute Cosine Similarity between $\mathbf{u} = [1, 0]$ and $\mathbf{v} = [1, 1]$.
4. Given 

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$

, compute \det(A).
5. For matrix $A$ in Q4, compute $A^T$.
6. State the inverse formula for a 2 \times 2 matrix 

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

.
7. If $A \mathbf{v} = 5 \mathbf{v}$, what is the eigenvalue $\lambda$?
8. What matrix operation projects a vector onto a subspace?
9. In SVD $A = U \Sigma V^T$, what do the diagonal entries of $\Sigma$ represent?
10. What property defines an orthogonal matrix $Q$?
11. Compute Matrix-Vector product 

$$
\begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 4 \\ 2 \end{bmatrix}
$$

.
12. What is the rank of a matrix with 3 linearly independent columns?

## Calculus (Questions 13–25)
13. Derivative of $f(x) = 4 x^3 - 5 x + 2$.
14. Derivative of Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$.
15. Compute gradient $\nabla f(x, y)$ for $f(x, y) = x^2 + 3 y^2$.
16. Evaluate $\nabla f(1, 2)$ for Q15.
17. Write the Chain Rule formula for $\frac{d}{dx}[f(g(x))]$.
18. Compute derivative of $\ln(x)$ at $x = 5$.
19. Compute Softmax for logits $[0, 0]$.
20. What is the derivative of ReLU $f(x) = \max(0, x)$ for $x > 0$?
21. Write the Gradient Descent update rule for parameter $w$.
22. Write the formula for Mean Squared Error (MSE) loss.
23. Write the formula for Binary Cross-Entropy (BCE) loss.
24. What matrix contains all second-order partial derivatives?
25. What is automatic differentiation in PyTorch?

## Probability (Questions 26–37)
26. If $P(A) = 0.4$, find $P(A^c)$.
27. State Kolmogorov's Second Axiom.
28. If $P(A) = 0.5, P(B) = 0.4, P(A \cap B) = 0.2$, compute $P(A \cup B)$.
29. Compute $P(A|B)$ using numbers in Q28.
30. State Bayes' Theorem formula.
31. Compute $E[X]$ for discrete RV with $P(X=1)=0.3, P(X=2)=0.7$.
32. Compute $\text{Var}(X) = E[X^2] - (E[X])^2$ for Q31.
33. If $X \sim \text{Bern}(0.8)$, state $E[X]$ and $\text{Var}(X)$.
34. If $X$ and $Y$ are independent with $\text{Var}(X)=4, \text{Var}(Y)=9$, find $\text{Var}(X+Y)$.
35. Formula for Pearson Correlation $\rho_{X,Y}$.
36. What is the Naive Bayes assumption?
37. What is Laplace smoothing formula?

## Statistics (Questions 38–50)
38. Compute sample mean of $\{2, 4, 6, 8, 10\}$.
39. Compute sample variance $s^2$ ($ddof=1$) for $\{2, 4, 6\}$.
40. Formula for $Z$-score.
41. For $X \sim \mathcal{N}(50, 10^2)$, compute $Z$-score for $x = 65$.
42. Percentage of data within $\mu \pm 2\sigma$ under Normal Empirical Rule.
43. Formula for Standard Error of Mean $SE(\bar{X})$.
44. State Central Limit Theorem statement for sample size $n \ge 30$.
45. Formula for $95\%$ $Z$-Confidence Interval.
46. State decision rule comparing $p$-value to significance level $\alpha$.
47. What is Type I Error ($\alpha$)?
48. What is Type II Error ($\beta$)?
49. What is Statistical Power ($1 - \beta$)?
50. Formula for Chi-Square test statistic.
