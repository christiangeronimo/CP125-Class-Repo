import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)
    
    high_df = df[(df["Math"] > 85) & 
                 (df["Science"] > 85) & 
                 (df["Chemistry"] > 85) &
                 (df["Physics"] > 85) &
                 (df["English"] > 85)]
    
    names = set(high_df["Name"])

    count = len(names)
    
    return {
        "count": count,
        "names": names
    }