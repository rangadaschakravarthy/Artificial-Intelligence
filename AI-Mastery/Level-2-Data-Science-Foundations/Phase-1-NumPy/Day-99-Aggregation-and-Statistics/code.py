import numpy as np

def main():
    # 1. Summary Statistics
    data = np.array([10, 20, 30, 40, 50, 90])
    print("Data:", data)
    print("Mean:              ", np.mean(data))
    print("Median:            ", np.median(data))
    print("Population Var:    ", np.var(data))
    print("Sample Var (ddof=1):", np.var(data, ddof=1))
    print("Std Dev:           ", np.std(data))
    
    # 2. Argmax & Argmin
    probs = np.array([0.1, 0.65, 0.25])
    print("
Class Probabilities:", probs)
    print("Predicted Class Index (argmax):", np.argmax(probs))
    
    # 3. 2D Axis Reduction
    m = np.array([[1, 2, 3], [4, 5, 6]])
    print("
Matrix:
", m)
    print("Column Means (axis=0):", m.mean(axis=0))
    print("Row Means (axis=1):   ", m.mean(axis=1))
    
    # 4. NaN-Robust Aggregation
    nan_arr = np.array([10.0, np.nan, 30.0])
    print("
NaN Array:", nan_arr)
    print("Standard Mean:  ", np.mean(nan_arr))
    print("NaN-Robust Mean:", np.nanmean(nan_arr))

if __name__ == "__main__":
    main()
