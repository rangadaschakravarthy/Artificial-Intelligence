# Practice Questions — Day 230

## Level 1 — Conceptual (5 Questions)
1. What distinguishes uninformed search from informed (heuristic) search?
2. Explain why BFS is complete when branching factor $b$ is finite.
3. Why is DFS space complexity $O(bm)$ while BFS space complexity is $O(b^d)$?
4. When is UCS guaranteed to yield an optimal path?
5. Why must UCS evaluate the goal test when a node is popped, rather than when generated?

## Level 2 — Manual Execution (5 Questions)
6. Draw a 4-level search tree ($b=2$) and show the exact pop order for BFS.
7. Show the exact pop order for DFS on the same tree.
8. Construct a trace table for UCS on a 5-node weighted graph.
9. Trace frontier contents step-by-step for a 3x3 grid search.
10. Calculate memory footprint of storing a BFS frontier at depth $d=10$ with $b=4$.

## Level 3 — Coding (3 Questions)
11. Implement BFS using `collections.deque` in Python.
12. Implement iterative DFS using an explicit Python `list` stack.
13. Implement UCS using Python's `heapq` library.

## Level 4 — Debugging (3 Questions)
14. Debug a BFS implementation that returns non-optimal paths due to early goal termination on weighted edges.
15. Fix a stack overflow error in recursive DFS caused by graph cycles.
16. Correct a priority queue ordering bug where nodes with identical costs fail comparison.

## Level 5 — Comparison (3 Questions)
17. Compare BFS vs DFS in terms of time, space, completeness, and optimality.
18. Compare UCS vs Dijkstra's algorithm.
19. Compare tree search (no explored set) vs graph search (with explored set).

## Level 6 — AI Applications (3 Questions)
20. Apply BFS to find minimum degree of separation in a social network graph.
21. Apply DFS to solve constraint satisfaction in automated Sudoku logic.
22. Apply UCS to find least-cost delivery routes in logistics networks.

## Level 7 — Interview Questions (5 Questions)
23. Under what conditions does BFS output the optimal path cost?
24. How would you modify DFS to guarantee completeness in infinite graphs? (Hint: Iterative Deepening).
25. Explain the impact of zero-cost edge loops on Uniform Cost Search.
26. How do memory constraints limit real-world deployment of BFS?
