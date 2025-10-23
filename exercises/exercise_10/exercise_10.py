# Exercise 10: Simple Calculator Function
# Objective: Create calculator using functions

# Hint: Define functions with def function_name(parameters):
# Hint: Use return to send back the result
# Hint: Call functions by passing values: result = add(5, 3)

# Define the four functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Get user input

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation(+, -, *, /): ")

# Use if/elif to call the appropriate function

if operation == "+":
    result = add(number1, number2)
elif operation == "-":
    result = subtract(number1, number2)
elif operation == "*":
    result = multiply(number1, number2)
elif operation == "/":
    result = divide(number1, number2)
else:
    result = None
    print("Invalid operation")

# Display the result

if result is not None:
    print(f'Result: {number1} {operation} {number2} = {result}')