import numpy as np

def encode_nominal(categories: list) -> np.ndarray:
    unique = sorted(list(set(categories)))
    mapping = {cat: i for i, cat in enumerate(unique)}
    one_hot = np.zeros((len(categories), len(unique)))
    for row, cat in enumerate(categories):
        one_hot[row, mapping[cat]] = 1.0
    return one_hot, unique

if __name__ == "__main__":
    cats = ["Red", "Green", "Blue", "Red"]
    encoded, labels = encode_nominal(cats)
    print("Labels:", labels)
    print("One-Hot Matrix:
", encoded)
