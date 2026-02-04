def get_student_courses(enrollments, student_id):
    """Return set of courses this student has completed."""
    courses = set()
    for sid, course in enrollments:
        if sid == student_id:
            courses.add(course)
    return courses


def find_missing_courses(completed_courses, required_courses):
    """Return set of required courses not yet completed."""
    return required_courses - completed_courses


def build_student_report(students, enrollments, required_courses):
    """Return sorted list of tuples (missing_count, student_id) for students with missing courses."""
    report = []

    for student_id in students:
        completed = get_student_courses(enrollments, student_id)
        missing = find_missing_courses(completed, required_courses)
        if missing:
            report.append((len(missing), student_id))

    for i in range(len(report)):
        for j in range(i + 1, len(report)):
            if report[i][0] < report[j][0]:
                report[i], report[j] = report[j], report[i]
            elif report[i][0] == report[j][0] and report[i][1] > report[j][1]:
                report[i], report[j] = report[j], report[i]

    return report


def find_incomplete_students(enrollments, required_courses):
    students = set()
    for sid, course in enrollments:
        students.add(sid)

    return build_student_report(students, enrollments, required_courses)
