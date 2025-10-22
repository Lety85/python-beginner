# Exercise 6: Even or Odd
# Objective: Determine if a number is even or odd

# Hint: Use the modulus operator (%) to check divisibility
# Hint: If number % 2 equals 0, it's even
# Hint: Use if/else statement structure

# Get number from user

number = int(input("Enter a number: "))

# Check if even or odd and print result

if number % 2 == 0:
    print(f'{number} is even.')
else:
    print(f'{number} is odd.')
