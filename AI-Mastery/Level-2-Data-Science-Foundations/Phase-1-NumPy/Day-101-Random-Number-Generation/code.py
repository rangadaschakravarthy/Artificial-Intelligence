import numpy as np

def main():
    # 1. Instantiate Generator
    rng = np.random.default_rng(seed=42)
    
    # 2. Uniform & Normal Distributions
    u = rng.uniform(low=0.0, high=10.0, size=5)
    n = rng.normal(loc=0.0, scale=1.0, size=(2, 3))
    
    print("Uniform [0, 10]:
", np.round(u, 2))
    print("
Normal N(0, 1):
", np.round(n, 4))
    
    # 3. Discrete Integers & Choice
    ints = rng.integers(low=1, high=7, size=10) # Roll a 6-sided die 10 times
    items = np.array(['A', 'B', 'C', 'D'])
    sampled = rng.choice(items, size=2, replace=False)
    
    print("
Dice Rolls (1 to 6):", ints)
    print("Random Choice (No Replace):", sampled)
    
    # 4. In-Place Shuffle
    arr = np.arange(5)
    rng.shuffle(arr)
    print("
Shuffled Array:", arr)

if __name__ == "__main__":
    main()
