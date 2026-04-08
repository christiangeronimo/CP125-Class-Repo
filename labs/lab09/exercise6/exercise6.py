import pandas as pd

def critical_inventory(filename):
    df = pd.read_csv(filename)
    
    total_products = len(df)
    
    # Correct column names
    critical_df = df[
        (df["StockLevel"] < df["ReorderThreshold"]) &
        (df["DaysSinceRestock"] > 30)
    ]
    
    # Use correct product column
    critical_products = set(critical_df["ProductName"])
    
    critical_count = len(critical_products)
    
    return {
        "total_products": total_products,
        "critical_count": critical_count,
        "critical_products": critical_products
    }


critical_inventory ("labs/lab09/data/inventory.csv")