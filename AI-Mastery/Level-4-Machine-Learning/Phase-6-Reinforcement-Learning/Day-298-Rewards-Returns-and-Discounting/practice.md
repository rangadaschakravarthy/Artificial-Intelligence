# Practice Questions — Day 298

## Basic Questions
1. Define Rewards, Returns & Discounting.
2. What are the 5 components of a Markov Decision Process (MDP)?
3. Define the Q-value $Q(s, a)$.

## Conceptual Questions
4. Why is the discount factor $\gamma \in [0, 1)$ necessary in reinforcement learning?
5. Explain the Exploration vs Exploitation trade-off.
6. Contrast Semi-Supervised Learning with Self-Supervised Learning.

## Calculation Questions
7. Compute cumulative return $G_0 = \sum_{k=0}^2 \gamma^k r_{k+1}$ for rewards $[5, -1, 20]$ with $\gamma = 0.8$.
8. Perform a Q-learning update for $Q(s,a)=1.0, \alpha=0.2, \gamma=0.9, r=5, \max_{a'} Q(s',a')=4.0$.

## Implementation Questions
9. Write a Python function implementing $\epsilon$-greedy action selection.
10. Build a scratch 2D GridWorld Q-learning environment in Python.

## ML Reasoning Questions
11. An RL agent immediately drops into a pit because all immediate rewards are 0 except death (-100). How can reward shaping fix this?
12. Why does Pseudo-Labeling risk propagating errors if the initial model has low precision?

## Dataset Questions
13. Formulate state, action, and reward representation for automated stock trading.

## Interview Questions
14. Write the Q-Learning Bellman update equation and explain every symbol.
15. What is the Markov Property, and why is it essential for MDP formulations?
