# Day 209 Theory: Rule-Based Expert System Architecture

### 1. What Is It?
The Rule-Based Expert System Mini Project implements a classic 1980s-era Symbolic AI inference engine that deduces diagnostic conclusions from a fact base using IF-THEN rules and provides a human-readable explanation trace.

### 2. Engine Components
1. **Fact Base**: Set of verified facts (`{"fever", "cough"}`).
2. **Rule Base**: List of production rules with preconditions and conclusions.
3. **Inference Engine**: Match-Resolve-Execute forward chaining loop.
4. **Explanation Facility**: Audit log tracking which rules fired.

### 3. Summary
Demonstrates 1980s Symbolic AI by implementing a production-rule forward chaining engine with an explanation trace.
