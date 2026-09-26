import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Day 138: Scatter Plots Demonstration ===")
    
    np.random.seed(42)
    x = np.random.normal(50, 10, 100)
    y = 2.5 * x + np.random.normal(0, 15, 100)
    scores = np.random.uniform(10, 100, 100)
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    sc = ax.scatter(x, y, c=scores, cmap='viridis', s=60, alpha=0.8, edgecolors='k')
    
    # Trendline
    z = np.polyfit(x, y, 1)
    ax.plot(np.unique(x), np.poly1d(z)(np.unique(x)), color='red', linestyle='--', linewidth=2, label='Fit Line')
    
    ax.set_title("Bivariate Relationship with Trendline & Color Map", fontsize=13)
    ax.set_xlabel("Feature X")
    ax.set_ylabel("Feature Y")
    fig.colorbar(sc, ax=ax, label='Score Metric')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    
    fig.tight_layout()
    fig.savefig("day138_scatter_plot.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day138_scatter_plot.png")

if __name__ == "__main__":
    main()
