# Examples — Day 297: Reinforcement Learning Basics

## Example 1 — Extremely Simple
GridWorld 2x2 movement: Agent moves Right $\implies$ Reward $+1$, State changes to Goal.

## Example 2 — Basic Numerical Calculation
Calculating Discounted Return $G_0$ for sequence of rewards $r_1=0, r_2=0, r_3=100$ with $\gamma = 0.9$:

$$
G_0 = 0 + 0.9(0) + (0.9)^2(100) = 0 + 0 + 81 = 81.0
$$

## Example 3 — Real Dataset / Environment Example (CartPole / GridWorld)
State $s = [\text{position}, \text{velocity}, \text{angle}, \text{angular\_velocity}]$; Actions $a \in \{\text{Left}, \text{Right}\}$; Reward $+1$ per timestep pole remains upright.

## Example 4 — Machine Learning Pipeline Example
Pseudo-labeling pipeline: Train initial classifier on 500 labeled samples $\to$ Predict pseudo-labels for 10,000 unlabeled samples $\to$ Re-train on combined dataset.

## Example 5 — Real-World Scenario (LLM RLHF)
RLHF alignment: LLM generates 2 responses $\to$ Reward model assigns score $\to$ PPO policy updates LLM weights to favor helpful responses.

## Example 6 — Interview-Style Example
Explaining why Self-Supervised masked language modeling (e.g. BERT/GPT) learns general representations that outperform supervised models pre-trained on narrow labeled tasks.
