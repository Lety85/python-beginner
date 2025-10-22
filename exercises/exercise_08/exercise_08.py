# Exercise 8: Multiplication Table
# Objective: Print multiplication table for a given number

# Hint: Use a for loop with range(1, 11)
# Hint: Loop syntax: for variable in range():
# Hint: Multiply the number by the loop variable

# Get number from user

number = int(input("Enter a number: "))

# Loop from 1 to 10 and print each multiplication

for i in range(1,11):
    print(f'{number} x {i} = {number * i}')
