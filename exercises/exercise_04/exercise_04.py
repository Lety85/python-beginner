# Exercise 4: User Input
# Objective: Get user input and perform calculations

# Hint: Use input("prompt") to get user input
# Hint: Convert age to integer using int()
# Hint: Current year is 2025

# Get user's name

# Get user's age (remember to convert to integer)

# Calculate birth year

# Print the personalized message

name = input("What's your name?")
age = int(input("How old are you?"))
current_year = 2025
birth_year = current_year - age

print(f'Hello, {name}! You are {age} years old and were born around {birth_year}')