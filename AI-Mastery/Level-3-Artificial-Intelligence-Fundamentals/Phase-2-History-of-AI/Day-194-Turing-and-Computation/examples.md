# Day 194 Worked Examples: Turing and Computation

## Example 1 — Practical: Simple Turing Machine Simulation
```python
# 1D Tape Incrementor Turing Machine
def turing_increment(tape):
    # Reads binary tape, increments value
    val = int("".join(tape), 2) + 1
    return list(bin(val)[2:])

tape = ['1', '0', '1'] # Binary 5
print("Tape Input: ", tape)
print("Tape Output:", turing_increment(tape)) # Binary 6 ('1', '1', '0')
```
