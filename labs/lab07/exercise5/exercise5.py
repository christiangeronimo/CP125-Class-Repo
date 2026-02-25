def find_at_risk_departments(departments, threshold):
    at_risk = []
    
    for dept, students in departments.items():
        total = 0
        below_count = 0
        
        # Nested loop over students
        for student, score in students.items():
            total += 1
            if score < threshold:
                below_count += 1
        
        if total > 0 and below_count > total / 2:
            at_risk.append(dept)
    
    return sorted(at_risk)


departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}

print(find_at_risk_departments(departments, 65))