import numpy as np

def classical_gram_schmidt(V: np.ndarray) -> np.ndarray:
    # Classical Gram-Schmidt (CGS) process.
    m, n = V.shape
    Q = np.zeros((m, n))
    for j in range(n):
        v = V[:, j].astype(float)
        for i in range(j):
            proj = np.dot(Q[:, i], V[:, j]) * Q[:, i]
            v -= proj
        Q[:, j] = v / np.linalg.norm(v)
    return Q

def qr_decomposition_gs(A: np.ndarray):
    # QR Decomposition using Modified Gram-Schmidt (MGS).
    m, n = A.shape
    V = A.copy().astype(float)
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for i in range(n):
        R[i, i] = np.linalg.norm(V[:, i])
        Q[:, i] = V[:, i] / R[i, i]
        for j in range(i + 1, n):
            R[i, j] = np.dot(Q[:, i], V[:, j])
            V[:, j] -= R[i, j] * Q[:, i]
            
    return Q, R

# Verification / Demo
if __name__ == "__main__":
    A = np.array([[1.0, 1.0],
                  [1.0, 0.0],
                  [0.0, 1.0]])
    
    print("Matrix A:\n", A)
    Q, R = qr_decomposition_gs(A)
    print("Gram-Schmidt Q:\n", Q)
    print("Upper Triangular R:\n", R)
    print("Reconstructed Q @ R:\n", Q @ R)
    print("Is Q @ R close to A?", np.allclose(A, Q @ R))
    
    Q_np, R_np = np.linalg.qr(A)
    print("NumPy Q:\n", Q_np)
