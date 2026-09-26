# Complexity Reference Guide for AI Search

## Key Complexity Notation & Variables
- $b$: Branching factor (average number of successor edges per state).
- $d$: Depth of the shallowest optimal goal state.
- $m$: Maximum depth of the state space graph.
- $C^*$: Cost of the optimal path.
- $\epsilon$: Minimum positive step cost bound ($\min c(s, a, s') > 0$).

## Asymptotic Growth Classes
1. **$O(1)$ Constant Time**: Immediate hash lookup or goal test.
2. **$O(\log N)$ Logarithmic Time**: Binary tree branch navigation.
3. **$O(N)$ Linear Time**: Traversal of single branch path.
4. **$O(b^d)$ Exponential Time**: Breadth-First and $A^*$ search frontier growth.
5. **$O(b^m)$ Deep Exponential Time**: Depth-First search maximum path traversal.
6. **$O(b^{m/2})$ Pruned Exponential Time**: Optimal Alpha-Beta pruning game tree evaluation.

## Space Complexity Tradeoffs
- **Linear Space $O(bm)$**: Storing only current path and unexpanded siblings (DFS).
- **Exponential Space $O(b^d)$**: Storing all boundary frontier states (BFS, $A^*$). High memory requirements often cause out-of-memory errors before time limits expire!
