import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Day 141: Customizing Matplotlib Demonstration ===")
    
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['font.size'] = 11
    
    x = np.linspace(0, 10, 100)
    y = np.exp(-x / 3) * np.sin(2 * x)
    
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    ax.plot(x, y, color='#d62728', linewidth=2.5, label='Damped Oscillation')
    
    # Annotate local maximum
    max_x, max_y = x[12], y[12]
    ax.annotate('Primary Peak', xy=(max_x, max_y), xytext=(max_x + 1.2, max_y + 0.2),
                arrowprops=dict(facecolor='black', shrink=0.08, width=1.5, headwidth=8),
                fontsize=11, fontweight='bold')
    
    ax.set_title("Publication-Ready Custom Signal Visualization", fontsize=14, pad=15)
    ax.set_xlabel("Time Constant (s)")
    ax.set_ylabel("Response Amplitude")
    
    # Despine
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    fig.tight_layout()
    fig.savefig("day141_customized_plot.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day141_customized_plot.png")

if __name__ == "__main__":
    main()
