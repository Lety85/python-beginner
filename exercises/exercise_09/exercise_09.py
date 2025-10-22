# Exercise 9: Sum of Numbers
# Objective: Calculate sum of numbers from 1 to N using while loop

# Hint: Initialize counter = 1 and total = 0
# Hint: While loop continues while counter <= n
# Hint: Add counter to total, then increment counter
# Hint: Use += operator for adding to a variable

# Get N from user

number = int(input("Enter a positive number: "))

# Initialize counter and total

total = 0
counter = 1

# Use while loop to calculate sum

while counter <= number:
    total += counter
    counter += 1

# Print the result

print(f'The sum of numbers from 1 to {number} is {total}')