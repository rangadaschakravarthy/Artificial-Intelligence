# Theory — Day 210: AI Problem Solving Foundations

## 1. What Is It?
AI Problem Solving is the study of how rational agents formulate, structure, and compute solutions to goal-oriented tasks using abstract formal representations.

## 2. Why Does It Exist?
Real-world environments are continuous, noisy, and infinitely complex. Problem-solving abstractions collapse physical complexity into discrete state graphs that computational algorithms can process systematically.

## 3. Intuition
Imagine navigating a dense forest. Instead of recording every individual leaf and pebble, you map key locations (intersections) and available paths (trails). Problem solving in AI reduces raw sensor inputs into a map of discrete choices.

## 4. Syntax / Notation
A well-defined AI problem is formally specified by a 6-tuple:
$$\mathcal{P} = \langle S, s_0, A, T, G, c \rangle$$
- $S$: State space (set of all valid states).
- $s_0 \in S$: Initial state.
- $A(s)$: Action space (valid actions available in state $s$).
- $T(s, a) \to s'$: Transition function producing successor state $s'$.
- $G(s) \to \{True, False\}$: Goal test function.
- $c(s, a, s')$: Step cost function (cost of taking action $a$ from state $s$ to state $s'$).

## 5. Parameters / Environment
- **Determinism**: Deterministic vs Stochastic transition models.
- **Observability**: Fully observable vs Partially observable environments.
- **Continuity**: Discrete vs Continuous state spaces.

## 6. How It Works
1. **Goal Formulation**: Set the objective criterion based on agent performance metrics.
2. **Problem Formulation**: Decide what states and actions to include in the 6-tuple model.
3. **Search Execution**: Execute search or reasoning algorithms over the state space.
4. **Action Execution**: Execute the path of actions returned by the solver.

## 7. Simple Example
Vacuum World (2 rooms: A, B):
- States: $\langle \text{Location}, \text{Room A dirt}, \text{Room B dirt} \rangle$ e.g., $\langle A, \text{Dirty}, \text{Clean} \rangle$.
- Actions: $\{\text{Left}, \text{Right}, \text{Suck}\}$.
- Goal: $\langle \cdot, \text{Clean}, \text{Clean} \rangle$.

## 8. Intermediate Example
8-Puzzle Grid:
- State: 3x3 matrix containing numbers 0..8 (0 is blank).
- Action: Move blank space $\{\text{Up}, \text{Down}, \text{Left}, \text{Right}\}$.
- Goal Test: Matrix equals $[[1,2,3],[4,5,6],[7,8,0]]$.

## 9. Output Interpretation
The solver returns a sequence of actions $[a_1, a_2, \dots, a_k]$ such that applying $T(s_{i-1}, a_i) = s_i$ starting from $s_0$ yields $G(s_k) = True$ with total path cost $C = \sum_{i=1}^k c(s_{i-1}, a_i, s_i)$.

## 10. Common Mistakes
- **Over-specifying state representations**: Including irrelevant data (e.g., color of vacuum cleaner).
- **Confusing physical states with state spaces**: A single board layout is a state; the set of all valid configurations is the state space.

## 11. Data Science Connection
Problem formulation maps directly to feature engineering and state definition in Reinforcement Learning (MDPs) and feature-space search.

## 12. AI/ML Connection
Classical problem formulation forms the discrete foundation for Markov Decision Processes (MDPs) used in modern Reinforcement Learning.

## 13. Interview Insight
When asked "How would you design an AI for X?", start by explicitly laying out the 6-tuple $(S, s_0, A, T, G, c)$. Interviewers look for systematic abstraction.

## 14. Summary
AI problem solving transforms unstructured real-world challenges into structured mathematical graphs defined by states, actions, transition rules, goal tests, and path costs.
