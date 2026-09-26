# Practice Solutions — Day 242

## 1-5. Conceptual Answers
1. $f(n) = g(n) + h(n)$, where $g(n)$ is accumulated path cost from start to $n$, and $h(n)$ is estimated cost from $n$ to goal.
2. Admissibility: $0 \le h(n) \le h^*(n)$ for all nodes $n$. The heuristic never overestimates the true remaining cost.
3. Consistency: $h(n) \le c(n, a, n') + h(n')$ for all nodes $n, n'$. Satisfies triangle inequality.
4. Greedy search selects nodes based purely on $h(n)$, ignoring $g(n)$, so it can be trapped by low-heuristic dead ends or long paths.
5. When $h(n)=0$, $f(n)=g(n)$, reducing $A^*$ search exactly to Uniform Cost Search (UCS).

## 6-10. Manual Tracing
6. Manhattan: $|4-1| + |6-2| = 3 + 4 = 7$. Euclidean: $\sqrt{3^2 + 4^2} = \sqrt{25} = 5$.
7. Step 1: Open=[(S, f=6)]. Step 2: Pop S, Expand A(g=2,h=4,f=6), B(g=1,h=7,f=8). Open=[(A, f=6), (B, f=8)]. Step 3: Pop A -> Goal G(g=6,h=0,f=6). Path: S -> A -> G.
8. Open set sequence logs priority queue state at each iteration.
9. Check $h(n) \le h^*(n)$ for all nodes. If holds for all, admissible. Check $h(n) - h(n') \le c(n, n')$. If holds, consistent.
10. If $h(A) = 100$ (overestimate), $A^*$ skips expanding $A$ and picks sub-optimal path $B$ with cost 50 instead of path $A$ with cost 10.

## 11-13. Coding Solutions
```python
import heapq

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star_search(grid, start, goal):
    # Open set: (f_score, g_score, current, path)
    open_set = [(manhattan(start, goal), 0, start, [start])]
    g_score = {start: 0}
    closed_set = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return g, path
        if current in closed_set:
            continue
        closed_set.add(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + manhattan(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor, path + [neighbor]))
    return float('inf'), []
```

## 14-16. Debugging Solutions
14. Negative heuristics break admissibility ($h(n) < 0$). Fix: clamp $h(n) = \max(0, h(n))$.
15. Node $g$-scores were not updated when finding a shorter path to an existing open node. Fix: track `g_score` dict and re-push updated tuple.
16. Diagonal movement allowed `(x+1, y+1)` even if `(x+1, y)` and `(x, y+1)` were walls. Fix: add corner-cutting collision validation.

## 17-26. Advanced Answers
17. UCS: $f=g$ (Optimal, Uninformed, slow). Greedy: $f=h$ (Fast, Sub-optimal). $A^*$: $f=g+h$ (Optimal, Informed, Fast).
18. Manhattan for 4-way grid movement; Euclidean for continuous 2D plane; Chebyshev for 8-way grid movement.
19. Weighted $A^*$ ($w > 1$) speeds up search by focusing more on $h(n)$, guaranteeing solution within factor $w \cdot C^*$.
20-22. Real-world pathfinding engines use $A^*$ with precomputed landmark heuristics and hierarchical graphs.
23-26. Proof shows consistent $h(n)$ ensures non-decreasing $f(n)$ along any path, preventing re-expansion of closed nodes.
