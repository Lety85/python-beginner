# Exercise 5: Temperature Converter
# Objective: Convert Celsius to Fahrenheit and Kelvin

# Hint: Use float() to convert input to decimal
# Hint: Fahrenheit formula: (C * 9/5) + 32
# Hint: Kelvin formula: C + 273.15
# Hint: Format with 2 decimals: f"{value:.2f}"

# Get temperature in Celsius from user

celsius = float(input("Enter the temperature in Celsius: "))

# Convert to Fahrenheit

fahrenheit = (celsius * 9/5) + 32

# Convert to Kelvin

kelvin = celsius + 273.15

# Display the results

print(f'{celsius}°C is equal to: \n{fahrenheit:.2f}°F (Fahrenheit) \n{kelvin:.2f} K (Kelvin)')