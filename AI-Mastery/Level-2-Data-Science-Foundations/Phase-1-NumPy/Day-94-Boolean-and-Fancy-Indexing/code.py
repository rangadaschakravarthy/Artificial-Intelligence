import numpy as np

def main():
    # 1. Basic Boolean Masking
    arr = np.array([10, 25, 30, 45, 50, 15])
    mask = arr > 20
    print("Array:", arr)
    print("Mask (arr > 20):", mask)
    print("Filtered arr[arr > 20]:", arr[mask])
    
    # 2. Combined Conditions
    combined = arr[(arr >= 20) & (arr <= 45)]
    print("
Combined (20 <= arr <= 45):", combined)
    
    # 3. Mask Assignment (In-Place Edit)
    a = np.array([1, -5, 3, -8, 5])
    a[a < 0] = 0
    print("
Zeroed negative elements:", a)
    
    # 4. Fancy Indexing
    m = np.arange(12).reshape(4, 3)
    print("
Matrix:
", m)
    print("Fancy Row Selection [3, 0]:
", m[[3, 0]])

if __name__ == "__main__":
    main()
