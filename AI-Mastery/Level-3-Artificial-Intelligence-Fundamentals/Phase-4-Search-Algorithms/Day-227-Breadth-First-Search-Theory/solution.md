# Practice Solutions — Day 227

## 1-5. Conceptual Answers
1. Uninformed search uses only problem definition ($S, A, T, G, c$); informed search uses domain-specific heuristics $h(n)$.
2. BFS explores depth levels systematically ($0, 1, 2, \dots, d$). Finite $b$ guarantees shallowest goal depth $d$ is reached in finite steps.
3. DFS stores only the current path and unexplored siblings ($O(bm)$); BFS stores all generated nodes at frontier boundary ($O(b^d)$).
4. UCS is optimal if all step costs $c(s, a, s') \ge \epsilon > 0$.
5. On weighted graphs, a cheaper path to goal $G$ may exist via unexpanded nodes in frontier; testing on pop ensures no cheaper path remains!

## 6-10. Manual Tracing
6. BFS Pop Order: Level 0 (Node 1), Level 1 (Nodes 2, 3), Level 2 (Nodes 4, 5, 6, 7).
7. DFS Pop Order: 1, 2, 4, 5, 3, 6, 7.
8. Trace table tracks: Step | Current Node | g(n) | Frontier List | Explored Set.
9. Grid (0,0) -> Frontier [(1,0), (0,1)] -> Pop (1,0) -> Frontier [(0,1), (2,0), (1,1)].
10. $b^d = 4^{10} = 1,048,576$ nodes in queue. At 100 bytes/node $\approx 104.8$ MB memory.

## 11-13. Coding Solutions
```python
from collections import deque
import heapq

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal: return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

def ucs(graph, start, goal):
    pq = [(0, start, [start])] # (cost, node, path)
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal: return (cost, path)
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return (float('inf'), [])
```

## 14-16. Debugging Solutions
14. Problem: BFS checked goal on child generation on a weighted graph. Fix: Use UCS with priority queue and goal check on pop.
15. Problem: Recursive DFS without visited tracking. Fix: Pass `visited=set()` set through recursive calls.
16. Problem: `heapq` compared raw node objects on cost ties. Fix: Store `(cost, id(node), node)` or define custom `__lt__`.

## 17-26. Advanced Answers
17. BFS: $O(b^d)$ space, Optimal (unweighted), Complete. DFS: $O(bm)$ space, Not optimal, Incomplete (infinite graphs).
18. UCS is identical to Dijkstra's algorithm, but stops immediately when target goal is popped rather than computing all shortest paths.
19. Tree search duplicates cyclic states ($O(\infty)$ time); graph search uses explored set to guarantee finite termination.
20-22. Real-world pathing utilizes domain-specific indexing (R-trees / spatial grids).
23-26. Interview answers highlight space bounds, zero-cost edge infinite loops, and iterative deepening (IDDFS).
