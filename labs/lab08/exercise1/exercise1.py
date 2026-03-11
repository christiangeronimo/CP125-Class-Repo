def filter_passing_scores(input_file, output_file):
    f = open(input_file, 'r')
    out = open(output_file, 'w')

    count = 0

    while True:
        student_id = f.readline()
        if student_id == "":
            break

        student_id = student_id[:-1]

        score_line = f.readline()
        score = int(score_line[:-1])

        if score >= 80:
            out.write(student_id + " " + str(score) + "\n")
            count += 1

    f.close()
    out.close()

    return count


# Test
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", 
                               "labs/lab08/exercise1/data/passing.txt")
print("Number of passing students:", result)