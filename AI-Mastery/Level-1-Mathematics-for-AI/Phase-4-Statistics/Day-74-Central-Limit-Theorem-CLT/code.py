import numpy as np

def verify_clt(pop_type: str = "exponential", n: int = 50, num_samples: int = 2000):
    if pop_type == "exponential":
        pop = np.random.exponential(scale=2.0, size=100000)
    elif pop_type == "uniform":
        pop = np.random.uniform(low=0, high=10, size=100000)
    
    sample_means = [np.mean(np.random.choice(pop, size=n)) for _ in range(num_samples)]
    
    skewness = float(np.mean(((sample_means - np.mean(sample_means)) / np.std(sample_means))**3))
    return {
        "n": n,
        "sample_means_mean": float(np.mean(sample_means)),
        "sample_means_std": float(np.std(sample_means)),
        "skewness_near_zero": abs(skewness) < 0.1
    }

if __name__ == "__main__":
    print("CLT Verification (n=50):", verify_clt(n=50))
