# Practice Solutions — Day 220

## 1-5. Conceptual Answers
1. Deductive, Inductive & Abductive Reasoning equips AI agents with symbolic inference, planning, and utility-based choice mechanisms.
2. Deduction derives guaranteed facts from premises; Induction learns general rules from data; Abduction finds best plausible explanation for observations.
3. Modus Ponens: From $P$ and $P \implies Q$, infer $Q$.
4. Forward chaining starts from known facts and derives new facts; Backward chaining starts from goal query and searches for supporting facts.
5. MEU states that a rational agent should choose the action that maximizes expected utility $E[U(a)] = \sum_{s'} P(s'|a) U(s')$.

## 6-10. Manual Tracing
6. Pass 1: $A, B$ known. Rule $A \land B \implies C$ fires $\implies C$ added. Pass 2: Rule $C \implies D$ fires $\implies D$ added. Goal reached!
7. Goal $D$ requires $C$. Query $C$ requires $A \land B$. $A$ is true in KB, $B$ is true in KB. Goal $D$ proven True!
8. $E[U_1] = 0.8(100) + 0.2(0) = 80$. $E[U_2] = 0.5(150) + 0.5(-10) = 70$. Action 1 is optimal.
9. Cause $H_1$ probability $= 0.7$, $H_2$ probability $= 0.3$. Hypothesis $H_1$ selected as best explanation.
10. `Stack(A, B)`: Precond `Clear(B) & Holding(A)`, Effect `On(A,B) & Clear(A) & not Holding(A) & not Clear(B)`.

## 11-13. Coding Solutions
```python
class SimpleRuleEngine:
    def __init__(self, facts, rules):
        self.facts = set(facts)
        self.rules = rules # list of (antecedents, consequent)
        
    def forward_chain(self):
        added = True
        while added:
            added = False
            for ante, cons in self.rules:
                if cons not in self.facts and all(a in self.facts for a in ante):
                    self.facts.add(cons)
                    added = True
        return self.facts
```

## 14-16. Debugging Solutions
14. Add a `visited_goals` set in recursive backward chaining to break cyclic rule loops.
15. Replace `all(conditions)` with `any(conditions)` for logical OR rule evaluation.
16. Ensure probability values sum to 1.0 using `probs = [p/sum(raw_p) for p in raw_p]`.

## 17-26. Advanced Answers
17. Symbolic reasoning is exact, interpretable, and rule-based; ML is statistical, data-driven, and robust to noise.
18. STRIPS uses factored state predicates; state graphs use atomic or vector nodes.
19. Deterministic assumes certain outcomes; decision under uncertainty weighs expected values across probability distributions.
20-22. Real-world systems combine rule logic for hard constraints with probability models for soft estimations.
23-26. Interview responses should address knowledge acquisition limits, frame problems in STRIPS, and neuro-symbolic trends.
