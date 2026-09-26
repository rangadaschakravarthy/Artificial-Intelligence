# Day 189 Worked Examples: DL vs Generative AI

## Example 1 — Practical: Categorizing Tasks
```python
tasks = [
    {"name": "ResNet-50 ImageNet Classifier", "cat": "Discriminative Deep Learning"},
    {"name": "Stable Diffusion Image Generator", "cat": "Generative AI (via Deep Diffusion)"},
    {"name": "BERT Sentiment Classifier", "cat": "Discriminative Deep Learning"},
    {"name": "GPT-4 Text Generator", "cat": "Generative AI (via Deep Transformer)"}
]

for t in tasks:
    print(f"Task: [{t['name']}] -> Category: {t['cat']}")
```
