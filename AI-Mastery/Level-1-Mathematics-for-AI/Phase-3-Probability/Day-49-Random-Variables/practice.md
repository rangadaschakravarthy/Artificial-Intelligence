# Practice Problems — Random Variables

## Level 1: Basic Concept Checks
1. Formally define a random variable $X$.
2. Explain the difference in notation between $X$ and $x$.
3. Classify: Number of support tickets per day (Discrete or Continuous?).
4. Classify: Exact height of a candidate in centimeters (Discrete or Continuous?).
5. What is the support $S_X$ of a fair 6-sided die roll $X$?

## Level 2: Direct Calculations
6. Flip 2 fair coins. Let $X = 	ext{Number of Tails}$. Find $P(X=1)$.
7. Let $X$ be the sum of 2 fair 6-sided dice. Compute $P(X=4)$.
8. In Q7, compute $P(X \ge 10)$.
9. Let $Y = 2X + 1$. If $X$ takes values $\{1, 2, 3\}$, list the possible values of $Y$.
10. A computer draws a random integer $Z$ uniformly from $\{1, 2, 3, 4, 5\}$. Find $P(Z 	ext{ is even})$.

## Level 3: Conceptual & Multi-Step Problems
11. Show that the expectation of an indicator variable $I_A$ equals $P(A)$.
12. Let $X$ be number of flips until first Heads with fair coin. List the support of $X$. Is it finite or countably infinite?
13. If $X$ is a discrete random variable with $P(X=x) = k x$ for $x \in \{1, 2, 3, 4\}$, find constant $k$.
14. Using $k$ from Q13, compute $P(X > 2)$.
15. Explain why a continuous random variable has $P(X = x) = 0$ for any single exact point $x$.

## Level 4: AI & ML Applications
16. In object detection, let $N$ be the number of detected objects in an image. Classify $N$ and state its support.
17. In linear regression $Y = w X + b + \epsilon$, identify which terms are fixed parameters and which are random variables.
18. In multi-class classification with 5 classes, express class target label $Y$ as a random variable.
19. Convert $Y \in \{1, 2, 3\}$ into a One-Hot encoded random vector $\mathbf{Y}$.
20. In reinforcement learning, reward $R_t$ at step $t$ is a random variable. Why is $R_t$ stochastic?

## Level 5: Interview Questions
21. What is the difference between a random variable and a random process (stochastic process)?
22. Define a measurable space $(\Omega, \mathcal{F})$ and explain measure-theoretic necessity of random variables.
23. How do generative AI models (VAEs, GANs) sample from latent random variables $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$?
