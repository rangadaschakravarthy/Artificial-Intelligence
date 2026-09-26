import numpy as np

def main():
    # 1. 1D & 2D Indexing
    arr1d = np.array([10, 20, 30, 40, 50])
    print("1D First:", arr1d[0], "Last:", arr1d[-1])
    
    m2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    print("
2D Center:", m2d[1, 1])
    print("2D Top-Right:", m2d[0, 2])
    print("2D Bottom-Left:", m2d[-1, 0])
    
    # 2. Element Mutation
    m2d[0, 0] = 99
    print("
Mutated Matrix:
", m2d)
    
    # 3. 3D Tensor Indexing
    t3d = np.arange(12).reshape(2, 2, 3)
    print("
3D Tensor Element [1, 0, 2]:", t3d[1, 0, 2])

if __name__ == "__main__":
    main()
