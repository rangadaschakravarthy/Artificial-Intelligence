import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Day 139: Box Plots Demonstration ===")
    
    np.random.seed(42)
    g1 = np.random.normal(100, 10, 200)
    g2 = np.random.normal(90, 20, 200)
    g3 = np.random.normal(110, 5, 200)
    g3 = np.append(g3, [135, 140, 75]) # Outliers
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bp = ax.boxplot([g1, g2, g3], labels=['Group A', 'Group B', 'Group C'], patch_artist=True, showmeans=True)
    
    colors = ['#1f77b4', '#aec7e8', '#ff7f0e']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
        
    ax.set_title("Multi-Group Comparative Box Plot with Outliers", fontsize=13)
    ax.set_ylabel("Value Scale")
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)
    
    fig.tight_layout()
    fig.savefig("day139_box_plot.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day139_box_plot.png")

if __name__ == "__main__":
    main()
