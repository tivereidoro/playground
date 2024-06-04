#!/usr/bin/python3

# 100-91: A+    90-81: A    80-71:B+    70-61:B
# 60-51: C      50-41: D    40 below: F

def score_check(score):
    if score > 90:
        return 'A+'
    elif score > 80:
        return 'A'
    elif score > 70:
        return 'B+'
    elif score > 60:
        return 'B'
    elif score > 50:
        return 'C'
    elif score > 40:
        return 'D'
    else:
        return 'F'


students_scores = {
    'Ram': 92,
    'Tuva': 78,
    'Nelly': 56,
    'Ese': 41,
    'Osaretin': 99,
    'Bolu': 34
}

students_grades = {}
for i in students_scores:
    students_grades[i] = score_check(students_scores[i])
    # print(f"{i} scored {students_grades[i]}")

print(students_grades)
