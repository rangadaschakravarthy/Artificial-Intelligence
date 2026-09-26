# Day 176 Theory: Rational Agents

### 1. What Is It?
A Rational Agent is an agent that selects an action expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent possesses.

### 2. Mathematical Definition of Rationality
For an agent with percept history $P^*$, built-in knowledge $K$, and action space $A$, the rational action $a^*$ satisfies:
$$a^* = rg\max_{a \in A} \mathbb{E}\left[ U(	ext{Outcome}(a)) \mid P^*, K ight]$$
where $\mathbb{E}[U(\cdot)]$ is the expected utility of the resulting environment state.

### 3. The 4 Factors Determining Rationality
1. The **Performance Measure** defining the criterion of success.
2. The agent's **Prior Knowledge** of the environment.
3. The **Actions** that the agent can perform.
4. The agent's **Percept Sequence** to date.

### 4. Rationality vs Omniscience
- An **Omniscient Agent** knows the actual outcome of its actions and can act accordingly (requires predicting the future with 100% certainty, which is physically impossible).
- A **Rational Agent** maximizes *expected* performance based on current information. A rational decision can lead to a bad outcome if unforeseen stochastic events occur, but the decision remains rational.

### 5. Bounded Rationality
Introduced by Herbert Simon, **Bounded Rationality** acknowledges that real-world agents have limited computational memory and processing time. Rather than computing global optima in complex environments, agents seek "satisficing" decisions that meet acceptable utility thresholds.

### 6. Summary
Rationality is expected utility maximization based on available information, bounded by computational constraints.
