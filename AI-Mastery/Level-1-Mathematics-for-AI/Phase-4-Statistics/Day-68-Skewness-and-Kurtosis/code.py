import numpy as np
from scipy import stats

def analyze_shape(data: list) -> dict:
    arr = np.array(data)
    skew = float(stats.skew(arr))
    kurt = float(stats.kurtosis(arr)) # Returns Excess Kurtosis by default
    return {
        "skewness": skew,
        "excess_kurtosis": kurt,
        "is_symmetric": abs(skew) < 0.5,
        "tail_type": "Leptokurtic" if kurt > 0 else "Platykurtic"
    }

if __name__ == "__main__":
    skewed_data = [1, 2, 2, 3, 4, 5, 10, 25, 100]
    print("Shape Analysis:", analyze_shape(skewed_data))
