import numpy as np

def main():
    # 1. Constant Creators
    z = np.zeros((2, 3))
    o = np.ones((2, 3))
    f = np.full((2, 3), 7)
    
    print("Zeros (2, 3):
", z)
    print("Full 7 (2, 3):
", f)
    
    # 2. Sequence Generators
    a = np.arange(0, 10, 2)
    l = np.linspace(0.0, 1.0, 5)
    
    print("
arange(0, 10, 2):", a)
    print("linspace(0.0, 1.0, 5):", l)
    
    # 3. Identity and Diagonal
    I = np.eye(3)
    D = np.diag([5, 10, 15])
    
    print("
Identity 3x3:
", I)
    print("Diagonal Matrix:
", D)
    
    # 4. Empty Buffer Allocation
    emp = np.empty((2, 2))
    print("
Uninitialized Empty Buffer (garbage values):
", emp)

if __name__ == "__main__":
    main()
