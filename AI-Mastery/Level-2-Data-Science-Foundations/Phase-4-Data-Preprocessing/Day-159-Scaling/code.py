import numpy as np

def main():
    print("=== Day 159: Feature Scaling Impact Demonstration ===")
    
    # 2 Samples: [Age (years), Income ($)]
    sample_1 = np.array([25.0, 50000.0])
    sample_2 = np.array([26.0, 50000.0])
    sample_3 = np.array([25.0, 80000.0])
    
    print("Sample 1:", sample_1)
    print("Sample 2 (1 year older):", sample_2)
    print("Sample 3 ($30k higher income):", sample_3)
    
    # Euclidean Distances
    print("
Unscaled Euclidean Distance (1 to 2):", np.linalg.norm(sample_1 - sample_2))
    print("Unscaled Euclidean Distance (1 to 3):", np.linalg.norm(sample_1 - sample_3))

if __name__ == "__main__":
    main()
