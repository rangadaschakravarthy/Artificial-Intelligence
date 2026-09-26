import numpy as np
import time

def main():
    # 1. Benchmarking Vectorization Speed
    N = 2000000
    py_list = list(range(N))
    np_arr = np.arange(N)
    
    t0 = time.time()
    py_res = [x * 2 + 1 for x in py_list]
    t_loop = time.time() - t0
    
    t0 = time.time()
    np_res = np_arr * 2 + 1
    t_vec = time.time() - t0
    
    print(f"Time for {N} elements:")
    print(f"Python Loop: {t_loop:.4f}s")
    print(f"NumPy Vector: {t_vec:.4f}s")
    print(f"Vector Speedup: {t_loop / t_vec:.1f}x faster!")
    
    # 2. Vectorized Conditional (np.where)
    scores = np.array([45, 82, 60, 95, 30])
    status = np.where(scores >= 60, 'Pass', 'Fail')
    print("
Scores:", scores)
    print("Vectorized Status:", status)
    
    # 3. Vectorized ReLU Activation
    x = np.array([-3.0, 1.5, -0.5, 4.0])
    relu = np.maximum(0.0, x)
    print("
Input x:", x)
    print("Vectorized ReLU:", relu)

if __name__ == "__main__":
    main()
