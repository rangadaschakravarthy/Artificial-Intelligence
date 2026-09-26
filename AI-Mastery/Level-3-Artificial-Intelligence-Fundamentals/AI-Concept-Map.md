# AI Concept Map — Level 3: Artificial Intelligence Fundamentals

```
                                ARTIFICIAL INTELLIGENCE
                                           │
       ┌───────────────────────────┬───────┴───────┬───────────────────────────┐
       ▼                           ▼               ▼                           ▼
  SYMBOLIC AI                PROBLEM SOLVING    SEARCH ALGORITHMS        ADVERSARIAL SEARCH
       │                           │               │                           │
  ┌────┴────┐                 ┌────┴────┐     ┌────┴────┐                 ┌────┴────┐
  ▼         ▼                 ▼         ▼     ▼         ▼                 ▼         ▼
Rules     Logic            States    Actions BFS/DFS  UCS/A*           Minimax  Alpha-Beta
Knowledge Chaining         Goals    Cost     Trees    Heuristics       GameTree Pruning
       │                           │               │                           │
       └───────────────────────────┼───────────────┴───────────────────────────┘
                                   │
                                   ▼
                      MACHINE LEARNING & MODERN AI
                      (Supervised, Unsupervised, RL)
```

## Relationships & Architecture Overview
1. **Symbolic AI**: Relies on explicit domain knowledge encoded as rules and logical statements.
2. **Problem Solving**: Converts complex physical reality into discrete mathematical 6-tuples $\langle S, s_0, A, T, G, c \rangle$.
3. **Search Algorithms**: Systematic state-space exploration techniques dividing into uninformed (BFS, DFS, UCS) and informed heuristic search (Greedy, $A^*$).
4. **Adversarial Search**: Decision-making optimization in zero-sum competitive environments using Minimax payoff evaluation and Alpha-Beta pruning.
5. **Machine Learning Connection**: Classical state search forms the discrete foundation for Markov Decision Processes (MDPs) and Reinforcement Learning algorithms.
