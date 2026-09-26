import pandas as pd
import numpy as np
import io

def main():
    # 1. Simulate CSV Data with Custom Delimiter and Sentinel NaNs
    raw_csv = "ID|Department|Salary|Bonus\n101|Engineering|85000.0|-999\n102|Marketing|N/A|5000.0\n103|Engineering|92000.0|7500.0\n104|Sales|60000.0|-999"

    # Parse with custom parameters
    df = pd.read_csv(
        io.StringIO(raw_csv),
        sep='|',
        na_values=['-999', 'N/A'],
        dtype={'ID': 'int32', 'Salary': 'float32'}
    )
    
    print("Parsed DataFrame:
", df)
    print("
Data Types:
", df.dtypes)
    print("
Missing Value Count:
", df.isna().sum())
    
    # 2. Chunked Reading Demonstration
    print("
--- Chunked Reading Demo ---")
    chunk_csv = "Val\n1\n2\n3\n4\n5\n6"
    for i, chunk in enumerate(pd.read_csv(io.StringIO(chunk_csv), chunksize=3)):
        print(f"Chunk {i+1} sum:", chunk['Val'].sum())

if __name__ == "__main__":
    main()
