# Practice Questions — Day 237

## Level 1 — Conceptual (5 Questions)
1. Write the formal definition of $f(n)$ in $A^*$ search.
2. Define heuristic admissibility and state its mathematical condition.
3. Define heuristic consistency (monotonicity) and state its condition.
4. Why does Greedy Best-First Search risk finding sub-optimal paths?
5. How does $A^*$ behave when $h(n) = 0$ for all nodes?

## Level 2 — Manual Execution (5 Questions)
6. Calculate Manhattan and Euclidean distances between $(1, 2)$ and $(4, 6)$.
7. Given a 5-node graph with heuristic values, manually trace $A^*$ expansion.
8. Show the open set priority queue contents at each step of $A^*$.
9. Verify whether a given heuristic table is admissible and consistent.
10. Construct a counterexample where an inadmissible heuristic causes $A^*$ to return a non-optimal path.

## Level 3 — Coding (3 Questions)
11. Write a Python function for Manhattan and Euclidean distance heuristics.
12. Implement Greedy Best-First Search in Python using `heapq`.
13. Implement full $A^*$ Graph Search in Python.

## Level 4 — Debugging (3 Questions)
14. Debug an $A^*$ solver that loops infinitely because heuristic values are negative.
15. Fix a priority queue update error in $A^*$ where cheaper $g(n)$ paths fail to update existing nodes.
16. Correct a grid $A^*$ implementation that allows illegal diagonal movement through wall corners.

## Level 5 — Comparison (3 Questions)
17. Compare $A^*$ vs Uniform Cost Search vs Greedy Best-First Search.
18. Compare Manhattan distance vs Euclidean distance vs Chebyshev distance.
19. Compare $A^*$ with admissible heuristic vs $A^*$ with weighted heuristic $f(n) = g(n) + w \cdot h(n)$.

## Level 6 — AI Applications (3 Questions)
20. Implement $A^*$ for NPC pathfinding in a 2D game grid.
21. Apply $A^*$ to solve the 8-puzzle using Manhattan distance.
22. Apply $A^*$ to automated road network route navigation.

## Level 7 — Interview Questions (5 Questions)
23. Prove that $A^*$ graph search is optimal when $h(n)$ is consistent.
24. What is the effect of heuristic dominance ($h_2(n) \ge h_1(n)$)?
25. How does Weighted $A^*$ ($w > 1$) trade off solution quality for speed?
26. What are the space complexity limitations of $A^*$, and how does IDA* solve them?
