import pandas as pd
import numpy as np

def main():
    print("=== Day 126: Pivot Tables & Melt Demonstration ===")
    
    # 1. Sample Transaction Dataset
    df = pd.DataFrame({
        'Year': [2022, 2022, 2023, 2023, 2022, 2023],
        'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
        'Category': ['Tech', 'Tech', 'Tech', 'Tech', 'Furniture', 'Furniture'],
        'Sales': [1000, 1500, 1200, 1800, 800, 950]
    })
    print("Raw Transaction Data:
", df)
    
    # 2. Basic Pivot Table
    print("
--- 1. Basic Pivot Table (Sales by Year & Region) ---")
    piv = df.pivot_table(index='Year', columns='Region', values='Sales', aggfunc='sum', fill_value=0)
    print(piv)
    
    # 3. Pivot Table with Margins
    print("
--- 2. Pivot Table with Totals (Margins) ---")
    piv_tot = df.pivot_table(index='Category', columns='Region', values='Sales', aggfunc='mean', margins=True)
    print(piv_tot)
    
    # 4. Wide to Long using pd.melt
    print("
--- 3. Unpivoting Wide Table (pd.melt) ---")
    wide_data = pd.DataFrame({
        'Country': ['USA', 'Canada'],
        'Q1_GDP': [500, 100],
        'Q2_GDP': [520, 105]
    })
    long_data = pd.melt(wide_data, id_vars=['Country'], value_vars=['Q1_GDP', 'Q2_GDP'], var_name='Quarter', value_name='GDP')
    print(long_data)

if __name__ == "__main__":
    main()
