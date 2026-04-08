import pandas as pd
import matplotlib

matplotlib.use('Agg') 

import matplotlib.pyplot as plt

def compare_subject_distributions(filename):
    df = pd.read_csv(filename)
    
    plt.hist(df['Math'], bins=10, alpha=0.5, label="Math")
    plt.hist(df['Science'], bins=10, alpha=0.5, label="Science")
    plt.hist(df['English'], bins=10, alpha=0.5, label="English")
    
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.title("Score Distribution Comparison")
    plt.legend()
    
    plt.show() 
    
    return len(df)

count = compare_subject_distributions("labs/lab09/data/students.csv")
print(count)