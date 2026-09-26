# Day 178 Worked Examples: Narrow AI

## Example 1 — Practical: Demonstrating Domain Brittleness
```python
class NarrowSpamFilter:
    def predict(self, text):
        keywords = ["win", "free", "cash", "prize"]
        return "Spam" if any(w in text.lower() for w in keywords) else "Ham"

filter_agent = NarrowSpamFilter()
print("Task 1 (Spam Check):", filter_agent.predict("Win free cash now!"))

# Fails completely if asked to perform image classification or routing!
print("Task 2 (Attempt Image Classification): Error - Domain out of bounds!")
```
