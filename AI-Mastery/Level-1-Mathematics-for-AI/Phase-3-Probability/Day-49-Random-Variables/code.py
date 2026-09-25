import numpy as np

def simulate_dice_sum(n_samples=100000):
    die1 = np.random.randint(1, 7, size=n_samples)
    die2 = np.random.randint(1, 7, size=n_samples)
    X = die1 + die2  # Random variable X = sum of two dice
    return X

def main():
    print("--- Day 49: Random Variables ---")
    
    # 1. Discrete Random Variable Simulation
    n_sims = 100000
    X = simulate_dice_sum(n_sims)
    
    print("
1. Discrete RV: Sum of Two Dice Simulation:")
    for value in range(2, 13):
        prob = np.mean(X == value)
        print(f"  P(X = {value:2d}): {prob:.4f}")
        
    # 2. Continuous Random Variable Simulation
    # API Latency modeled as Exponential RV
    latency = np.random.exponential(scale=50.0, size=n_sims) # Mean 50ms
    print("
2. Continuous RV: Simulated API Latency (ms):")
    print(f"  Min Latency:    {np.min(latency):.2f} ms")
    print(f"  Max Latency:    {np.max(latency):.2f} ms")
    print(f"  Mean Latency:   {np.mean(latency):.2f} ms")
    print(f"  P(Latency < 20ms): {np.mean(latency < 20):.4f}")

if __name__ == "__main__":
    main()
