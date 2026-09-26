import numpy as np

def main():
    # 1. Inspecting Dtypes
    i = np.array([1, 2, 3], dtype=np.int32)
    f = np.array([1.5, 2.5, 3.5], dtype=np.float64)
    
    print("Int32 itemsize:", i.itemsize, "bytes, total nbytes:", i.nbytes)
    print("Float64 itemsize:", f.itemsize, "bytes, total nbytes:", f.nbytes)
    
    # 2. Type Casting
    f_to_i = f.astype(np.int32)
    print("
Float array:", f)
    print("Casted to int32 (truncated):", f_to_i)
    
    # 3. Overflow Demonstration
    u8 = np.array([250], dtype=np.uint8)
    print("
Uint8 base value:", u8[0])
    print("Uint8 + 10 (overflow):", u8 + 10)
    
    # 4. Silent Truncation Warning
    arr_int = np.array([10, 20, 30])
    arr_int[0] = 99.99 # Decimal part discarded silently!
    print("
Array after assigning 99.99:", arr_int)

if __name__ == "__main__":
    main()
