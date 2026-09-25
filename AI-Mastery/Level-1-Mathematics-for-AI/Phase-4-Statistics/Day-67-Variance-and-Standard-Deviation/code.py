import numpy as np

def compute_variances(data: list) -> dict:
    arr = np.array(data)
    pop_var = np.var(arr, ddof=0)
    sample_var = np.var(arr, ddof=1)
    return {
        "pop_var": float(pop_var),
        "pop_std": float(np.sqrt(pop_var)),
        "sample_var": float(sample_var),
        "sample_std": float(np.sqrt(sample_var))
    }

if __name__ == "__main__":
    data = [4, 8, 12]
    print("Variance Stats:", compute_variances(data))
