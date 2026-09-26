# Day 207 Worked Examples: Modern AI History Synthesis

## Example 1 — Practical: Eras of AI Classification
```python
eras = [
    ("1956-1974", "Symbolic Exploration", "Logic Theorist, ELIZA, GPS"),
    ("1980-1987", "Expert Systems Boom", "MYCIN, XCON, LISP Machines"),
    ("1995-2010", "Statistical Machine Learning", "SVMs, Random Forests, HMMs"),
    ("2012-2017", "Deep Learning Era", "AlexNet, ResNet, AlphaGo"),
    ("2017-Present", "Transformer & GenAI Era", "BERT, GPT-4, Diffusion Models")
]

for period, era, tech in eras:
    print(f"[{period}] {era:30s} | Key Tech: {tech}")
```
