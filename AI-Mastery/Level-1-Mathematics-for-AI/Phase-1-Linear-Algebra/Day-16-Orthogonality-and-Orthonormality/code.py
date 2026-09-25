import numpy as np

def is_orthogonal(u: np.ndarray, v: np.ndarray, tol: float = 1e-9) -> bool:
    # Check if two vectors are orthogonal.
    return abs(np.dot(u, v)) < tol

def normalize(v: np.ndarray) -> np.ndarray:
    # Normalize vector to unit length.
    norm = np.linalg.norm(v)
    if norm < 1e-9:
        raise ValueError("Cannot normalize zero vector.")
    return v / norm

def is_orthogonal_matrix(Q: np.ndarray, tol: float = 1e-9) -> bool:
    # Check if a matrix Q is orthogonal (Q^T Q = I).
    if Q.shape[0] != Q.shape[1]:
        return False
    identity = np.eye(Q.shape[0])
    return np.allclose(Q.T @ Q, identity, atol=tol)

# Verification / Demo
if __name__ == "__main__":
    u = np.array([3.0, 4.0])
    v = np.array([-4.0, 3.0])
    
    print(f"u . v = {np.dot(u, v)}")
    print(f"Is u ⊥ v? {is_orthogonal(u, v)}")
    
    u_hat = normalize(u)
    v_hat = normalize(v)
    print(f"Normalized u: {u_hat}, Norm: {np.linalg.norm(u_hat):.4f}")
    print(f"Normalized v: {v_hat}, Norm: {np.linalg.norm(v_hat):.4f}")
    
    theta = np.pi / 4 # 45 degrees
    Q = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    
    print("Matrix Q:\n", Q)
    print("Is Q orthogonal?", is_orthogonal_matrix(Q))
    print("Q^T @ Q:\n", np.round(Q.T @ Q, 4))
