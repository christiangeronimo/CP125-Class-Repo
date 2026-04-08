import pandas as pd

def promotion_candidates(filename):
    df = pd.read_csv(filename)
    
    # Calculate average performance (rounded to 1 decimal)
    avg_performance = round(df["PerformanceScore"].mean(), 1)
    
    # Minimum years required
    min_years = 2
    
    # Filter candidates
    candidates_df = df[
        (df["PerformanceScore"] > avg_performance) &
        (df["YearsOfService"] >= min_years)
    ]
    
    # Get candidate names
    candidate_names = set(candidates_df["EmployeeName"])
    
    # Count candidates
    candidate_count = len(candidate_names)
    
    # Return dictionary
    return {
        "average_performance": avg_performance,
        "min_years_required": min_years,
        "candidate_count": candidate_count,
        "candidate_names": candidate_names
    }

promotion_candidates ("labs/lab09/data/employees.csv")