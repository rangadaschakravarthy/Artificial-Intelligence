# Day 202 Theory: Statistical AI

### 1. What Is It?
Statistical AI is an approach to artificial intelligence that models real-world uncertainty using probability theory, Bayesian statistics, and stochastic graph models rather than rigid boolean logic.

### 2. Why Does It Exist?
The real world is filled with noisy sensor data, incomplete information, and ambiguity. Deterministic boolean logic ($1$ or $0$) breaks when data is noisy. Statistical AI represents beliefs as continuous probabilities $P(\text{State} \mid \text{Evidence}) \in [0, 1]$.

### 3. Core Mathematical Foundation: Bayes' Rule
$$P(H \mid E) = \frac{P(E \mid H) \cdot P(H)}{P(E)}$$
where $P(H \mid E)$ is the posterior probability of hypothesis $H$ given evidence $E$, $P(E \mid H)$ is the likelihood, and $P(H)$ is the prior.

### 4. Summary
Statistical AI handles real-world noise and ambiguity by modeling beliefs as continuous Bayesian probabilities.
