import numpy as np

def main():
    print("=== Day 183: Deep Learning Single Neuron Simulation ===")
    inputs = np.array([1.0, 2.0, 3.0])
    weights = np.array([0.2, 0.8, -0.5])
    bias = 1.0
    z = np.dot(inputs, weights) + bias
    print("Neuron Output z:", z)

if __name__ == "__main__":
    main()
