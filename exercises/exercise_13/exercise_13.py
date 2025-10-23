# Exercise 13: String Manipulation
# Objective: Practice string methods and slicing

# Hint: String methods: .upper(), .lower(), .split()
# Hint: Slicing syntax: string[start:end:step]
# Hint: Reverse with [::-1], first N chars with [:N]
# Hint: Use 'in' operator to check if substring exists

# Get sentence from user

sentence = input("Enter a sentence: ")

# Display length

print(f'Length: {len(sentence)}')

# Display uppercase and lowercase

print(f'Uppercase: {sentence.upper()}')
print(f'Lowecase: {sentence.lower()}')

# Display word count (use .split())

print(f'Number of words: {len(sentence.split())}')

# Display reversed string

print(f'Reversed: {sentence[::-1]}')

# Display first 3 characters

print(f'First 3 characters: {sentence[:3]}')

# Check if contains 'python' (case-insensitive)

print(f'Contains Python: {"python" in sentence.lower()} ')

if "python" in sentence.lower():
    print(f'Contains Python: Yes')
else:
    print(f'Contains Python: No')
