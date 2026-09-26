import numpy as np

def main():
    # 1. Reshaping & Wildcard -1
    arr = np.arange(12)
    m = arr.reshape(3, 4)
    print("Original 1D:", arr)
    print("Reshaped 3x4:
", m)
    
    # 2. Ravel vs Flatten
    rav = m.ravel()    # View
    flat = m.flatten() # Copy
    print("
Ravel shares memory?", np.shares_memory(m, rav))
    print("Flatten shares memory?", np.shares_memory(m, flat))
    
    # 3. Transpose & Swapaxes
    print("
Transposed (4, 3):
", m.T)
    
    t3d = np.zeros((2, 3, 4))
    print("
3D Tensor shape:", t3d.shape)
    print("Transposed (2, 0, 1):", t3d.transpose(2, 0, 1).shape)
    print("Swapaxes (0, 2):", t3d.swapaxes(0, 2).shape)

if __name__ == "__main__":
    main()
