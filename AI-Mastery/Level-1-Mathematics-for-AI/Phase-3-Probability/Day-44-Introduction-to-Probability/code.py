import numpy as np

def coin_toss_simulation(num_flips=10000):
    # Simulate coin tosses: 1 for Heads, 0 for Tails
    flips = np.random.choice([0, 1], size=num_flips, p=[0.5, 0.5])
    empirical_prob_heads = np.mean(flips)
    return empirical_prob_heads

def softmax(logits):
    exp_logits = np.exp(logits - np.max(logits)) # Numerical stability offset
    return exp_logits / np.sum(exp_logits)

def main():
    print("--- Day 44: Introduction to Probability ---")
    
    # 1. Empirical Coin Flip Simulation
    flips_counts = [10, 100, 1000, 100000]
    print("
1. Law of Large Numbers (Coin Flip Simulation):")
    for n in flips_counts:
        prob = coin_toss_simulation(n)
        print(f"  Flips: {n:6d} | Empirical P(Heads): {prob:.4f}")
        
    # 2. Softmax Probability Conversion in Machine Learning
    raw_logits = np.array([3.0, 1.0, 0.0])
    probabilities = softmax(raw_logits)
    print("
2. Softmax Conversion of Logits:")
    print(f"  Raw Logits:    {raw_logits}")
    print(f"  Probabilities: {np.round(probabilities, 4)}")
    print(f"  Sum of Probs:  {np.sum(probabilities):.4f}")

if __name__ == "__main__":
    main()
