# Level 3 Comprehensive Interview Questions & Solutions

## 1. AI Fundamentals & Agents
- **Q**: What is the difference between AI, Machine Learning, Deep Learning, and Generative AI?
- **A**: AI is the broad field of creating intelligent agents. ML is a subset of AI where systems learn rules from data. Deep Learning is an ML subset using deep neural networks for representation learning. Generative AI is a modern capability built on DL models (e.g., Transformers) to generate new content.

## 2. Problem Solving & State Spaces
- **Q**: How do you formally formulate an AI search problem?
- **A**: By defining a 6-tuple $\langle S, s_0, A, T, G, c \rangle$: State space $S$, initial state $s_0$, action function $A(s)$, transition model $T(s,a)$, goal test predicate $G(s)$, and step cost function $c(s,a,s')$.

## 3. Search Algorithms
- **Q**: When is BFS guaranteed to find an optimal path?
- **A**: When all step costs are equal (unweighted graph). On weighted graphs, Uniform Cost Search (UCS) or $A^*$ is required.

- **Q**: Prove why $A^*$ is optimal with an admissible heuristic.
- **A**: When $A^*$ pops goal node $G$ from the priority queue, any other node $n'$ in the queue has $f(n') = g(n') + h(n') \ge g(n') + 0 \ge g(G)$. Because $h$ never overestimates, no remaining unexpanded path can yield a cost smaller than $g(G)$.

## 4. Adversarial Search
- **Q**: How does Alpha-Beta pruning achieve $O(b^{m/2})$ time complexity?
- **A**: Under optimal move ordering (evaluating best moves first), alpha and beta bounds tighten immediately. This allows pruning roughly half of the branches at every ply, effectively doubling search depth.
