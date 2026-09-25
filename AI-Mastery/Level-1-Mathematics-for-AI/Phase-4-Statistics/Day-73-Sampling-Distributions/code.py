import numpy as np

def simulate_sampling_distribution(pop_data: np.ndarray, n: int, num_samples: int = 1000):
    means = [np.mean(np.random.choice(pop_data, size=n, replace=True)) for _ in range(num_samples)]
    return {
        "pop_mean": float(np.mean(pop_data)),
        "sampling_mean": float(np.mean(means)),
        "theoretical_se": float(np.std(pop_data) / np.sqrt(n)),
        "empirical_se": float(np.std(means))
    }

if __name__ == "__main__":
    pop = np.random.uniform(0, 100, 10000)
    res = simulate_sampling_distribution(pop, n=25, num_samples=2000)
    print("Sampling Sim:", res)
