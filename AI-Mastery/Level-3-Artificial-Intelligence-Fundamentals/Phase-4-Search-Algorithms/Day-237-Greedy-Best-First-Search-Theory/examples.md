# Examples — Day 237: Greedy Best-First Search Theory

## Example 1: Manhattan Distance Calculation
Current: (2, 3), Goal: (5, 7).
$h(n) = |5 - 2| + |7 - 3| = 3 + 4 = 7$.

## Example 2: Admissibility Verification
True cost to goal $h^*(n) = 10$.
- $h_1(n) = 8 \implies$ Admissible ($8 \le 10$).
- $h_2(n) = 12 \implies$ Inadmissible ($12 > 10$).

## Example 3: Numerical Trace of A* Search
Node S: g=0, h=6, f=6.
Expand S -> Node A (g=2, h=4, f=6), Node B (g=1, h=7, f=8).
Pop A (f=6) -> Expand to Goal G (g=2+4=6, h=0, f=6).
Optimal Path found: S -> A -> G (cost 6).

## Example 4: Greedy Search vs A* Search Comparison
Greedy follows lowest $h(n)$ blindly and takes a long, sub-optimal detour. $A^*$ balances $g(n)$ and $h(n)$ to stay on optimal path.

## Example 5: Grid Navigation with Obstacles
2D grid maze pathfinding showing Open Set priority queue state transitions.
