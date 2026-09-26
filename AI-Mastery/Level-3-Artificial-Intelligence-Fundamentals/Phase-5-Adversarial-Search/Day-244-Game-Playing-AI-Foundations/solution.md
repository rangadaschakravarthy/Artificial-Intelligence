# Practice Solutions — Day 244

## 1-5. Conceptual Answers
1. Zero-Sum Game: Total utility across all players is constant. Any gain by player A equals exact loss by player B ($U_A + U_B = 0$).
2. MAX player selects move to maximize score; MIN player selects move to minimize score (which maximizes MIN's advantage).
3. A ply is a single turn taken by one player (2 plies = 1 full round of move and counter-move).
4. Pruning cut-off occurs when $\alpha \ge \beta$.
5. Expanding the best moves first updates $\alpha$ and $\beta$ to tight bounds early, causing subsequent weaker branches to prune immediately.

## 6-10. Manual Tracing
6. Leaf values [3, 5, 2, 9, 1, 4, 0, 7]. MIN nodes: min(3,5)=3, min(2,9)=2, min(1,4)=1, min(0,7)=0. MAX root: max(3,2,1,0)=3.
7. Node 1: 3, 5 -> MIN=3, alpha=3. Node 2: first child 2 -> beta=2. Since alpha(3) >= beta(2), prune child 9!
8. Logs $(\alpha, \beta)$ bounds down tree branches.
9. Saved evaluations = 3 out of 8 leaf nodes (37.5% node reduction).
10. Board state utility = +10 if MAX wins, -10 if MIN wins, 0 otherwise.

## 11-13. Coding Solutions
```python
def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10 or score == -10 or depth == 0 or not moves_left(board):
        return score
    
    if is_max:
        best = -1000
        for move in get_moves(board):
            make_move(board, move, 'X')
            best = max(best, minimax(board, depth - 1, False))
            undo_move(board, move)
        return best
    else:
        best = 1000
        for move in get_moves(board):
            make_move(board, move, 'O')
            best = min(best, minimax(board, depth - 1, True))
            undo_move(board, move)
        return best

def alphabeta(board, depth, alpha, beta, is_max):
    score = evaluate(board)
    if score == 10 or score == -10 or depth == 0 or not moves_left(board):
        return score
    if is_max:
        v = -1000
        for move in get_moves(board):
            make_move(board, move, 'X')
            v = max(v, alphabeta(board, depth - 1, alpha, beta, False))
            undo_move(board, move)
            alpha = max(alpha, v)
            if alpha >= beta: break
        return v
    else:
        v = 1000
        for move in get_moves(board):
            make_move(board, move, 'O')
            best = min(v, alphabeta(board, depth - 1, alpha, beta, True))
            undo_move(board, move)
            beta = min(beta, v)
            if alpha >= beta: break
        return v
```

## 14-16. Debugging Solutions
14. Problem: Move loop didn't filter out occupied cells. Fix: Add `if cell == ' ': moves.append(i)`.
15. Problem: Alpha/Beta modified globally across recursive branches. Fix: Pass primitives `alpha` and `beta` by value in recursion arguments.
16. Problem: Board filled draw check missing. Fix: Add `if ' ' not in board:` to terminal conditions.

## 17-26. Advanced Answers
17. Both return exact same optimal move. Minimax takes $O(b^m)$ time; Alpha-Beta takes $O(b^{m/2})$ time with optimal ordering.
18. Minimax does exhaustive depth tree search; MCTS uses random simulation rollouts and UCT selection for high-branching games (Go).
19. Expectimax replaces MIN nodes with Chance nodes taking expected value sum $\sum P(s') V(s')$.
20-22. Interactive bots use game loop: get human move -> update board -> run AI search -> render board.
23-26. Proof shows pruned branches could never affect root decision because MAX/MIN already guaranteed better scores elsewhere. Horizon effect occurs when bad move is delayed beyond search depth limit.
