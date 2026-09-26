# Theory — Day 239: Greedy Search Python Implementation

## 1. What Is It?
Greedy Search Python Implementation is a cornerstone of informed search in Artificial Intelligence. Executable Python Greedy Best-First Search with heuristic callbacks and path evaluation.

## 2. Why Does It Exist?
Uninformed search algorithms (BFS, UCS) expand nodes uniformly in all directions. Informed heuristics guide search towards the goal target, reducing explored states exponentially.

## 3. Intuition
- **$g(n)$**: Actual cost incurred to travel from starting state $s_0$ to current node $n$.
- **$h(n)$**: Estimated remaining cost from node $n$ to the goal.
- **$f(n) = g(n) + h(n)$**: Total estimated cost of path passing through node $n$ to goal.

Think of driving across a country: $g(n)$ is the odometer reading so far; $h(n)$ is the straight-line distance on a map; $f(n)$ is the total trip estimate.

## 4. Syntax / Notation
$$\begin{aligned}
f(n) &= g(n) + h(n) \\
\text{Admissibility: } & 0 \le h(n) \le h^*(n) \quad \forall n \\
\text{Consistency: } & h(n) \le c(n, a, n') + h(n') \quad \forall n, n'
\end{aligned}$$

Where $h^*(n)$ is the true optimal cost from node $n$ to goal.

## 5. Parameters / Environment
- **Manhattan Distance** (Grid 4-way): $h(n) = |x_1 - x_2| + |y_1 - y_2|$.
- **Euclidean Distance** (Straight-line): $h(n) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$.
- **Open Set (Frontier)**: Priority queue sorted by ascending $f(n)$.
- **Closed Set (Explored)**: Hash set of fully evaluated nodes.

## 6. How It Works ($A^*$ Search Execution Loop)
1. Push starting node $s_0$ into Open Set with $g(s_0)=0, f(s_0)=h(s_0)$.
2. Initialize Closed Set $= \emptyset$.
3. Loop while Open Set is not empty:
   a. Pop node $n$ with lowest $f(n)$ value.
   b. If $n$ is Goal, reconstruct and return path.
   c. Add $n$ to Closed Set.
   d. For each successor $n'$ of $n$ via action $a$:
      - If $n' \in \text{Closed Set}$, continue.
      - Tentative $g_{\text{tent}} = g(n) + c(n, a, n')$.
      - If $n' \notin \text{Open Set}$ or $g_{\text{tent}} < g(n')$:
        - Update parent of $n'$ to $n$, set $g(n') = g_{\text{tent}}$, $f(n') = g(n') + h(n')$.
        - Insert/update $n'$ in Open Set.

## 7. Simple Example
Start $S(0,0)$, Goal $G(2,2)$. Obstacle at $(1,1)$.
- $h(S) = |2-0| + |2-0| = 4$. $g(S)=0 \implies f(S)=4$.
- Successors $(1,0)$ and $(0,1)$ evaluated by $f(n) = g(n) + h(n)$. $A^*$ navigates efficiently around the obstacle!

## 8. Intermediate Example (Romania Distance Graph)
Arad to Bucharest route planning using straight-line distance heuristics $h_{\text{SLD}}$.

## 9. Output Interpretation
Returns optimal path array, minimal path cost $g(\text{Goal})$, total expanded nodes, and execution runtime.

## 10. Common Mistakes
- **Inadmissible Heuristic**: Overestimating $h(n) > h^*(n)$ breaks $A^*$ optimality guarantees!
- **Inconsistent Heuristic**: Violating triangle inequality requires re-opening closed nodes.

## 11. Data Science Connection
$A^*$ principles align with cost function minimization in optimization algorithms (Gradient Descent + Regularization term $\approx g(n) + h(n)$).

## 12. AI/ML Connection
Used in modern game engines (Unity / Unreal Navigation Meshes), robotics motion planning (RRT* / $A^*$), and LLM token decoding (Heuristic Guided Search).

## 13. Interview Insight
When asked to prove $A^*$ optimality, state: "If $h(n)$ is admissible, when $A^*$ pops a goal node from the priority queue, any remaining node $n'$ in the queue has $f(n') = g(n') + h(n') \ge g(n') + 0 \ge g(\text{Goal})$, proving no cheaper goal path exists."

## 14. Summary
Greedy Search Python Implementation unifies accumulated path cost $g(n)$ and heuristic estimate $h(n)$ to deliver optimal, computationally focused search solutions.
