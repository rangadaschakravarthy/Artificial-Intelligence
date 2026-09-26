import numpy as np

def main():
    # 1. 1D Slicing
    a = np.array([0, 10, 20, 30, 40, 50, 60])
    print("Full 1D:", a)
    print("Slice [1:5]:", a[1:5])
    print("Step [::2]:", a[::2])
    print("Reversed:", a[::-1])
    
    # 2. 2D Slicing
    m = np.arange(16).reshape(4, 4)
    print("
Full 4x4 Matrix:
", m)
    print("Top-Right 2x2:
", m[:2, 2:])
    print("All rows, Col index 1 (1D):", m[:, 1], "Shape:", m[:, 1].shape)
    print("All rows, Col index 1:2 (2D):
", m[:, 1:2], "Shape:", m[:, 1:2].shape)
    
    # 3. View Mutation Verification
    sub = m[:2, :2]
    sub[0, 0] = 999
    print("
Matrix after sub-matrix edit:
", m)

if __name__ == "__main__":
    main()
