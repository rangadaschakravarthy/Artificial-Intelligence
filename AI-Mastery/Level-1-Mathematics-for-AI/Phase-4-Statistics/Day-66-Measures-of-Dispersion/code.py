import numpy as np

def detect_outliers_iqr(data: list):
    arr = np.array(data)
    q1, q3 = np.percentile(arr, [25, 75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = arr[(arr < lower) | (arr > upper)]
    return {"q1": q1, "q3": q3, "iqr": iqr, "lower": lower, "upper": upper, "outliers": outliers.tolist()}

if __name__ == "__main__":
    data = [1, 10, 12, 13, 15, 17, 85]
    print("Outlier Report:", detect_outliers_iqr(data))
