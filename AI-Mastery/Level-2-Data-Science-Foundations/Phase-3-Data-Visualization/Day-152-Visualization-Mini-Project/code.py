import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np

def main():
    print("=== Day 152: Exploratory Data Analysis Dashboard Mini Project ===")
    
    # 1. Dataset Generation
    np.random.seed(42)
    n = 200
    df = pd.DataFrame({
        'Tenure_Months': np.random.randint(1, 48, n),
        'Monthly_Spend': np.random.normal(75, 20, n).clip(15, 180),
        'Support_Calls': np.random.poisson(2, n),
        'Tier': np.random.choice(['Basic', 'Premium', 'Enterprise'], n),
        'Churn': np.random.choice([0, 1], n, p=[0.8, 0.2])
    })
    
    # 2. Static Dashboard Suite (Matplotlib + Seaborn)
    sns.set_theme(style='whitegrid')
    fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))
    
    # Plot 1: Distribution
    sns.histplot(df['Monthly_Spend'], kde=True, ax=axes[0, 0], color='steelblue')
    axes[0, 0].set_title("1. Spend Distribution (Right-Normal)", fontweight='bold')
    
    # Plot 2: Boxplot Group Comparison
    sns.boxplot(data=df, x='Tier', y='Monthly_Spend', palette='Set2', ax=axes[0, 1])
    axes[0, 1].set_title("2. Spend Distribution by Subscription Tier", fontweight='bold')
    
    # Plot 3: Scatter Relationship
    sns.scatterplot(data=df, x='Tenure_Months', y='Monthly_Spend', hue='Churn', palette='Set1', alpha=0.8, ax=axes[1, 0])
    axes[1, 0].set_title("3. Tenure vs Spend Colored by Churn", fontweight='bold')
    
    # Plot 4: Correlation Heatmap
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm', ax=axes[1, 1])
    axes[1, 1].set_title("4. Feature Correlation Matrix", fontweight='bold')
    
    fig.suptitle("Customer Analytics EDA Executive Dashboard", fontsize=15, fontweight='bold', y=0.99)
    fig.tight_layout()
    fig.savefig("day152_static_dashboard.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day152_static_dashboard.png")
    
    # 3. Interactive Dashboard (Plotly Express)
    fig_px = px.scatter(
        df, x='Tenure_Months', y='Monthly_Spend',
        color='Tier', size='Support_Calls',
        hover_data=['Churn'], title="Interactive Customer Segmentation Dashboard"
    )
    fig_px.write_html("day152_interactive_dashboard.html")
    print("Saved day152_interactive_dashboard.html")
    
    print("=== Phase 3 Visualization Mini Project Completed Successfully ===")

if __name__ == "__main__":
    main()
