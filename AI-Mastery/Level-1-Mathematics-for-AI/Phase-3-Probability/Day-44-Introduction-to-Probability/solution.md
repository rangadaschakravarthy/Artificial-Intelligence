# Solutions — Introduction to Probability

## Level 1
1. Range is $[0, 1]$ or $0 \le P(A) \le 1$.
2. $P(A^c) = 1 - 0.35 = 0.65$.
3. Unitarity Axiom: $P(\Omega) = 1$.
4. False. Empirical probability converges to theoretical probability only as sample size $N \to \infty$ (Law of Large Numbers).
5. $\Omega = \{HH, HT, TH, TT\}$.

## Level 2
6. Favorable outcomes: $\{5, 6\} \implies |A|=2$. $P = \frac{2}{6} = \frac{1}{3} pprox 0.3333$.
7. $P = \frac{18}{30} = 0.60$.
8. Total marbles = $5+3+2 = 10$. $P(	ext{Red}) = \frac{5}{10} = 0.50$.
9. Primes in 1-10: $\{2, 3, 5, 7\} \implies |A|=4$. $P = \frac{4}{10} = 0.40$.
10. Empirical $P(	ext{Heads}) = \frac{100 - 70}{100} = \frac{30}{100} = 0.30$.

## Level 3
11. Law of Large Numbers states that as trial count $n \to \infty$, relative frequency $\frac{k}{n}$ converges almost surely to theoretical probability $P(A)$.
12. For mutually exclusive events: $P(A \cup B) = P(A) + P(B) = 0.4 + 0.3 = 0.7$.
13. Proof: $B = A \cup (B \setminus A)$ where $A$ and $(B \setminus A)$ are disjoint. By Axiom 3, $P(B) = P(A) + P(B \setminus A)$. Since Axiom 1 gives $P(B \setminus A) \ge 0$, $P(B) \ge P(A)$.
14. Odds = $\frac{P(	ext{Rain})}{P(	ext{No Rain})} = \frac{0.7}{0.3} = \frac{7}{3}$ or $7:3$.
15. $P(	ext{Failure}) = P(C_1 \cup C_2) = P(C_1) + P(C_2) = 0.02 + 0.03 = 0.05$.

## Level 4
16. Logits $z = [3.0, 1.0, 0.0]$. $e^z = [e^3, e^1, e^0] pprox [20.0855, 2.7183, 1.0]$. Sum $= 23.8038$. Softmax$(z_1) = \frac{20.0855}{23.8038} pprox 0.8438$.
17. Expected spam emails $= 100 	imes 0.90 = 90$.
18. Cross-Entropy loss relies on log-likelihood $\log P(Y|X)$. Outputs must be valid probabilities ($[0,1]$ summing to 1) for the logarithm to be mathematically defined.
19. Loss $= -\ln(0.85) pprox 0.1625$.
20. Expected conversions $= 1000(0.12) + 1000(0.15) = 120 + 150 = 270$.

## Level 5
21. Frequentist views probability as long-run limiting frequency of repeatable events. Bayesian views probability as a measure of belief or degree of certainty given current evidence.
22. $\Omega = A \cup A^c$, where $A$ and $A^c$ are disjoint. By Axiom 2, $P(\Omega) = 1$. By Axiom 3, $P(A \cup A^c) = P(A) + P(A^c) = 1 \implies P(A^c) = 1 - P(A)$.
23. Softmax handles negative logits, amplifies larger differences (via exponential function), and creates a differentiable probability distribution summing to 1.
