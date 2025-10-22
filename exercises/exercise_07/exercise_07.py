# Exercise 7: Grade Calculator
# Objective: Convert numerical grade to letter grade

# Hint: Use if, elif, and else
# Hint: Check from highest grade to lowest
# Hint: Grade ranges: A(90+), B(80-89), C(70-79), D(60-69), F(0-59)

# Get grade from user

numerical = int(input("Enter your grade: "))

# Determine letter grade using if/elif/else

if numerical >= 90 and numerical <= 100:
    print(f'Your letter grade is A')
elif numerical >= 80 and numerical < 90:
    print(f'Your letter grade is B')
elif numerical >= 70 and numerical < 80:
    print(f'Your letter grade is C')
elif numerical >= 60 and numerical <70:
    print(f'Your letter grade is D')
elif numerical >= 0 and numerical <60:
    print(f'Your grade is F')
else:
    print(f'Invalid number')

# Print the letter grade
