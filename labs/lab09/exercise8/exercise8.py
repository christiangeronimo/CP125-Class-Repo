import pandas as pd
import matplotlib.pyplot as plt

def plot_subject_maximums(filename):
    df = pd.read_csv(filename)
    
    subjects = ["Math", "Science", "English", "Physics", "Chemistry"]
    

    max_scores = [df[subject].max() for subject in subjects]
    
    # Plot maximum scores
    plt.plot(subjects, max_scores)
    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")
    plt.title("Maximum Scores by Subject")
    plt.show()
    

    return len(df)

count = plot_subject_maximums("labs/lab09/data/students.csv")
print(count)