# Day 206 Worked Examples: Generative AI Revolution

## Example 1 — Practical: RLHF Pipeline Stage Simulation
```python
stages = [
    {"stage": "1. Base Pre-training", "objective": "Predict next token on petabytes of text data"},
    {"stage": "2. Instruction Tuning (SFT)", "objective": "Fine-tune on prompt-response demonstration pairs"},
    {"stage": "3. Reward Modeling", "objective": "Train reward model on human-ranked response pairs"},
    {"stage": "4. RL Optimization (PPO)", "objective": "Optimize model policy to maximize human preference reward"}
]

for s in stages:
    print(f"[{s['stage']}] -> {s['objective']}")
```
