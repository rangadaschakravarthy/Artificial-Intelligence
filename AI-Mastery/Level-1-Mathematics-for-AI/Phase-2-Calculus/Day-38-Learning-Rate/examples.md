# Examples — Learning Rate

## Example 1 — Very Easy
Too Small $\eta = 0.0001$: Loss decreases by $0.00001$ per epoch (takes 100,000 epochs).

## Example 2 — Beginner
Too Large $\eta = 1.5$: Loss jumps $4.0 \to 16.0 \to 256.0 \to \text{NaN}$ (Divergence!).

## Example 3 — Intermediate
Optimal $\eta = 0.01$: Loss decreases smoothly $4.0 \to 2.1 \to 0.9 \to 0.05$.

## Example 4 — AI/ML Example
Cosine Annealing: $\eta$ smoothly decreases from $0.1 \to 0.001$ over 100 epochs following cosine curve.

## Example 5 — Real-World Interpretation
Linear Warmup: $\eta$ increases linearly from $0 \to 0.001$ for first 1,000 steps, then decays.
