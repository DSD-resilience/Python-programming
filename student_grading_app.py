# Student grading app.

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Empty dictionary to hold the final grades
student_grades = {}

# Grading logic
for student, score in student_scores.items():
    if 91 <= score <= 100:
        grade = "Outstanding"
    elif 81 <= score <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[student] = grade

# Output the final grades
print("Student Grades:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
