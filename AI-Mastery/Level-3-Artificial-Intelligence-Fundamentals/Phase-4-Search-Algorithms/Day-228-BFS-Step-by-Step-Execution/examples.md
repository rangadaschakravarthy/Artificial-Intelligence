# Examples — Day 228: BFS Step-by-Step Execution

## Example 1: Unweighted Graph Traversal
Nodes: A, B, C, D, Goal. Edges: (A-B), (A-C), (B-D), (C-Goal).
Search Order (BFS): A -> B -> C -> D -> Goal. Path: A -> C -> Goal.

## Example 2: Weighted Graph Traversal
Edges: (S->A: 1), (S->B: 5), (A->G: 10), (B->G: 2).
UCS Frontier sequence: S(0) -> A(1), B(5) -> B(5), G(11) -> G(7). Optimal Path: S -> B -> G (cost 7).

## Example 3: Stack Backtracking in Maze
DFS enters dead-end at Node X, pops stack frame, backtracks to junction Node Y, continues along alternative path.

## Example 4: State Graph Cycle Avoidance
Graph with cycle A -> B -> C -> A. Explored set prevents re-adding A to frontier when expanding C.

## Example 5: Path Reconstruction via Parent Pointers
Node(G) -> Parent Node(B) -> Parent Node(A) -> None. Reconstructed: [A, B, G].
