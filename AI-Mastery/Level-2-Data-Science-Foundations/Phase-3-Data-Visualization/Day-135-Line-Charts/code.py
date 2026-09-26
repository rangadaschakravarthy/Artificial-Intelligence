import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Day 135: Line Charts Demonstration ===")
    
    x = np.linspace(1, 12, 12)
    y_sales = [100, 120, 115, 140, 160, 155, 175, 190, 185, 210, 230, 250]
    y_err = [10, 12, 11, 14, 16, 15, 17, 19, 18, 21, 23, 25]
    
    fig, ax = plt.subplots(figsize=(9, 4.5))
    
    ax.plot(x, y_sales, color='#1f77b4', marker='o', linewidth=2.5, label='Monthly Revenue ($K)')
    ax.fill_between(x, np.array(y_sales) - np.array(y_err), np.array(y_sales) + np.array(y_err), color='#1f77b4', alpha=0.2, label='Confidence Interval')
    
    ax.set_title("Monthly Revenue Trend with Confidence Bounds", fontsize=13)
    ax.set_xlabel("Month of Year")
    ax.set_ylabel("Revenue ($K)")
    ax.set_xticks(x)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    
    fig.tight_layout()
    fig.savefig("day135_line_chart.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day135_line_chart.png")

if __name__ == "__main__":
    main()
