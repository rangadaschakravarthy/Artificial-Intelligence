# Solutions — Sample Spaces and Events

## Level 1
1. Set of all possible outcomes of a random experiment.
2. Intersection ($A \cap B$).
3. $A^c = \Omega \setminus A$.
4. $A$ and $B$ are mutually exclusive (disjoint).
5. Continuous.

## Level 2
6. $\Omega = \{(1,1), (1,2), \dots, (4,4)\}$ total $4 	imes 4 = 16$ pairs.
7. $A \cap B = \{6, 8, 10\}$.
8. $A \cup B = \{2, 4, 6, 7, 8, 9, 10\}$.
9. $A \setminus B = \{2, 4\}$.
10. $|A \cup B| = 15 + 10 - 4 = 21$.

## Level 3
11. Proof: $x \in (A \cup B)^c \iff x 
otin (A \cup B) \iff (x 
otin A 	ext{ and } x 
otin B) \iff (x \in A^c 	ext{ and } x \in B^c) \iff x \in A^c \cap B^c$.
12. $\Omega = \{(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)\}$.
13. $E = \{(0,1,1), (1,0,1), (1,1,0), (1,1,1)\}$.
14. $A \cup B = A \cup (B \setminus A)$ where $A$ and $(B \setminus A)$ are disjoint. $P(A \cup B) = P(A) + P(B \setminus A)$. Since $B = (A \cap B) \cup (B \setminus A)$ disjointly, $P(B) = P(A \cap B) + P(B \setminus A) \implies P(B \setminus A) = P(B) - P(A \cap B)$. Substituting gives $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
15. 1) Mutually exclusive: $A_i \cap A_j = \emptyset$ for $i 
\neq j$. 2) Collectively exhaustive: $igcup_{i} A_i = \Omega$.

## Level 4
16. $|A \cup B| = 50 + 50 - 25 = 75$. $	ext{IoU} = \frac{25}{75} = \frac{1}{3} pprox 0.3333$.
17. No, because $0.3333 < 0.50$.
18. $E = \{	ext{Pos}, 	ext{Neu}\} = \Omega \setminus \{	ext{Neg}\}$.
19. Softmax assumes mutually exclusive events ($\sum P_i = 1$). In multi-label classification, multiple labels can co-occur, so independent binary sigmoids are used for each label set event.
20. $A \cup B$.

## Level 5
21. IoU is mathematically identical to the Jaccard similarity coefficient $J(A, B) = \frac{|A \cap B|}{|A \cup B|}$, measuring set similarity between ground truth bounding box set $A$ and predicted set $B$.
22. A collection $\mathcal{F}$ of subsets of $\Omega$ satisfying: 1) $\Omega \in \mathcal{F}$, 2) Closed under complementation ($A \in \mathcal{F} \implies A^c \in \mathcal{F}$), 3) Closed under countable unions.
23. For continuous variables, probability is density integrated over area. Single point width is zero $\int_x^x f(t)dt = 0$, but interval width $> 0$ yields positive integral area.
