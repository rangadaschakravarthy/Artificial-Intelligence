# Day 196 Worked Examples: Dartmouth Conference

## Example 1 — Practical: Founding Figures Database
```python
founders = [
    {"name": "John McCarthy", "contribution": "Coined term 'AI', LISP language"},
    {"name": "Marvin Minsky", "contribution": "Cognitive frames, neural nets"},
    {"name": "Claude Shannon", "contribution": "Information Theory, chess computer theory"},
    {"name": "Allen Newell & Herbert Simon", "contribution": "Logic Theorist (First AI program)"}
]

for f in founders:
    print(f"Founder: {f['name']} -> Contribution: {f['contribution']}")
```
