import numpy as np
from scipy import stats

def compute_confidence_intervals(data: list, confidence: float = 0.95) -> dict:
    arr = np.array(data)
    n = len(arr)
    mean = np.mean(arr)
    sem = stats.sem(arr)
    
    # Z-interval
    z_crit = stats.norm.ppf((1 + confidence) / 2)
    z_ci = (mean - z_crit * sem, mean + z_crit * sem)
    
    # t-interval
    t_ci = stats.t.interval(confidence, df=n-1, loc=mean, scale=sem)
    
    return {
        "mean": float(mean),
        "sem": float(sem),
        "z_ci": (float(z_ci[0]), float(z_ci[1])),
        "t_ci": (float(t_ci[0]), float(t_ci[1]))
    }

if __name__ == "__main__":
    data = [12, 15, 18, 22, 25, 28, 30]
    print("CI Report:", compute_confidence_intervals(data))
