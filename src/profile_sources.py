from pathlib import Path
import pandas as pd

RAW = Path("data/raw")

customers = pd.read_csv(RAW / "customers.csv")
orders = pd.read_json(RAW / "orders.json")
products = pd.read_parquet(RAW / "products.parquet")

for name, df in {
    "customers.csv": customers,
    "orders.json": orders,
    "products.parquet": products,
}.items():
    
    print(f"\nProfiling: {name}")
    
    file_path = RAW / name
    if file_path.exists():
        size_kb = file_path.stat().st_size / 1024
        print(f"File Size: {size_kb:.2f} KB")
    else:
        print("File Size: [File not found locally]")

    print(f"Shape (Rows, Columns): {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nMissing/Null Values:")
    print(df.isna().sum())
    
    hashable_df = df.astype(str)
    
    print(f"\nFully Duplicated Rows: {hashable_df.duplicated().sum()}")
    
    print("\nDistinct Values (Nunique):")
    print(hashable_df.nunique())
    
    print("\nFirst 5 Records:")
    print(df.head())
    
    print("\nNumeric Columns (Min / Max):")
    numeric_cols = df.select_dtypes(include='number').columns
    if not numeric_cols.empty:
        for col in numeric_cols:
            print(f" {col}: Min = {df[col].min()}, Max = {df[col].max()}")
    else:
        print(" No numeric columns found.")

    print("\nDate/Time Columns (Earliest / Latest):")
    has_date = False
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            print(f" {col}: Earliest = {df[col].min()}, Latest = {df[col].max()}")
            has_date = True
        elif df[col].dtype == 'object' or pd.api.types.is_string_dtype(df[col]):
            try:
                parsed_dates = pd.to_datetime(df[col], errors='coerce')
                if parsed_dates.notna().sum() > (df[col].notna().sum() * 0.5) and parsed_dates.notna().sum() > 0:
                    print(f" {col} (Parsed): Earliest = {parsed_dates.min()}, Latest = {parsed_dates.max()}")
                    has_date = True
            except Exception:
                pass
                
    if not has_date:
        print(" No date/time columns found.")