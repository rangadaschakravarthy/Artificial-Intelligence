import numpy as np

def main():
    # 1. Dimensions Demo
    scalar = np.array(100)
    vector = np.array([1, 2, 3])
    matrix = np.array([[1, 2], [3, 4]])
    tensor = np.ones((2, 3, 4))
    
    print("0D ndim:", scalar.ndim, "Shape:", scalar.shape)
    print("1D ndim:", vector.ndim, "Shape:", vector.shape)
    print("2D ndim:", matrix.ndim, "Shape:", matrix.shape)
    print("3D ndim:", tensor.ndim, "Shape:", tensor.shape)
    
    # 2. View vs Copy Verification
    base = np.array([10, 20, 30, 40])
    v = base[1:3]
    c = base[1:3].copy()
    
    print("
Shares memory (base, view):", np.shares_memory(base, v))
    print("Shares memory (base, copy):", np.shares_memory(base, c))
    
    # 3. Strides Inspection
    m = np.arange(6, dtype=np.int64).reshape(2, 3)
    print("
Matrix:
", m)
    print("Strides (int64):", m.strides) # (24 bytes per row, 8 bytes per col)
    print("Transposed Strides:", m.T.strides)

if __name__ == "__main__":
    main()
