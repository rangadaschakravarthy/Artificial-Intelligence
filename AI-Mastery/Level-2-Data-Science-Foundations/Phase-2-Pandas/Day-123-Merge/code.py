import pandas as pd
import numpy as np

def main():
    print("=== Day 123: Merge Demonstration ===")
    
    # 1. Sample Relational Tables
    customers = pd.DataFrame({
        'Cust_ID': [101, 102, 103, 104],
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'City': ['NY', 'SF', 'LA', 'NY']
    })
    
    orders = pd.DataFrame({
        'Order_ID': [5001, 5002, 5003, 5004],
        'Customer_ID': [101, 102, 101, 105],
        'Amount': [250.0, 180.0, 420.0, 95.0]
    })
    
    print("Customers Table:
", customers)
    print("
Orders Table:
", orders)
    
    # 2. Inner Join
    print("
--- 1. Inner Join ---")
    inner_df = pd.merge(customers, orders, left_on='Cust_ID', right_on='Customer_ID', how='inner')
    print(inner_df[['Cust_ID', 'Name', 'Order_ID', 'Amount']])
    
    # 3. Left Join
    print("
--- 2. Left Outer Join ---")
    left_df = pd.merge(customers, orders, left_on='Cust_ID', right_on='Customer_ID', how='left')
    print(left_df[['Cust_ID', 'Name', 'Order_ID', 'Amount']])
    
    # 4. Full Outer Join with Indicator
    print("
--- 3. Full Outer Join with Indicator ---")
    outer_df = pd.merge(customers, orders, left_on='Cust_ID', right_on='Customer_ID', how='outer', indicator=True)
    print(outer_df[['Cust_ID', 'Name', 'Order_ID', 'Amount', '_merge']])

if __name__ == "__main__":
    main()
