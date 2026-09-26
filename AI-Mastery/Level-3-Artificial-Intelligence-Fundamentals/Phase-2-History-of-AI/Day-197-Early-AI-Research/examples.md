# Day 197 Worked Examples: Early AI Research & Logic

## Example 1 — Practical: ELIZA Pattern-Matching Chatbot Simulation
```python
def eliza_response(user_input):
    rules = {
        "mother": "Tell me more about your mother.",
        "sad": "Why do you say you are sad?",
        "always": "Can you think of a specific example?"
    }
    for key, response in rules.items():
        if key in user_input.lower():
            return response
    return "Please continue."

print("User: I feel sad today.")
print("ELIZA:", eliza_response("I feel sad today."))
```
