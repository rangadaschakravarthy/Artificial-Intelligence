# Theory — Day 222: AI Decision Making Under Uncertainty

## 1. What Is It?
AI Decision Making Under Uncertainty is an essential component of AI problem solving. Probabilistic decision making, maximum expected utility (MEU), and belief state spaces.

## 2. Why Does It Exist?
Search alone is blind to rule relationships, uncertainty, and high-level goal planning. AI Decision Making Under Uncertainty provides structured decision-making mechanisms.

## 3. Intuition
Imagine a detective analyzing a crime scene. Deduction derives necessary facts from known rules; induction learns general patterns from evidence; abduction identifies the most probable explanation for observed symptoms.

## 4. Syntax / Notation
Formal Inference / Planning Syntax:
$$\text{KB} \models \alpha \quad \iff \quad M(\text{KB}) \subseteq M(\alpha)$$
Where $\text{KB}$ is the Knowledge Base, $\alpha$ is a target proposition, and $M(\cdot)$ is the set of models.

## 5. Parameters / Environment
- Knowledge base size $|KB|$
- Inference depth $d$
- Certainty factors / Probabilities $P(E | H)$

## 6. How It Works
1. Encode domain facts and production rules into KB.
2. Receive percepts or goal queries.
3. Apply inference engine (forward/backward chaining or resolution) to evaluate target state.
4. Output proven facts, plan steps, or optimal decision choices.

## 7. Simple Example
Rule: $\text{If } \text{Rain} \implies \text{Wet Ground}$.
Fact: $\text{Rain}$ is True.
Inference: $\text{Wet Ground}$ is proven True by Modus Ponens.

## 8. Intermediate Example
STRIPS Planning Action:
`Action(Fly(p, from, to), PRECOND: At(p, from) and Plane(p), EFFECT: At(p, to) and not At(p, from))`

## 9. Output Interpretation
The engine outputs a logical proof tree, an action sequence satisfying preconditions, or a numerical expected utility value.

## 10. Common Mistakes
- Confusing material implication ($P \implies Q$) with causal necessity or biconditional equality.
- Infinite loops in backward chaining when rules contain recursive cycles.

## 11. Data Science Connection
Inductive reasoning is the theoretical counterpart of statistical machine learning (generalizing models from empirical sample distributions).

## 12. AI/ML Connection
Combines with neural networks in Neuro-Symbolic AI to provide explainable decision paths and safety constraints.

## 13. Interview Insight
When asked to compare symbolic vs probabilistic reasoning, emphasize that symbolic reasoning handles exact rule constraints while probabilistic reasoning handles noise and partial observability.

## 14. Summary
AI Decision Making Under Uncertainty enables AI agents to infer unobserved truths, plan multi-step goal paths, and evaluate optimal decisions under real-world constraints.
