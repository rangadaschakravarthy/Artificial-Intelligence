# Day 184 Worked Examples: Generative AI

## Example 1 — Practical: Simple Autoregressive Text Generator Simulation
```python
import random

# Simple N-gram Markov Chain Text Generator
corpus = "artificial intelligence models generate new data using deep learning probability distributions"
words = corpus.split()
bigrams = {words[i]: [] for i in range(len(words)-1)}
for i in range(len(words)-1):
    bigrams[words[i]].append(words[i+1])

def generate_text(start_word, length=5):
    curr = start_word
    result = [curr]
    for _ in range(length - 1):
        if curr in bigrams and bigrams[curr]:
            curr = random.choice(bigrams[curr])
            result.append(curr)
        else:
            break
    return " ".join(result)

print("Generated Text Sequence:", generate_text("generate", 4))
```
