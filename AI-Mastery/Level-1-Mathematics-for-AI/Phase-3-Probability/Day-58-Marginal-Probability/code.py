import numpy as np

def main():
    print("--- Day 58: Marginal Probability ---")
    
    # 2D Joint PMF Table (2x3)
    # Rows: X in {0, 1}, Columns: Y in {0, 1, 2}
    joint_pmf = np.array([
        [0.10, 0.20, 0.10], # X = 0
        [0.15, 0.30, 0.15]  # X = 1
    ])
    
    # 1. Marginalization along Axis 1 (Sum out Y -> Marginal P(X))
    marginal_X = np.sum(joint_pmf, axis=1)
    
    # 2. Marginalization along Axis 0 (Sum out X -> Marginal P(Y))
    marginal_Y = np.sum(joint_pmf, axis=0)
    
    print("
1. Joint PMF Array (2x3):")
    print(joint_pmf)
    
    print("
2. Marginal Distribution P(X):")
    print(f"  P(X = 0): {marginal_X[0]:.2f}")
    print(f"  P(X = 1): {marginal_X[1]:.2f}")
    print(f"  Sum P(X): {np.sum(marginal_X):.2f}")
    
    print("
3. Marginal Distribution P(Y):")
    print(f"  P(Y = 0): {marginal_Y[0]:.2f}")
    print(f"  P(Y = 1): {marginal_Y[1]:.2f}")
    print(f"  P(Y = 2): {marginal_Y[2]:.2f}")
    print(f"  Sum P(Y): {np.sum(marginal_Y):.2f}")

if __name__ == "__main__":
    main()
