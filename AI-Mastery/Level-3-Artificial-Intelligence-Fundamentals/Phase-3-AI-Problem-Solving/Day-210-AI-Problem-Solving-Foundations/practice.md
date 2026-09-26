# Practice Questions — Day 210

## Level 1 — Conceptual (5 Questions)
1. Define the 6-tuple formulation of an AI search problem.
2. Explain the difference between state space and environment space.
3. What makes a problem formulation valid and sound?
4. Differentiate deterministic transitions from non-deterministic transitions.
5. Why is abstraction essential when defining AI states?

## Level 2 — Manual Execution & Tracing (5 Questions)
6. Write out the formal 6-tuple for a 3x3 Tic-Tac-Toe game from the perspective of X's first turn.
7. Calculate the total state space size for the 8-puzzle problem (explain parity constraints).
8. Given a 2-jug problem (5L and 3L), trace a valid sequence of state transitions to measure 4L.
9. Trace the valid successor states from initial state $(3, 3, 1)$ in Missionaries & Cannibals.
10. Represent a 4x4 maze navigation problem with 3 obstacles as a state space graph.

## Level 3 — Coding Exercises (3 Questions)
11. Build a `Problem` base class in Python storing $s_0$, $A(s)$, $T(s,a)$, and $G(s)$.
12. Implement a Python class representing the 8-puzzle problem state space.
13. Write a Python function that verifies whether a given sequence of actions reaches the goal state from $s_0$.

## Level 4 — Debugging (3 Questions)
14. Identify the flaw in an 8-puzzle transition function that allows illegal tile swaps.
15. Fix a infinite loop defect in a state generator caused by mutating mutable state objects in place.
16. Correct an invalid goal check function that returns True for partially satisfied conditions.

## Level 5 — Comparison (3 Questions)
17. Compare State Space formulation for Route Finding vs. 8-Puzzle.
18. Contrast fully observable problem formulation with partially observable problem formulation.
19. Compare path-cost formulation vs. step-cost formulation.

## Level 6 — AI Applications (3 Questions)
20. Formulate an AI problem for automated logistics drone delivery.
21. Formulate automated code generation as a state search problem.
22. Formulate dynamic portfolio optimization as an AI search problem.

## Level 7 — Interview Questions (5 Questions)
23. How do you decide what details to include or omit in an AI problem formulation?
24. Explain the relationship between problem formulation efficiency and search space explosion.
25. How do state space symmetries affect search performance?
26. What happens to state space formulation when action outcomes are stochastic?
