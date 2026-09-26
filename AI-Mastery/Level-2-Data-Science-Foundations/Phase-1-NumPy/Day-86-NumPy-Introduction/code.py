import numpy as np
import time

def main():
    print("NumPy Version:", np.__version__)
    
    # 1. Basic Array Creation
    arr = np.array([1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Dtype:", arr.dtype)
    print("Shape:", arr.shape)
    
    # 2. Benchmarking Python List vs NumPy Array
    N = 1000000
    py_list = list(range(N))
    np_arr = np.arange(N)
    
    t0 = time.time()
    py_res = [x * 3 for x in py_list]
    t1 = time.time()
    py_duration = t1 - t0
    
    t0 = time.time()
    np_res = np_arr * 3
    t1 = time.time()
    np_duration = t1 - t0
    
    print(f"
Time for {N} elements:")
    print(f"Python List: {py_duration:.5f}s")
    print(f"NumPy Array:  {np_duration:.5f}s")
    print(f"NumPy is {py_duration / np_duration:.2f}x faster!")

if __name__ == "__main__":
    main()
