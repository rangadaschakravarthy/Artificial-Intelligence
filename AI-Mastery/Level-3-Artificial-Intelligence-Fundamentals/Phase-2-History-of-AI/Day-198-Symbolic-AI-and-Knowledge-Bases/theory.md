# Day 198 Theory: Symbolic AI and Knowledge Bases

### 1. What Is It?
Knowledge-Based Systems represent domain expertise explicitly as structured facts and IF-THEN production rules, using an inference engine to deduce new conclusions.

### 2. Forward vs Backward Chaining
- **Forward Chaining (Data-Driven)**:
  $$\text{Known Facts} \xrightarrow{\text{Match IF Rules}} \text{Infer New Facts} \xrightarrow{\dots} \text{Reach Goal}$$
- **Backward Chaining (Goal-Driven)**:
  $$\text{Goal Hypothesis} \xrightarrow{\text{Check THEN Rules}} \text{Verify IF Conditions} \xrightarrow{\dots} \text{Match Base Facts}$$

### 3. Summary
Forward chaining deduces new conclusions from facts; backward chaining verifies supporting evidence for goals.
