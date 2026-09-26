import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Day 140: Subplots Demonstration ===")
    
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.5))
    
    axes[0, 0].plot(x, np.sin(x), color='#1f77b4', linewidth=2)
    axes[0, 0].set_title("Line Trend")
    axes[0, 0].grid(True, linestyle='--')
    
    axes[0, 1].bar(['Q1', 'Q2', 'Q3', 'Q4'], [400, 550, 480, 620], color='#2ca02c')
    axes[0, 1].set_title("Quarterly Sales")
    
    axes[1, 0].hist(np.random.normal(100, 15, 300), bins=20, color='#d62728', alpha=0.7, edgecolor='k')
    axes[1, 0].set_title("Distribution")
    
    axes[1, 1].scatter(x, 2 * x + np.random.normal(0, 3, 50), color='#9467bd')
    axes[1, 1].set_title("Bivariate Scatter")
    axes[1, 1].grid(True, linestyle='--')
    
    fig.suptitle("Executive Analytics 2x2 Dashboard", fontsize=15, y=0.98)
    fig.tight_layout()
    fig.savefig("day140_subplots_dashboard.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day140_subplots_dashboard.png")

if __name__ == "__main__":
    main()
