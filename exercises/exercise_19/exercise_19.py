# Exercise 19: Palindrome Checker
# Objective: Check if a word or phrase is a palindrome

# Hint: Remove spaces with .replace(" ", "")
# Hint: Convert to lowercase with .lower()
# Hint: Reverse string with [::-1]
# Hint: Compare cleaned string with its reverse
# Hint: For advanced: use .isalnum() to keep only letters/numbers

# Get input from user
text = input("Enter a word or phrase: ")

# Clean the text (remove spaces, convert to lowercase)
text_cleaned = text.replace(" ", "").lower()

# Check if palindrome (compare with reversed version)
if text_cleaned == text_cleaned[::-1]:
    print(f'"{text_cleaned}" is a palindrome!')
else:
    print(f'"{text_cleaned}" is not a palindrome.')

# Display result
