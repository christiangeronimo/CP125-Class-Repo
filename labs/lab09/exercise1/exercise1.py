import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)
    total_students = len(df)
    subjects = ["Math", "Science", "English"]
    math_average = round(df["Math"].mean(), 1)
    highest_math_student = df["Math"].max()
    
    
    
    result = pd.DataFrame({
    'Total Students': total_students,
    'Subjects': subjects,
    'Math Average': math_average,
    'Highest_math_student' : highest_math_student
})
    print(result)
    return result

result = explore_data("labs/lab09/data/students.csv")
    