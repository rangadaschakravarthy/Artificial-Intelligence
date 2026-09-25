# Solutions — Conditional Probability

## Level 1
1. $P(A|B) = rac{P(A \cap B)}{P(B)}$.
2. $P(B) > 0$.
3. $P(A|B) = 0$ since $P(A \cap B) = 0$.
4. $P(A|B) = 1$ since $A \cap B = B \implies rac{P(B)}{P(B)} = 1$.
5. $P(A|B) = rac{0.12}{0.40} = 0.30$.

## Level 2
6. $B = \{3, 4, 5, 6\} \implies P(B) = 4/6$. $A = 	ext{Even} = \{2, 4, 6\}$. $A \cap B = \{4, 6\} \implies P(A \cap B) = 2/6$. $P(A|B) = rac{2/6}{4/6} = 0.50$.
7. $P(	ext{Black}) = 26/52 = 0.5$. $P(	ext{Black Ace}) = 2/52$. $P(	ext{Ace}|	ext{Black}) = rac{2/52}{26/52} = rac{2}{26} = rac{1}{13} pprox 0.0769$.
8. $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.6 - 0.8 = 0.3$. $P(A|B) = rac{0.3}{0.6} = 0.50$.
9. $P(B|A) = rac{P(A \cap B)}{P(A)} = rac{0.3}{0.5} = 0.60$.
10. After drawing 1 red chip, 3 red and 6 blue remain (9 total). $P(R_2 | R_1) = rac{3}{9} = rac{1}{3} pprox 0.3333$.

## Level 3
11. Proof: $P(A) \cdot P(B|A) = P(A \cap B)$. Then $P(A \cap B) \cdot P(C | A \cap B) = P((A \cap B) \cap C) = P(A \cap B \cap C)$.
12. Event $B$ increases the likelihood of event $A$ (positively correlated / dependent).
13. $P(	ext{Physics} | 	ext{Math}) = rac{P(	ext{Math} \cap 	ext{Physics})}{P(	ext{Math})} = rac{0.30}{0.60} = 0.50$.
14. $P(	ext{Math} | 	ext{Physics}^c) = rac{P(	ext{Math} \cap 	ext{Physics}^c)}{P(	ext{Physics}^c)} = rac{P(	ext{Math}) - P(	ext{Math} \cap 	ext{Physics})}{1 - P(	ext{Physics})} = rac{0.60 - 0.30}{1 - 0.50} = rac{0.30}{0.50} = 0.60$.
15. $P(A^c | B) = rac{P(A^c \cap B)}{P(B)} = rac{P(B) - P(A \cap B)}{P(B)} = 1 - rac{P(A \cap B)}{P(B)} = 1 - P(A|B)$.

## Level 4
16. Precision $= rac{TP}{TP + FP} = rac{150}{150 + 50} = rac{150}{200} = 0.75$.
17. Recall $= rac{TP}{TP + FN} = rac{150}{150 + 25} = rac{150}{175} pprox 0.8571$.
18. Specificity $= rac{TN}{TN + FP} = rac{775}{775 + 50} = rac{775}{825} pprox 0.9394$.
19. Expected detections $= 100 	imes 0.98 = 98$ pedestrians.
20. In rare disease or fraud detection ($P(Y=1) = 0.001$), a dummy model predicting $\hat{Y}=0$ always achieves $99.9\%$ accuracy, but has Recall $= 0$ ($P(\hat{Y}=1 | Y=1) = 0$). Precision/Recall metrics are required.

## Level 5
21. Transposition Fallacy is assuming $P(A|B) = P(B|A)$. In AI: Confusing $P(	ext{Fraud} \mid 	ext{Alert}) = 0.95$ with $P(	ext{Alert} \mid 	ext{Fraud}) = 0.95$. If alerts trigger frequently on clean data, $P(	ext{Fraud} \mid 	ext{Alert})$ can actually be very low.
22. $P(X_1, X_2, \dots, X_n) = P(X_1) P(X_2|X_1) P(X_3|X_1, X_2) \dots P(X_n | X_1, \dots, X_{n-1})$. Proven by induction on conditional definition.
23. GPT generates text token $w_t$ sequentially by computing conditional probability distribution $P(w_t \mid w_1, w_2, \dots, w_{t-1})$ over vocabulary using Softmax logits conditioned on prior context tokens.
