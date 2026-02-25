def merge_results(existing, new_results):
    for student, score in new_results.items():
        if student in existing:
            existing[student] = max(existing[student], score)
        else:
            existing[student] = score
    return existing


def get_passing_students(scores, pass_mark):
    passing_names = [student for student, score in scores.items() if score >= pass_mark]
    return sorted(passing_names)


if __name__ == "__main__":
    # Example usage
    existing = {"Ali": 85, "Sara": 70}
    new_results = {"Ali": 90, "Ahmad": 60}

    merged = merge_results(existing, new_results)
    print("Merged Scores:", merged)
    print("Passing Students:", get_passing_students(merged, 75))