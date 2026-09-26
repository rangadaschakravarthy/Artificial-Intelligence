# Examples — Day 244: Game-Playing AI Foundations

## Example 1: Terminal Utility Evaluation
Tic-Tac-Toe:
- Board where X has 3 in a row $\implies +10$.
- Board where O has 3 in a row $\implies -10$.
- Board full with no winner $\implies 0$.

## Example 2: Minimax Value Propagation
Leaf values: [4, 7, 2, 8].
MIN layer computes: min(4,7)=4, min(2,8)=2.
MAX layer computes: max(4,2)=4. Minimax root value = 4.

## Example 3: Alpha-Beta Pruning Trace
Leaf values evaluated in order: 3, 5, 2...
When evaluating second branch, alpha=3, beta updated to 2.
Prune condition triggered (3 >= 2). Remaining children skipped.

## Example 4: Heuristic Evaluation Function for Non-Terminal Nodes
Chess: Static evaluation function $E = \text{Material Count} + \text{Positional Mobility}$.
$Q=9, R=5, B=3, N=3, P=1$.

## Example 5: Interactive Human vs AI Tic-Tac-Toe
AI uses Alpha-Beta with depth limit 9 to guarantee it never loses.
