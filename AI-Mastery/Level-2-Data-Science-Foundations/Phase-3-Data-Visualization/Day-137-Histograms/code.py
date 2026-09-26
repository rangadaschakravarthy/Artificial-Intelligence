import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Day 137: Histograms Demonstration ===")
    
    np.random.seed(42)
    income = np.random.exponential(scale=50000, size=1000)
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.hist(income, bins=35, color='#d62728', alpha=0.7, edgecolor='black')
    
    ax.set_title("Right-Skewed Household Income Distribution", fontsize=13)
    ax.set_xlabel("Income ($)")
    ax.set_ylabel("Frequency (Count)")
    ax.grid(True, linestyle='--', alpha=0.5)
    
    fig.tight_layout()
    fig.savefig("day137_histogram.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day137_histogram.png")

if __name__ == "__main__":
    main()
