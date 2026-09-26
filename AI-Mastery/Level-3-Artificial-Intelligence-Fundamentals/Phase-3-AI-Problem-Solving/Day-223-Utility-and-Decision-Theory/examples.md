# Examples — Day 223: Utility & Decision Theory

## Example 1: Basic Propositional Modus Ponens
Fact: `Symptom(Fever)`
Rule: `Symptom(Fever) -> Infection`
Derived Fact: `Infection`

## Example 2: Forward Chaining Path Execution
Base Facts: `{ A, B }`
Rules: `A & B -> C`, `C -> D`
Derived Facts: `{ A, B, C, D }`

## Example 3: Abductive Medical Reasoning
Observation: `Patient Has Rash`
Candidate Causes: `[Chickenpox (prob 0.8), Measles (prob 0.15), Allergy (prob 0.05)]`
Best Explanation: `Chickenpox`

## Example 4: STRIPS Planning Step
Initial State: `At(Robot, RoomA)`
Goal State: `At(Robot, RoomB)`
Action: `Move(RoomA, RoomB)` -> Preconditions satisfied, state updated.

## Example 5: Maximum Expected Utility Calculation
Action 1 (Safe Road): $U=80$, $P=1.0 \implies \text{EU}=80$.
Action 2 (Highway): $U=100$ ($P=0.7$) + $U=0$ ($P=0.3$) $\implies \text{EU}=70$.
Optimal Decision: Action 1.
