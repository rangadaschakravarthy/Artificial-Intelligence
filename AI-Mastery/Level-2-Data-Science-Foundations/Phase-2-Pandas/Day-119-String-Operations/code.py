import pandas as pd
import numpy as np

def main():
    # 1. Clean Casing & Whitespace
    raw_s = pd.Series(['  apple ', 'BANANA ', ' Cherry  ', np.nan])
    clean_s = raw_s.str.strip().str.lower()
    print("Raw Series:
", raw_s)
    print("
Cleaned Series:
", clean_s)
    
    # 2. Currency Text Cleaning
    prices = pd.Series(['$1,200.00', '$45.50', 'N/A'])
    numeric_p = pd.to_numeric(
        prices.str.replace('$', '', regex=False).str.replace(',', '', regex=False),
        errors='coerce'
    )
    print("
Cleaned Numeric Prices:
", numeric_p)
    
    # 3. String Splitting & Expand
    names = pd.Series(['Alice Smith', 'Bob Jones'])
    df_names = names.str.split(' ', expand=True)
    df_names.columns = ['First', 'Last']
    print("
Split Name DataFrame:
", df_names)
    
    # 4. Regex Domain Extraction
    emails = pd.Series(['alice@gmail.com', 'bob@yahoo.org'])
    domains = emails.str.extract(r'@([\w\.]+)')
    print("
Extracted Email Domains:
", domains)

if __name__ == "__main__":
    main()
