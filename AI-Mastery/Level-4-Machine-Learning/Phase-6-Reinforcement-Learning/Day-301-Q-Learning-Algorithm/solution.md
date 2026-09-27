# Practice Solutions — Day 301

## Basic Solutions
1. Q-Learning Algorithm establishes feedback systems (rewards, pretext signals, pseudo-labels) for model training.
2. MDP 5-tuple: State space $S$, Action space $A$, Transition probability $P$, Reward function $R$, Discount factor $\gamma$.
3. $Q(s, a)$ is the expected cumulative return of taking action $a$ in state $s$ and thereafter following policy $\pi$.

## Conceptual Solutions
4. $\gamma$ ensures mathematical convergence of infinite horizon sums and models preference for immediate over delayed rewards.
5. Exploitation uses current best-known actions to maximize immediate reward; Exploration tries new actions to discover potentially better long-term strategies.
6. Semi-supervised uses a small human-labeled set + unlabeled data; Self-supervised creates its own supervision signal directly from unlabeled data via pretext tasks.

## Calculation Solutions
7. $G_0 = 5 + 0.8(-1) + (0.8)^2(20) = 5 - 0.8 + 0.64(20) = 4.2 + 12.8 = 17.0$.
8. $\text{TD Target} = 5 + 0.9(4.0) = 5 + 3.6 = 8.6$. $\text{TD Error} = 8.6 - 1.0 = 7.6$. New $Q(s,a) = 1.0 + 0.2(7.6) = 1.0 + 1.52 = 2.52$.

## Implementation Solutions
```python
import numpy as np

# 9. Epsilon-Greedy Action Selection
def select_action(q_values, epsilon, n_actions):
    if np.random.rand() < epsilon:
        return np.random.randint(n_actions) # Explore
    else:
        return np.argmax(q_values) # Exploit

# 10. Q-Update Test
q_val = 1.0
alpha, gamma, r, max_q_next = 0.2, 0.9, 5.0, 4.0
new_q = q_val + alpha * (r + gamma * max_q_next - q_val)
print("Updated Q-value:", new_q)
```

## ML Reasoning Solutions
11. Add dense intermediate rewards (reward shaping) for steps that move closer to the goal destination.
12. Confirmation bias: Incorrect pseudo-labels get added to training set with high confidence, reinforcing original model errors.

## Dataset Questions
13. State: portfolio holdings, cash balance, stock price history; Action: Buy, Sell, Hold; Reward: net portfolio profit/loss.

## Interview Solutions
14. $Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$. $Q(s,a)$ is current estimate, $\alpha$ is learning rate, $r$ is immediate reward, $\gamma$ is discount factor, $\max_{a'} Q(s',a')$ is best future value estimate.
15. Markov Property: $P(S_{t+1} \mid S_t, A_t, S_{t-1}, A_{t-1}, \dots) = P(S_{t+1} \mid S_t, A_t)$. Future state depends ONLY on current state and action, not historical trajectory.
