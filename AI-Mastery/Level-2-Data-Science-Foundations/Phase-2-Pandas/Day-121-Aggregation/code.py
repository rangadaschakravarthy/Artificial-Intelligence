import pandas as pd
import numpy as np

def main():
    print("=== Day 121: Aggregation Demonstration ===")
    
    # 1. Sample Dataset
    df = pd.DataFrame({
        'Category': ['Tech', 'Tech', 'Tech', 'Furniture', 'Furniture', 'Tech'],
        'Product': ['Laptop', 'Mouse', 'Monitor', 'Desk', 'Chair', 'Keyboard'],
        'Sales': [1200, 25, 300, 450, 150, 80],
        'Rating': [4.8, 4.2, 4.5, 4.0, 3.8, 4.1]
    })
    
    # 2. Multi-Function Aggregation on Column
    print("
--- 1. Multi-Function Aggregation ---")
    sales_stats = df.groupby('Category')['Sales'].agg(['min', 'mean', 'max', 'sum'])
    print(sales_stats)
    
    # 3. Dictionary-Based Aggregation
    print("
--- 2. Dictionary Aggregation ---")
    dict_agg = df.groupby('Category').agg({
        'Sales': ['sum', 'mean'],
        'Rating': 'max'
    })
    print(dict_agg)
    
    # 4. Named Aggregation (Flat Columns)
    print("
--- 3. Named Aggregation ---")
    named_agg = df.groupby('Category').agg(
        Total_Revenue=('Sales', 'sum'),
        Average_Rating=('Rating', 'mean'),
        Product_Count=('Product', 'count')
    )
    print(named_agg)

if __name__ == "__main__":
    main()
