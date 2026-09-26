# AI Glossary — Level 3 Fundamentals

- **Agent**: An entity that perceives its environment through sensors and takes actions via actuators.
- **Environment**: The world or task domain in which an agent operates.
- **State ($s$)**: A discrete mathematical configuration of the problem environment.
- **Action ($a$)**: A valid move or operation an agent can perform in a given state.
- **Transition Model ($T(s, a)$)**: Function defining the successor state resulting from executing action $a$ in state $s$.
- **Goal Test ($G(s)$)**: Predicate function determining whether state $s$ satisfies the goal criteria.
- **Path Cost ($g(n)$)**: Accumulated sum of step costs from initial state to node $n$.
- **Heuristic ($h(n)$)**: Domain-specific estimate of remaining path cost from node $n$ to goal.
- **Admissible Heuristic**: A heuristic that never overestimates the true remaining cost to goal ($h(n) \le h^*(n)$).
- **Consistent Heuristic**: A heuristic satisfying triangle inequality ($h(n) \le c(n, a, n') + h(n')$).
- **Frontier (Open Set)**: Data structure containing nodes discovered but not yet expanded.
- **Explored Set (Closed Set)**: Data structure tracking already expanded states to prevent loops.
- **Minimax**: Algorithm for computing optimal move sequence in two-player zero-sum games.
- **Alpha-Beta Pruning**: Optimization technique that skips evaluating branches that cannot affect the final Minimax decision.
