# Theory — Day 298: Rewards, Returns & Discounting

### 6.1 Definition
Rewards, Returns & Discounting is a vital advanced branch of Machine Learning. Immediate rewards $r_t$, cumulative return $G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}$, discount factor $\gamma \in [0, 1)$, and horizon modeling.

### 6.2 Intuition
Think of this as learning through interaction and trial-and-error: An agent explores an environment, takes actions, observes consequences (state transitions), and receives numerical feedback (rewards or penalties) to learn an optimal strategy (policy).

### 6.3 Why It Exists
Static datasets cannot model dynamic sequential decision-making environments (e.g., game playing, robotics navigation, autonomous driving, resource allocation). RL provides a framework for sequential optimization over time.

### 6.4 Real-World Analogy
Training a pet dog: When the dog sits on command (Action), you give a treat (Positive Reward). When it jumps on furniture, you say "No" (Negative Penalty). Over time, the dog learns a behavioral policy that maximizes treats.

### 6.5 Formal Definition
An MDP is formally defined by the tuple $\langle S, A, P, R, \gamma \rangle$:
- $S$: State space.
- $A$: Action space.
- $P(s' \mid s, a) = \mathbb{P}(S_{t+1} = s' \mid S_t = s, A_t = a)$: Transition probability.
- $R(s, a, s')$: Reward function.
- $\gamma \in [0, 1)$: Discount factor.

### 6.6 Mathematical Representation
- **Cumulative Discounted Return**:
  

$$
G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
$$

- **Bellman Expectation Equation for $Q^\pi(s, a)$**:
  

$$
Q^\pi(s, a) = \mathbb{E}_\pi \left[ R_{t+1} + \gamma Q^\pi(S_{t+1}, A_{t+1}) \mid S_t = s, A_t = a \right]
$$

- **Q-Learning Update Rule (TD Control)**:
  

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

### 6.7 Worked Example
Trace a single Q-learning update step:
- $Q(s, a) = 0.5$, $\alpha = 0.1$, $\gamma = 0.9$, $r = 10$, $s' = \text{next\_state}$.
- $\max_{a'} Q(s', a') = 2.0$.
- $\text{TD Target} = 10 + 0.9(2.0) = 11.8$.
- $\text{TD Error} = 11.8 - 0.5 = 11.3$.
- New $Q(s, a) = 0.5 + 0.1(11.3) = 1.63$.

### 6.8 ML Example
Training a GridWorld agent to navigate from $(0,0)$ to goal $(3,3)$ while avoiding traps.

### 6.9 Python Example
Scratch Q-Table environment and update loop.

### 6.10 scikit-learn / RL Library Connection
Connecting tabular Q-learning to Deep Q-Networks (DQN) and Gymnasium environments.

### 6.11 Common Mistakes
- Setting discount factor $\gamma = 1.0$ in infinite-horizon non-terminal tasks (causes infinite returns!).
- Setting exploration rate $\epsilon = 0$ too early, causing the agent to get trapped in sub-optimal local policies.

### 6.12 Strengths
Requires no explicit supervisor/labels; learns optimal sequential decision-making strategies directly from environment interaction.

### 6.13 Weaknesses
Sample inefficient (requires millions of trial steps); credit assignment problem; sensitive to reward function design.

### 6.14 Real-World Applications
Game AI (AlphaGo, OpenAI Five), Robotics locomotion, RLHF for Large Language Models (ChatGPT alignment), automated HVAC control.

### 6.15 Interview Insight
Be ready to derive the Bellman Optimality Equation and explain why $\epsilon$-greedy exploration prevents premature policy convergence.

### 6.16 Summary
Rewards, Returns & Discounting equips agents with decision-making policies optimized via environment interaction, rewards, and Bellman temporal difference updates.
