import numpy as np

def main():
    # 1. Shape and Size Relationship
    arr = np.arange(12)
    print("1D Array:", arr)
    print("Shape:", arr.shape, "Size:", arr.size)
    
    # 2. Reshaping with -1
    m1 = arr.reshape(3, -1)
    m2 = arr.reshape(-1, 2)
    print("
Reshaped (3, -1) -> Shape:", m1.shape)
    print("Reshaped (-1, 2) -> Shape:", m2.shape)
    
    # 3. Flatten vs Ravel
    grid = np.array([[1, 2], [3, 4]])
    flat = grid.flatten() # Copy
    rav = grid.ravel()    # View
    
    rav[0] = 999
    print("
Original after ravel edit:
", grid)
    print("Flatten array (independent copy):", flat)
    
    # 4. Matrix Inner Dimensions Validation
    A = np.ones((5, 3))
    B = np.ones((3, 2))
    print("
Matrix A shape:", A.shape)
    print("Matrix B shape:", B.shape)
    print("A @ B shape:", (A @ B).shape)

if __name__ == "__main__":
    main()
