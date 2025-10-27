# Exercise 4: User Input
# Objective: Get user input and perform calculations

# Hint: Use input("prompt") to get user input
# Hint: Convert age to integer using int()
# Hint: Current year is 2025

# Get user's name
name = input("What's your name?")
# Get user's age (remember to convert to integer)
age = int(input("How old are you?"))
# Calculate birth year
current_year = 2025
birth_year = current_year - age
# Print the personalized message
print(f'Hello, {name}! You are {age} years old and were born around {birth_year}')