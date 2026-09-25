# Practice Problems — Independence

## Level 1: Basic Concept Checks
1. State the definition of independent random variables in terms of joint distribution $f(x,y)$.
2. If $X \perp \!\!\! \perp Y$, what is $P(X|Y)$?
3. What is $	ext{Cov}(X, Y)$ if $X$ and $Y$ are independent?
4. What does the acronym i.i.d. stand for?
5. True or False: If $	ext{Cov}(X, Y) = 0$, $X$ and $Y$ are guaranteed to be independent.

## Level 2: Direct Calculations
6. Independent $X, Y$ have $E[X] = 2, E[Y] = 7$. Find $E[XY]$.
7. Independent $X, Y$ have $	ext{Var}(X) = 5, 	ext{Var}(Y) = 8$. Find $	ext{Var}(X - Y)$.
8. If $X \sim 	ext{Bern}(0.4)$ and $Y \sim 	ext{Bern}(0.5)$ are independent, find $P(X=1, Y=1)$.
9. Continuous PDF $f(x, y) = c (x + y)$ on $[0, 1] 	imes [0, 1]$. Are $X$ and $Y$ independent?
10. If $X, Y, Z$ are i.i.d. with mean $\mu=3$, find $E[X + 2Y - Z]$.

## Level 3: Conceptual & Multi-Step Problems
11. Prove that if $X$ and $Y$ are independent, $E[XY] = E[X] E[Y]$ for continuous random variables.
12. Prove that if $X$ and $Y$ are independent, $	ext{Var}(X + Y) = 	ext{Var}(X) + 	ext{Var}(Y)$.
13. If $X$ and $Y$ are independent, prove that any functions $g(X)$ and $h(Y)$ are also independent.
14. Show that two events $A$ and $B$ are independent if and only if their indicator variables $I_A$ and $I_B$ are independent random variables.
15. If $X$ and $Y$ are Jointly Gaussian and $	ext{Cov}(X, Y) = 0$, prove that $X$ and $Y$ are independent.

## Level 4: AI & ML Applications
16. In Naive Bayes classification, features $X_1, X_2$ are assumed conditionally independent given $Y$. Write $P(X_1, X_2 | Y)$.
17. Explain why time series stock data violates the i.i.d. assumption.
18. In training neural networks, why do we shuffle dataset rows at each epoch?
19. Given i.i.d. samples $x_1, \dots, x_N \sim \mathcal{N}(\mu, \sigma^2)$, write the total log-likelihood $\ln L(\mu, \sigma^2)$.
20. In reinforcement learning, how does an Experience Replay Buffer help break temporal correlations between successive transitions?

## Level 5: Interview Questions
21. Give a formal proof that Independence implies Zero Covariance.
22. Explain why Joint Gaussianity is a necessary condition for Zero Covariance to guarantee Independence.
23. Write Python code using SciPy `scipy.stats.chi2_contingency` to test independence of two categorical features in a Pandas DataFrame.
