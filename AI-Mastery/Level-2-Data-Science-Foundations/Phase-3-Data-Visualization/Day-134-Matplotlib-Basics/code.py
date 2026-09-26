import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Day 134: Matplotlib Basics Demonstration ===")
    
    # Data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # OO Plotting
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=100)
    
    ax.plot(x, y1, color='#1f77b4', linewidth=2, label='Sine Wave')
    ax.plot(x, y2, color='#ff7f0e', linewidth=2, linestyle='--', label='Cosine Wave')
    
    ax.set_title("Sine & Cosine Functions (Matplotlib OO API)", fontsize=14, pad=12)
    ax.set_xlabel("Time (s)", fontsize=11)
    ax.set_ylabel("Amplitude", fontsize=11)
    
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.3, 1.3)
    
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', frameon=True)
    
    fig.tight_layout()
    fig.savefig("day134_oo_basics.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day134_oo_basics.png")

if __name__ == "__main__":
    main()
