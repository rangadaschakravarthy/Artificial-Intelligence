# Solutions — Conditional Independence

## Level 1
1. $P(X, Y | Z) = P(X|Z) P(Y|Z)$ for all $x,y,z$.
2. $P(X_1, \dots, X_d | Y) = \prod_{i=1}^d P(X_i | Y)$.
3. False.
4. A node $Z$ where two or more arrowheads converge ($X ightarrow Z \leftarrow Y$).
5. Conditioning on a Collider (or its descendants) opens the path and CREATES dependence between its parents $X$ and $Y$.

## Level 2
6. $P(X=1, Y=1 | Z=1) = 0.3 	imes 0.7 = 0.21$.
7. $P(Y=0|Z=0) = 1 - 0.2 = 0.8$. $P(X=1, Y=0 | Z=0) = 0.1 	imes 0.8 = 0.08$.
8. Joint $= P(	ext{Spam}) P(X_1=1|	ext{Spam}) P(X_2=1|	ext{Spam}) = 0.3 	imes 0.9 	imes 0.8 = 0.216$.
9. $P(X_3 | X_2, X_1) = P(X_3 | X_2)$.
10. $10$ parameters (one per binary feature per class).

## Level 3
11. Proof: $P(X | Y, Z) = rac{P(X, Y, Z)}{P(Y, Z)} = rac{P(X, Y | Z) P(Z)}{P(Y | Z) P(Z)} = rac{P(X|Z) P(Y|Z)}{P(Y|Z)} = P(X|Z)$.
12. Two independent coin flips $X$ and $Y$. Let $Z = X + Y$. Given $Z=2$, knowing $X=1$ forces $Y=1$. They become dependent when conditioning on sum $Z$.
13. Stature $X$ and Vocabulary size $Y$ among children, conditionally independent given Age $Z$.
14. In $A ightarrow C \leftarrow B$, two independent causes $A$ and $B$ compete to explain effect $C$. Observing $C=1$ and confirming $A=1$ reduces belief in $B=1$ because $A$ explains away effect $C$.
15. By chain rule: $P(X,Y,Z) = P(Z) P(X|Z) P(Y|X,Z)$. Under $X \leftarrow Z ightarrow Y$, $P(Y|X,Z) = P(Y|Z) \implies P(X,Y,Z) = P(Z)P(X|Z)P(Y|Z)$.

## Level 4
16. $P(Y=1 | X_1, \dots, X_d) = rac{P(Y=1) \prod_{i=1}^d P(X_i | Y=1)}{\sum_{y \in \{0,1\}} P(Y=y) \prod_{i=1}^d P(X_i | Y=y)}$.
17. Because it makes the "naive" assumption that all input features are conditionally independent given the class, which is rarely true in real data.
18. Two parameters per feature per class: mean $\mu_{y,i}$ and variance $\sigma_{y,i}^2$.
19. "Not" and "bad" are strongly correlated in context; treating them as conditionally independent counts negative sentiment twice, distorting probability scores.
20. 1) Current state $S_t$ depends ONLY on previous state $S_{t-1}$ ($S_t \perp \!\!\! \perp S_{1:t-2} \mid S_{t-1}$). 2) Observation $O_t$ depends ONLY on current state $S_t$ ($O_t \perp \!\!\! \perp 	ext{others} \mid S_t$).

## Level 5
21. 1) Chain $X ightarrow Z ightarrow Y$: Blocked if $Z$ is observed. 2) Common Cause $X \leftarrow Z ightarrow Y$: Blocked if $Z$ is observed. 3) Collider $X ightarrow Z \leftarrow Y$: Blocked if $Z$ (and its descendants) is NOT observed; active if observed.
22. Duplicate/correlated features effectively re-multiply the same likelihood ratio multiple times, exponentially inflating class posterior confidence toward 0 or 1.
23. `log_prior = np.log(priors); log_lik = np.sum(np.log(likelihoods), axis=1); log_post = log_prior + log_lik`.
