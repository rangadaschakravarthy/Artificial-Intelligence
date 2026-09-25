# Final Practice Test Solutions — Level 1 Mathematics for AI

1. $\mathbf{u} \cdot \mathbf{v} = 2(4) + 3(-1) = 8 - 3 = 5$.
2. \|\mathbf{x}\|_2 = \sqrt{3^2 + 4^2} = \sqrt{25} = 5.
3. $\mathbf{u} \cdot \mathbf{v} = 1(1) + 0(1) = 1$. $\|\mathbf{u}\| = 1, \|\mathbf{v}\| = \sqrt{2}$. $\text{sim} = \frac{1}{\sqrt{2}} \approx 0.7071$.
4. $\det(A) = (1)(4) - (2)(3) = 4 - 6 = -2$.
5. $A^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}$.
6. $A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$.
7. Eigenvalue $\lambda = 5$.
8. Orthogonal projection matrix $P = A (A^T A)^{-1} A^T$.
9. Singular values $\sigma_i$ (square roots of eigenvalues of $A^T A$).
10. $Q^T Q = Q Q^T = I \implies Q^{-1} = Q^T$.
11. $\begin{bmatrix} 2(4)+1(2) \\ 0(4)+3(2) \end{bmatrix} = \begin{bmatrix} 10 \\ 6 \end{bmatrix}$.
12. Rank $= 3$.
13. $f'(x) = 12 x^2 - 5$.
14. $\sigma'(z) = \sigma(z)(1 - \sigma(z))$.
15. $\nabla f(x, y) = [2x, 6y]^T$.
16. $\nabla f(1, 2) = [2(1), 6(2)]^T = [2, 12]^T$.
17. $\frac{d}{dx}[f(g(x))] = f'(g(x)) g'(x)$.
18. $\frac{d}{dx}[\ln(x)] = \frac{1}{x} \implies \frac{1}{5} = 0.20$.
19. $\text{Softmax}([0, 0]) = [0.5, 0.5]$.
20. $f'(x) = 1$ for $x > 0$.
21. $w^{(t+1)} = w^{(t)} - \eta \nabla f(w^{(t)})$.
22. $L_{\text{MSE}} = \frac{1}{N} \sum (y_i - \hat{y}_i)^2$.
23. $L_{\text{BCE}} = -\frac{1}{N} \sum [y_i \ln \hat{y}_i + (1-y_i) \ln(1-\hat{y}_i)]$.
24. Hessian Matrix $H$.
25. Computing gradients using chain rule over dynamic computational graphs (`autograd`).
26. $P(A^c) = 1 - 0.4 = 0.6$.
27. Unitarity: $P(\Omega) = 1$.
28. $P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$.
29. $P(A|B) = \frac{0.2}{0.4} = 0.50$.
30. $P(H|E) = \frac{P(E|H) P(H)}{P(E)}$.
31. $E[X] = 1(0.3) + 2(0.7) = 0.3 + 1.4 = 1.7$.
32. $E[X^2] = 1^2(0.3) + 2^2(0.7) = 0.3 + 2.8 = 3.1$. $\text{Var}(X) = 3.1 - 1.7^2 = 3.1 - 2.89 = 0.21$.
33. $E[X] = 0.8$, $\text{Var}(X) = 0.8(0.2) = 0.16$.
34. $\text{Var}(X+Y) = 4 + 9 = 13$.
35. $\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$.
36. $P(X_1, \dots, X_d | Y) = \prod P(X_i | Y)$.
37. $\hat{P}(X_i | c) = \frac{N_{c,i} + \alpha}{N_c + \alpha D}$.
38. $\bar{x} = \frac{2+4+6+8+10}{5} = \frac{30}{5} = 6.0$.
39. Devs: $-2, 0, +2$. $s^2 = \frac{4 + 0 + 4}{3-1} = \frac{8}{2} = 4.0$.
40. $Z = \frac{x - \mu}{\sigma}$.
41. $Z = \frac{65 - 50}{10} = +1.5$.
42. $95.45\%$.
43. $SE(\bar{X}) = \frac{s}{\sqrt{n}}$.
44. Sample mean $\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$ for $n \ge 30$.
45. $\bar{x} \pm 1.96 \frac{\sigma}{\sqrt{n}}$.
46. If $p \le \alpha \implies$ Reject $H_0$; if $p > \alpha \implies$ Fail to Reject $H_0$.
47. Rejecting $H_0$ when $H_0$ is true (False Positive).
48. Failing to reject $H_0$ when $H_0$ is false (False Negative).
49. $\text{Power} = 1 - \beta$.
50. $\chi^2 = \sum \frac{(O - E)^2}{E}$.
