import numpy as np

def main():
    # 1. Determinant and Inverse
    A = np.array([[4.0, 7.0],
                  [2.0, 6.0]])
    print("Matrix A:
", A)
    print("Determinant:", np.linalg.det(A))
    print("Inverse A^-1:
", np.linalg.inv(A))
    
    # 2. Solving Linear System Ax = b
    # 3x + y = 9, x + 2y = 8
    coeffs = np.array([[3.0, 1.0], [1.0, 2.0]])
    depend = np.array([9.0, 8.0])
    sol = np.linalg.solve(coeffs, depend)
    print("
Linear System Solution [x, y]:", sol)
    
    # 3. Vector Norms
    v = np.array([3.0, -4.0])
    print("
Vector v:", v)
    print("L1 Norm:", np.linalg.norm(v, ord=1))
    print("L2 Norm:", np.linalg.norm(v, ord=2))
    
    # 4. Eigenvalues & Eigenvectors
    evals, evecs = np.linalg.eig(A)
    print("
Eigenvalues:", evals)
    print("Eigenvectors:
", evecs)

if __name__ == "__main__":
    main()
