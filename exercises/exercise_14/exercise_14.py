# Exercise 14: Student Grade Book
# Objective: Use dictionaries to store and manage student grades

# Hint: Create dictionary: grades = {"name": score}
# Hint: Use .items() to get both key and value
# Hint: Use .values() to get all values
# Hint: Use max(dict, key=dict.get) to find key with max value
# Hint: Check if key exists with: if key in dict:

# Create grade book with at least 3 students

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Display all students and grades

print(f'Grade Book: ')
for name, grade in grades.items():
    print(f'{name} : {grade}')

# Calculate and display average grade

average = sum(grades.values())/ len(grades.values())
print(f'Average grade: {average}')

# Find and display top student

top_student = max(grades, key = grades.get)
top_grade = grades[top_student]
print(f'Top student: {top_student} with grade {top_grade}')

# Look up a specific student's grade

students_name = input("Enter student name to look up: ")

if students_name in grades:
    print(f"{students_name}'s grade: {grades[students_name]}")
else:
    print("The student is not in the diccionary")