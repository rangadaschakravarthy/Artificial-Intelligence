# Solutions — Bayes' Theorem

## Level 1
1. $P(A|B) = rac{P(B|A)P(A)}{P(B)}$.
2. Prior $P(A)$, Likelihood $P(B|A)$, Posterior $P(A|B)$, Evidence $P(B)$.
3. To compute the denominator (Evidence) by summing across all mutually exclusive hypotheses: $P(E) = \sum P(E|H_i) P(H_i)$.
4. Likelihood $P(E|H)$ is the probability of observing the evidence $E$ assuming hypothesis $H$ is true.
5. If $P(E)=1$, Posterior equals $	ext{Likelihood} 	imes 	ext{Prior} = P(E|H) P(H) = P(H)$.

## Level 2
6. $P(A|B) = rac{(0.8)(0.3)}{0.4} = rac{0.24}{0.4} = 0.60$.
7. Denominator $P(E) = (0.9)(0.5) + (0.1)(0.5) = 0.45 + 0.05 = 0.50$. $P(H|E) = rac{0.45}{0.50} = 0.90$.
8. Numerator: $(0.50)(0.20) = 0.10$. Denominator: $0.10 + (0.05)(0.80) = 0.10 + 0.04 = 0.14$. $P(	ext{Spam}|	ext{Word}) = rac{0.10}{0.14} = rac{5}{7} pprox 0.7143$.
9. $P(X) = 0.10, P(+|X) = 0.90, P(+|X^c) = 0.10$. $P(+) = (0.90)(0.10) + (0.10)(0.90) = 0.09 + 0.09 = 0.18$. $P(X|+) = rac{0.09}{0.18} = 0.50 = 50\%$.
10. $P(-|X^c) = 0.90, P(-|X) = 0.10$. $P(-) = (0.90)(0.90) + (0.10)(0.10) = 0.81 + 0.01 = 0.82$. NPV $= P(X^c|-) = rac{0.81}{0.82} pprox 0.9878 = 98.78\%$.

## Level 3
11. By definition, $P(A|B) = rac{P(A \cap B)}{P(B)}$ and $P(B|A) = rac{P(A \cap B)}{P(A)} \implies P(A \cap B) = P(B|A)P(A)$. Substituting into the first equation yields $P(A|B) = rac{P(B|A)P(A)}{P(B)}$.
12. Base Rate Fallacy: When prevalence $P(H)$ is very small (e.g. 0.0001), even a highly accurate test (e.g. 99% accuracy) produces far more false positives than true positives, making $P(H|E) < 1\%$ despite $99\%$ test accuracy.
13. $P(E) = (0.01)(0.50) + (0.02)(0.30) + (0.05)(0.20) = 0.005 + 0.006 + 0.010 = 0.021$. $P(F_3|E) = rac{0.010}{0.021} = rac{10}{21} pprox 0.4762$.
14. Divide $P(H|E) = rac{P(E|H)P(H)}{P(E)}$ by $P(H^c|E) = rac{P(E|H^c)P(H^c)}{P(E)}$. The denominator $P(E)$ cancels out: $rac{P(H|E)}{P(H^c|E)} = rac{P(H)}{P(H^c)} 	imes rac{P(E|H)}{P(E|H^c)}$.
15. Prior Odds $= rac{0.01}{0.99} pprox 0.010101$. Posterior Odds $= 0.010101 	imes 100 = 1.0101$. Posterior $P(H|E) = rac{1.0101}{1 + 1.0101} pprox 0.5025 = 50.25\%$.

## Level 4
16. $P(	ext{Fraud}) = 0.002, P(	ext{Legit}) = 0.998$. $P(	ext{High}) = (0.80)(0.002) + (0.05)(0.998) = 0.0016 + 0.0499 = 0.0515$. $P(	ext{Fraud}|	ext{High}) = rac{0.0016}{0.0515} pprox 0.03107 = 3.11\%$.
17. $P(Y=1|X_1, X_2) = rac{P(X_1|Y=1) P(X_2|Y=1) P(Y=1)}{P(X_1, X_2)}$.
18. $P(	ext{Shape}) = (0.90)(0.05) + (0.10)(0.95) = 0.045 + 0.095 = 0.140$. $P(	ext{Pedestrian}|	ext{Shape}) = rac{0.045}{0.140} = rac{9}{28} pprox 0.3214$.
19. MLE maximizes Likelihood $P(X|	heta)$ without considering prior beliefs. MAP maximizes Posterior $P(	heta|X) \propto P(X|	heta)P(	heta)$, combining likelihood with prior probability over parameters.
20. When prior $P(	heta)$ is uniform (flat / constant), MAP estimation becomes mathematically identical to MLE estimation.

## Level 5
21. $\hat{y} = rg\max_y P(Y=y|X) = rg\max_y rac{P(X|Y=y)P(Y=y)}{P(X)}$. Since denominator $P(X)$ is constant across all candidate classes $y$, we simplify to $rg\max_y P(Y=y) \prod_i P(X_i|Y=y)$ under feature independence.
22. In MAP classification, $P(E)$ is constant for all evaluated class hypotheses $y$. Thus, comparing numerators $P(E|y)P(y)$ is sufficient to find the maximum class without computing $P(E)$.
23. Sequential updating uses today's Posterior $P(H|E_1)$ directly as tomorrow's Prior for new incoming evidence $E_2$. This allows continuous online learning without retraining on historical data from scratch.
