import pandas as pd

def main():
    # 1. Set and Reset Index
    df = pd.DataFrame({
        'ID': ['A1', 'A2', 'A3'],
        'Product': ['Phone', 'Tablet', 'Laptop'],
        'Price': [800, 500, 1200]
    })
    print("Original DataFrame:
", df)
    
    df_id = df.set_index('ID')
    print("
Indexed by ID:
", df_id)
    print("Is Index Unique?", df_id.index.is_unique)
    
    df_reset = df_id.reset_index()
    print("
Reset Index:
", df_reset)
    
    # 2. Filtering & Clean Reset
    filtered = df[df['Price'] > 600]
    print("
Filtered (Broken Index):
", filtered)
    print("Clean Reset (drop=True):
", filtered.reset_index(drop=True))

if __name__ == "__main__":
    main()
