# Day 101 Theory: Random Number Generation

### 1. What Is It?
NumPy random generation routines construct arrays of pseudo-random numbers sampled from theoretical probability distributions (Uniform, Gaussian, Binomial, Poisson).

### 2. Why Does It Exist?
Data science and machine learning require stochastic processes for weight initialization, random data shuffling, bootstrap sampling, and noise simulation.

### 3. Intuition
Random number generators are deterministic mathematical formulas (like PCG64) that produce sequences of numbers so complex and uniform that they appear completely random to statistical tests.

### 4. Syntax
```python
import numpy as np

# Modern Generator API (Recommended)
rng = np.random.default_rng(seed=42)

# Uniform random floats in [0.0, 1.0)
u = rng.random((2, 3))

# Normal distribution N(mean, std)
n = rng.normal(loc=0.0, scale=1.0, size=(3, 3))

# Random integers
i = rng.integers(low=1, high=10, size=5)

# Random choice sampling
sample = rng.choice([10, 20, 30, 40], size=2, replace=False)
```

### 5. Parameters
- `seed`: Integer initializing the pseudo-random state engine.
- `replace`: Boolean in `choice()` specifying sampling with or without replacement.

### 6. How It Works
The modern `Generator` uses the Permuted Congruential Generator (PCG64) bit-generator engine to generate 64-bit random integers, which are then transformed into specific probability distributions using inversion or Box-Muller algorithms.

### 7. Simple Example
```python
import numpy as np
rng = np.random.default_rng(42)
print(rng.normal(0, 1, size=3))
```

### 8. Intermediate Example
```python
import numpy as np
rng = np.random.default_rng(42)
dataset = np.arange(10)
rng.shuffle(dataset) # In-place shuffle
print("Shuffled Dataset:", dataset)
```

### 9. Output Interpretation
`rng.shuffle` permutes array element order in-place using the Fisher-Yates algorithm.

### 10. Common Mistakes
- Using legacy `np.random.seed(42)` instead of recommended thread-safe `default_rng(42)`.
- Forgetting to set a random seed, making scientific experiments un-reproducible.

### 11. Data Science Connection
Randomly splitting data tables into train/test sets and generating bootstrap confidence interval resamples.

### 12. AI/ML Connection
Weight initialization (Xavier / He initialization) and dropout regularization in Neural Networks.

### 13. Interview Insight
Question: "Why should you use `np.random.default_rng()` over legacy `np.random.rand()`?"
Answer: 1) `default_rng` uses PCG64, a faster and statistically superior bit generator than legacy MT19937 (Mersenne Twister). 2) It is object-oriented and thread-safe, avoiding global state pollution across multi-threaded applications.

### 14. Summary
Use `default_rng(seed)` for reproducible, thread-safe random generation. Sample from Uniform, Normal, or Discrete distributions for ML model initialization and evaluation.
