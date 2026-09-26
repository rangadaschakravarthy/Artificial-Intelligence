# Practice Solutions — Day 216

## 1-5. Conceptual Answers
1. Search Trees & Search Graphs abstracts complex domain physics into computable graph nodes and edges.
2. State representation is the internal data structure for one state; state space is the set of all reachable states.
3. Immutability prevents unintended state corruption when expanding multiple search paths.
4. Higher branching factor $b$ increases state space growth rate exponentially ($O(b^d)$).
5. Explicit goal lists allow direct lookup; implicit goal predicates allow matching infinitely large goal sets.

## 6-10. Manual Tracing
6. Depth 0: $(0,0)$. Depth 1: $(1,0), (-1,0), (0,1), (0,-1)$. Depth 2: 12 surrounding states.
7. Center cell has $b=4$; corner cells have $b=2$; wall cells have $b=3$. Average $b = 2.8$.
8. Search tree duplicates cyclic nodes infinitely without explored sets; state graph merges duplicate nodes.
9. Inversion count = 1 (odd). Solvable 8-puzzles must have even inversion count. Not reachable!
10. 64-bit integer tuple $\approx 80$ bytes $\times 10^6 = 80$ MB memory.

## 11-13. Coding Solutions
```python
class StateSpaceNode:
    def __init__(self, state_id, payload=None):
        self.state_id = state_id
        self.payload = payload
    def __eq__(self, other):
        return self.state_id == other.state_id
    def __hash__(self):
        return hash(self.state_id)
```

## 14-16. Debugging Solutions
14. Use `tuple(state)` instead of `list(state)` to make state hashable and immutable.
15. Maintain a `visited = set()` to track explored state hashes.
16. Ensure consistent key types (e.g., int vs str) across state dictionaries.

## 17-26. Advanced Answers
17. Explicit graphs store all nodes in memory; implicit graphs generate nodes on demand via successor functions.
18. Vector states allow matrix operations; graph states allow topological traversals.
19. Path-cost focuses on edge weights; state-count focuses on minimum edge steps.
20-22. Real-world applications rely on domain-specific state filtering and bounding boxes.
23-26. Interview responses should emphasize state space abstraction, hashing efficiency, and graph vs tree distinctions.
