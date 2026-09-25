import numpy as np

def evaluate_estimator(true_mu: float = 10.0, n: int = 25, num_trials: int = 5000):
    estimates = [np.mean(np.random.normal(loc=true_mu, scale=2.0, size=n)) for _ in range(num_trials)]
    bias = float(np.mean(estimates) - true_mu)
    var = float(np.var(estimates))
    mse = float(np.mean((np.array(estimates) - true_mu)**2))
    return {"bias": bias, "variance": var, "mse": mse, "bias_sq_plus_var": bias**2 + var}

if __name__ == "__main__":
    print("Estimator Evaluation:", evaluate_estimator())
