import numpy as np

def compute_sample_stats(data: list) -> dict:
    arr = np.array(data)
    return {
        "n": len(arr),
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr, ddof=1))
    }

if __name__ == "__main__":
    sample = [12, 15, 18, 21, 24]
    res = compute_sample_stats(sample)
    print("Sample Stats:", res)
