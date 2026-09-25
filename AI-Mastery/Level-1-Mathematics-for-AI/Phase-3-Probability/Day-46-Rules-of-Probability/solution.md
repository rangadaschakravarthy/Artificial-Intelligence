# Solutions — Rules of Probability

## Level 1
1. $P(A \cup B) = P(A) + P(B)$.
2. $P(A^c) = 1 - 0.42 = 0.58$.
3. $P(A \cap B) = P(A) 	imes P(B)$.
4. False. $P(A \cup B) = P(A) + P(B) - P(A \cap B) \le P(A) + P(B)$.
5. $P(A \cap B) = P(A) \cdot P(B|A)$.

## Level 2
6. $P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$.
7. $P(A \cup B) = 0.7 + 0.3 = 1.0$.
8. $P(	ext{At least 1 H}) = 1 - P(	ext{TTT}) = 1 - (0.5)^3 = 1 - 0.125 = 0.875$.
9. With replacement: $rac{4}{52} 	imes rac{4}{52} = \left(rac{1}{13}ight)^2 = rac{1}{169} pprox 0.0059$.
10. Without replacement: $rac{4}{52} 	imes rac{3}{51} = rac{1}{13} 	imes rac{1}{17} = rac{1}{221} pprox 0.0045$.

## Level 3
11. $P(A \cup B) = P(A) + P(B) - P(A \cap B) \le 1 \implies P(A) + P(B) - 1 \le P(A \cap B)$.
12. $P(	ext{All work}) = (1 - 0.05)^4 = 0.95^4 pprox 0.8145$.
13. Min $P(A \cap B) = 0.6 + 0.5 - 1.0 = 0.10$.
14. Max $P(A \cap B) = \min(P(A), P(B)) = 0.50$.
15. By De Morgan's Law, $P(A^c \cap B^c) = P((A \cup B)^c) = 1 - P(A \cup B) = 0.2 \implies P(A \cup B) = 0.8$.

## Level 4
16. Pipeline Uptime $= 0.99 	imes 0.98 	imes 0.95 = 0.92169 pprox 92.17\%$.
17. Binomial distribution $n=5, p=0.10$. $P(X \ge 3) = inom{5}{3}(0.1)^3(0.9)^2 + inom{5}{4}(0.1)^4(0.9)^1 + inom{5}{5}(0.1)^5 = 10(0.001)(0.81) + 5(0.0001)(0.9) + 1(0.00001) = 0.0081 + 0.00045 + 0.00001 = 0.00856$.
18. $P(	ext{Click AND Buy}) = P(	ext{Click}) 	imes P(	ext{Buy}|	ext{Click}) = 0.10 	imes 0.25 = 0.025$.
19. $P(	ext{System Up}) = 1 - P(	ext{Both Down}) = 1 - (1 - 0.99)^2 = 1 - 0.01^2 = 1 - 0.0001 = 0.9999$.
20. $P(	ext{At least 1 spam}) = 1 - (1 - 0.20)^5 = 1 - (0.8)^5 = 1 - 0.32768 = 0.67232 pprox 67.23\%$.

## Level 5
21. Start with $P(A \cup B) \le 1$. Since $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, we substitute: $P(A) + P(B) - P(A \cap B) \le 1 \implies P(A \cap B) \ge P(A) + P(B) - 1$.
22. Condorcet's Jury Theorem states that if each independent voter/model has probability $p > 0.5$ of being correct, adding more voters increases the probability that majority vote is correct toward 1. This is the theoretical basis for Ensemble Machine Learning.
23. Drawing with replacement restores original population probabilities for subsequent draws (independent). Drawing without replacement changes population size and composition, altering conditional probabilities for future draws (dependent).
