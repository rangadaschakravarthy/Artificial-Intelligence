# Day 101 Worked Examples: Random Number Generation

## Example 1 — Beginner: Generating Uniform & Normal Arrays
```python
import numpy as np

rng = np.random.default_rng(seed=42)

# Uniform random numbers between 0.0 and 1.0
uniform_arr = rng.random(size=(2, 3))

# Normal (Gaussian) distribution: Mean=0, Std=1
normal_arr = rng.normal(loc=0.0, scale=1.0, size=(2, 3))

print("Uniform Array:
", np.round(uniform_arr, 4))
print("Normal Array:
", np.round(normal_arr, 4))
```

## Example 2 — Practical: Random Sampling with and without Replacement
```python
import numpy as np

rng = np.random.default_rng(seed=100)
items = np.array(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'])

# Sample 3 items WITHOUT replacement (all unique)
sample_no_replace = rng.choice(items, size=3, replace=False)

# Sample 5 items WITH replacement (duplicates allowed)
sample_replace = rng.choice(items, size=5, replace=True)

print("Sample without replacement:", sample_no_replace)
print("Sample with replacement:   ", sample_replace)
```

## Example 3 — Intermediate: Creating Synthetic Feature Datasets
```python
import numpy as np

rng = np.random.default_rng(seed=42)

# Generate 5 synthetic samples with 2 features:
# Feature 0: Age ~ Uniform[18, 65]
# Feature 1: Income ~ Normal(μ=50, σ=15)
n_samples = 5
ages = rng.uniform(low=18, high=65, size=n_samples)
incomes = rng.normal(loc=50, scale=15, size=n_samples)

dataset = np.column_stack((ages, incomes))
print("Synthetic Dataset (Ages, Incomes):
", np.round(dataset, 2))
```

## Example 4 — Real Dataset: Simulating Coin Flips and Central Limit Theorem
```python
import numpy as np

rng = np.random.default_rng(seed=42)

# Simulate 1,000 trials of flipping 100 fair coins (Binomial p=0.5)
# Sum of 100 flips per trial
flips_sum = rng.binomial(n=100, p=0.5, size=1000)

print("Mean of 100 coin flips across 1000 trials:", np.mean(flips_sum)) # Expected ~50.0
print("Std of coin flips across 1000 trials:    ", np.round(np.std(flips_sum), 2)) # Expected ~5.0
```

## Example 5 — AI/ML Application: He (Kaiming) Weight Initialization
```python
import numpy as np

rng = np.random.default_rng(seed=42)

# Neural layer with 500 inputs, 100 outputs
fan_in = 500
fan_out = 100

# He Initialization: Normal(0, std = sqrt(2 / fan_in))
std_he = np.sqrt(2.0 / fan_in)
W_he = rng.normal(loc=0.0, scale=std_he, size=(fan_in, fan_out))

print("He Initialized Weight Matrix Shape:", W_he.shape)
print("Actual Weight Mean: ", np.round(W_he.mean(), 5))
print("Actual Weight Std:  ", np.round(W_he.std(), 5), "Expected:", np.round(std_he, 5))
```
