import matplotlib.pyplot as plt

def main():
    print("=== Day 150: Data Storytelling Demonstration ===")
    
    regions = ['North', 'East', 'South', 'West']
    churn_rate = [4.2, 3.8, 12.5, 4.1]
    
    # Strategic Color: Gray out baseline regions, Highlight South in Red
    colors = ['#cccccc', '#cccccc', '#d62728', '#cccccc']
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(regions, churn_rate, color=colors, width=0.55)
    
    # Action Headline Title
    ax.set_title("Southern Region Exhibited 3x Higher Customer Churn Rate", fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel("Churn Rate (%)")
    
    # Despine & Annotate
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(bars, fmt='%.1f%%', padding=3, fontweight='bold')
    
    fig.tight_layout()
    fig.savefig("day150_data_storytelling.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day150_data_storytelling.png")

if __name__ == "__main__":
    main()
