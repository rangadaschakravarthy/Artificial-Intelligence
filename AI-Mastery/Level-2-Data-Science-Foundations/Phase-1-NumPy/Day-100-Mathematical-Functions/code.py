import numpy as np

def main():
    # 1. Exponential & Logarithms
    x = np.array([1.0, 2.0, 3.0])
    print("x:      ", x)
    print("exp(x): ", np.round(np.exp(x), 4))
    print("log(x): ", np.round(np.log(x), 4))
    
    # 2. Log1p Stability Demo
    small = 1e-15
    print("
Standard log(1 + 1e-15):", np.log(1.0 + small))
    print("Stable log1p(1e-15):    ", np.log1p(small))
    
    # 3. Rounding Methods
    vals = np.array([-2.7, -1.5, 1.5, 2.7])
    print("
Values: ", vals)
    print("Floor:  ", np.floor(vals))
    print("Ceil:   ", np.ceil(vals))
    print("Round:  ", np.round(vals))
    
    # 4. Sigmoid Activation Function
    z = np.array([-2.0, 0.0, 2.0])
    sigmoid = 1.0 / (1.0 + np.exp(-z))
    print("
Sigmoid Activation Output:", np.round(sigmoid, 4))

if __name__ == "__main__":
    main()
