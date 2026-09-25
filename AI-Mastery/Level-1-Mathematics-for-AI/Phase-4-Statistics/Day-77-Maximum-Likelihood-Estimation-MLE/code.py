import numpy as np
from scipy.optimize import minimize

def fit_gaussian_mle(data: np.ndarray):
    # Negative Log-Likelihood for Gaussian (mu, sigma)
    def nll(params):
        mu, sigma = params
        if sigma <= 0:
            return 1e10
        n = len(data)
        log_lik = - (n / 2) * np.log(2 * np.pi * sigma**2) - (1 / (2 * sigma**2)) * np.sum((data - mu)**2)
        return -log_lik

    init_params = [0.0, 1.0]
    res = minimize(nll, init_params, method='L-BFGS-B', bounds=[(None, None), (1e-5, None)])
    return {
        "mle_mu": float(res.x[0]),
        "mle_sigma": float(res.x[1]),
        "sample_mean": float(np.mean(data)),
        "sample_std": float(np.std(data))
    }

if __name__ == "__main__":
    np.random.seed(42)
    sample_data = np.random.normal(loc=5.0, scale=2.0, size=500)
    print("MLE Fit Result:", fit_gaussian_mle(sample_data))
