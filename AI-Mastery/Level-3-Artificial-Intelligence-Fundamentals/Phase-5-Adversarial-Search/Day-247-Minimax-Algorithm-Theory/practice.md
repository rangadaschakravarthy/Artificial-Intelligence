# Practice Questions — Day 247

## Level 1 — Conceptual (5 Questions)
1. Define a Zero-Sum Game in AI game theory.
2. Explain the difference between MAX player and MIN player roles.
3. What is a ply in game trees?
4. Write the mathematical condition for an Alpha-Beta pruning cut-off.
5. Why does move ordering significantly impact Alpha-Beta pruning efficiency?

## Level 2 — Manual Execution (5 Questions)
6. Draw a 3-level game tree with 8 leaf values and execute Minimax propagation.
7. Execute Alpha-Beta pruning on the same tree, explicitly marking PRUNED branches.
8. Trace alpha and beta values $(\alpha, \beta)$ at every node of the tree.
9. Calculate the total number of node evaluations saved by Alpha-Beta pruning.
10. Evaluate a Tic-Tac-Toe board state and compute its static utility value.

## Level 3 — Coding (3 Questions)
11. Implement a recursive Minimax function in Python.
12. Implement Alpha-Beta pruning in Python for a general game tree.
13. Implement a Tic-Tac-Toe game environment class with move validation.

## Level 4 — Debugging (3 Questions)
14. Debug a Minimax implementation that allows the AI to choose illegal moves.
15. Fix a bug in Alpha-Beta pruning where alpha/beta values are not passed by value correctly across recursion.
16. Resolve an infinite recursion error caused by missing terminal state detection.

## Level 5 — Comparison (3 Questions)
17. Compare Minimax vs Alpha-Beta Pruning in time, space, and output correctness.
18. Compare Minimax search vs Monte Carlo Tree Search (MCTS).
19. Compare deterministic game AI vs stochastic (dice/cards) game AI (Expectimax).

## Level 6 — AI Applications (3 Questions)
20. Build an unbeatable Tic-Tac-Toe AI using Alpha-Beta pruning.
21. Design an evaluation heuristic function for Connect-Four.
22. Apply Minimax concepts to competitive automated pricing bots.

## Level 7 — Interview Questions (5 Questions)
23. Prove that Alpha-Beta pruning always returns the exact same move as Minimax.
24. What is the theoretical minimum complexity $O(b^{m/2})$ of Alpha-Beta pruning under optimal move ordering?
25. How do evaluation function inaccuracies affect Minimax decision quality?
26. Explain Horizon Effect in game-playing AI and how Quiescence Search resolves it.
