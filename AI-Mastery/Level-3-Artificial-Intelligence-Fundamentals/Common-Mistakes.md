# Common Mistakes in AI Fundamentals & Search

1. **Confusing AI with Machine Learning**: Assuming every AI system requires statistical training datasets. Rule-based expert systems and $A^*$ search are classical AI without ML.
2. **Modifying State Objects In-Place**: Mutating shared state lists during graph search causes parent pointers and historical states to corrupt retroactively.
3. **Using BFS on Weighted Graphs**: Expecting BFS to find shortest path cost when edge weights differ. BFS minimizes step count, not path cost!
4. **Evaluating Goal Test on Generation in UCS**: Testing for goal when adding to priority queue instead of when popping. This can return sub-optimal paths on weighted graphs.
5. **Using Inadmissible Heuristics in A***: Overestimating remaining cost ($h(n) > h^*(n)$) breaks $A^*$ optimality guarantees.
6. **Passing Global Alpha/Beta in Pruning**: Mutating alpha/beta across sibling branches in Alpha-Beta pruning instead of passing them by value down recursive paths.
