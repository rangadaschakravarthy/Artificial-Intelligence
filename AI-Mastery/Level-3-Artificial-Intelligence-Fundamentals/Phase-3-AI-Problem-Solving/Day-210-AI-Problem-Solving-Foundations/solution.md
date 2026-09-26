# Practice Solutions — Day 210

## 1-5. Conceptual Answers
1. The 6-tuple is $\langle S, s_0, A, T, G, c \rangle$: State space, initial state, action function, transition model, goal test function, step cost function.
2. Environment space is the physical reality; state space is the minimal mathematical abstraction used by the agent to make decisions.
3. Validity requires that all real-world valid configurations can be represented; soundness requires that no illegal operations are permitted in the model.
4. Deterministic: $T(s, a)$ yields exactly one predictable state $s'$. Non-deterministic: $T(s, a)$ yields a probability distribution over multiple possible states.
5. Abstraction reduces computational complexity by omitting non-essential physical variables.

## 6-10. Manual Tracing Solutions
6. $S$: $3 \times 3$ grid with values $\{X, O, \text{Empty}\}$. $s_0$: empty grid. $A(s)$: place $X$ in any empty cell. $T(s, a)$: board with $X$ placed. $G(s)$: 3 $X$'s in a line. Step cost $c = 1$.
7. Total permutations of 9 tiles = $9! = 362,880$. Half are reachable due to inversion parity, so $|S| = 362,880 / 2 = 181,440$.
8. $(0,0) \to (5,0) \to (2,3) \to (2,0) \to (0,2) \to (5,2) \to (4,3)$. 4L in 5L jug!
9. From $(3,3,1)$ (left bank), valid boat moves: 2 Cannibals $(0,2)$, 2 Missionaries $(2,0)$, or 1 of each $(1,1)$. Left bank becomes $(3,1,0)$, $(1,3,0)$, or $(2,2,0)$. $(3,1,0)$ leaves 2 cannibals and 0 missionaries on right bank (safe). $(1,3,0)$ leaves 2 missionaries and 0 cannibals on left bank (safe).
10. States: $(x,y)$ coordinates for $x, y \in \{1..4\}$. Obstacles remove $(x,y)$ from $S$. Actions: $\{\text{N, S, E, W}\}$ restricted by boundary and obstacles.

## 11-13. Coding Solutions
```python
class Problem:
    def __init__(self, initial_state, goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def actions(self, state):
        raise NotImplementedError
        
    def result(self, state, action):
        raise NotImplementedError
        
    def is_goal(self, state):
        return state == self.goal_state

class EightPuzzle(Problem):
    def actions(self, state):
        # state is tuple of length 9
        blank = state.index(0)
        moves = []
        if blank >= 3: moves.append('UP')
        if blank <= 5: moves.append('DOWN')
        if blank % 3 != 0: moves.append('LEFT')
        if blank % 3 != 2: moves.append('RIGHT')
        return moves
```

## 14-16. Debugging Solutions
14. Flaw: swapped blank across row boundaries without checking `blank % 3`. Fix: enforce modulo boundary checks.
15. Flaw: `state.append(x)` mutates list in place so prior states change retroactively. Fix: use tuples or copy state `list(state)`.
16. Flaw: goal check checked `state[0] == 1` instead of full board matching. Fix: check full equality `state == goal_tuple`.

## 17-19. Comparison Solutions
17. Route finding state space size scales linearly/quadratically with map nodes; 8-puzzle grows exponentially with grid dimensions ($N^2!/2$).
18. Fully observable: agent state equals world state. Partially observable: agent state is a belief state (set of possible world states).
19. Path cost $g(n)$ is total sum of step costs along path; step cost $c(s, a, s')$ is localized cost of a single state transition.

## 20-22. AI Applications
20. Drone Delivery: $S = (x, y, z, \text{battery}, \text{payload\_status})$. Actions = waypoint movements, land, drop. Goal = payload delivered at target location with battery $> 15\%$.
21. Automated Code Gen: $S = \text{Abstract Syntax Tree (AST)}$. Actions = append node/token. Goal = pass all unit test suites.
22. Portfolio: $S = \text{asset allocation weights vector}$. Actions = rebalance $\pm \Delta w$. Goal = maximize Sharpe ratio.

## 23-26. Interview Solutions
23. Include variables directly influencing performance measure or state accessibility; exclude uninformative environmental factors.
24. Too detailed state space leads to exponential state explosion; over-simplified state space leads to invalid or unreachable solutions.
25. Symmetries introduce redundant paths; breaking symmetries collapses state space size significantly.
26. Requires stochastic transition function $P(s' | s, a)$ leading to Expectimax or MDP formulations rather than simple search trees.
