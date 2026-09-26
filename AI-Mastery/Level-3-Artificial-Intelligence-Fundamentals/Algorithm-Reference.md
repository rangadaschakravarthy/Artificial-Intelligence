# Search Algorithm Reference Guide

| Algorithm | Search Strategy | Frontier Data Structure | Uses Heuristic? | Complete? | Optimal? | Time Complexity | Space Complexity |
| --------- | --------------- | ----------------------- | --------------- | --------- | -------- | --------------- | ---------------- |
| **BFS** | Level-order expansion | FIFO Queue (`collections.deque`) | No | Yes (if $b$ finite) | Yes (unweighted) | $O(b^d)$ | $O(b^d)$ |
| **DFS** | Deepest node first | LIFO Stack (`list`) | No | No (infinite graphs) | No | $O(b^m)$ | $O(bm)$ |
| **UCS** | Lowest path cost $g(n)$ | Min-Priority Queue (`heapq`) | No | Yes (if step cost $\ge \epsilon$) | Yes (weighted) | $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$ | $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$ |
| **Greedy Best-First** | Lowest heuristic $h(n)$ | Min-Priority Queue (`heapq`) | Yes | No (can loop without explored) | No | $O(b^m)$ worst case | $O(b^m)$ |
| **A* Search** | Lowest total $f(n) = g(n) + h(n)$ | Min-Priority Queue (`heapq`) | Yes | Yes | Yes (if $h$ admissible) | $O(b^d)$ | $O(b^d)$ |
| **Minimax** | Maximizes MAX / Minimizes MIN | Recursive Game Tree | No | Yes (finite trees) | Yes (against optimal MIN) | $O(b^m)$ | $O(bm)$ |
| **Alpha-Beta Pruning** | Minimax with $\alpha \ge \beta$ cut-off | Recursive Game Tree | No | Yes | Yes | $O(b^{m/2})$ optimal | $O(bm)$ |
