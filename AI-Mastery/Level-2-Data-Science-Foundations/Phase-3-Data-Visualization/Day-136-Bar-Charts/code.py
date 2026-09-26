import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Day 136: Bar Charts Demonstration ===")
    
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
    sales = [450, 320, 280, 210, 150]
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(categories[::-1], sales[::-1], color='#2ca02c', height=0.6)
    
    ax.set_title("Category Sales Performance (Sorted)", fontsize=13)
    ax.set_xlabel("Sales Revenue ($K)")
    ax.bar_label(bars, fmt='$%dK', padding=5)
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)
    
    fig.tight_layout()
    fig.savefig("day136_bar_chart.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day136_bar_chart.png")

if __name__ == "__main__":
    main()
