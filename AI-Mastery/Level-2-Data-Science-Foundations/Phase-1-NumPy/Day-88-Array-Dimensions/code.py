import numpy as np

def main():
    # 1. Axis Operations Demo
    m = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print("Matrix (2, 3):
", m)
    print("Sum axis=0 (down rows):", m.sum(axis=0)) # Shape (3,)
    print("Sum axis=1 (across cols):", m.sum(axis=1)) # Shape (2,)
    
    # 2. keepdims parameter
    sum_kd = m.sum(axis=1, keepdims=True)
    print("Sum axis=1 (keepdims=True) shape:", sum_kd.shape) # Shape (2, 1)
    
    # 3. Dimension Expansion
    v = np.array([10, 20, 30]) # (3,)
    v_col = v[:, np.newaxis]   # (3, 1)
    v_row = v[np.newaxis, :]   # (1, 3)
    
    print("
Original 1D vector:", v.shape)
    print("Column Vector Shape:", v_col.shape)
    print("Row Vector Shape:", v_row.shape)
    
    # 4. Squeezing
    dummy = np.zeros((1, 5, 1))
    print("
Dummy tensor shape:", dummy.shape)
    print("Squeezed shape:", np.squeeze(dummy).shape)

if __name__ == "__main__":
    main()
