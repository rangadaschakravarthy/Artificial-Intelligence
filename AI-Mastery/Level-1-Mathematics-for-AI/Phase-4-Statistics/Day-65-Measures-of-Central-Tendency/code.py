import numpy as np
from scipy import stats

def compute_all_centers(data: list) -> dict:
    arr = np.array(data)
    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "mode": float(stats.mode(arr, keepdims=True).mode[0]),
        "gmean": float(stats.gmean(arr)),
        "hmean": float(stats.hmean(arr))
    }

if __name__ == "__main__":
    data = [2, 4, 4, 4, 10, 100]
    print("Central Tendencies:", compute_all_centers(data))
