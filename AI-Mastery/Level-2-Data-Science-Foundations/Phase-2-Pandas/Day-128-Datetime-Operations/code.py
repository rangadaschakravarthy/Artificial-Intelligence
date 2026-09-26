import pandas as pd
import numpy as np

def main():
    print("=== Day 128: Datetime Operations Demonstration ===")
    
    # 1. Sample Daily Time Series
    dates = pd.date_range('2023-01-01', periods=14, freq='D')
    np.random.seed(42)
    sales_values = [100, 110, 105, 120, 130, 125, 140, 150, 145, 160, 170, 165, 180, 190]
    
    df = pd.DataFrame({'Sales': sales_values}, index=dates)
    print("Raw Daily Dataset:
", df.head())
    
    # 2. Extract Date Components using .dt
    print("
--- 1. Feature Extraction (.dt) ---")
    df_reset = df.reset_index()
    df_reset['Day_Name'] = df_reset['index'].dt.day_name()
    df_reset['Is_Weekend'] = df_reset['index'].dt.dayofweek >= 5
    print(df_reset[['index', 'Sales', 'Day_Name', 'Is_Weekend']].head())
    
    # 3. Resampling (Daily to Weekly)
    print("
--- 2. Resampling (Weekly Sum) ---")
    weekly_sales = df.resample('W').sum()
    print(weekly_sales)
    
    # 4. Rolling Moving Average & Lag Features
    print("
--- 3. Rolling SMA and Lag Features ---")
    df['SMA_7'] = df['Sales'].rolling(window=7).mean()
    df['Sales_Lag_1'] = df['Sales'].shift(1)
    print(df.tail(8))

if __name__ == "__main__":
    main()
