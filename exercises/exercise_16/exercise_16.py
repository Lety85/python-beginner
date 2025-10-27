# Exercise 16: List Comprehensions
# Objective: Practice creating lists using comprehensions

# Hint: Basic syntax: [expression for item in iterable]
# Hint: With filter: [expression for item in iterable if condition]
# Hint: Example: [x*2 for x in range(5)] creates [0, 2, 4, 6, 8]

# 1. Create list of squares from 1 to 10

squares = [x**2 for x in range(1,11)]
print(f'Squares: {squares}')

# 2. Create list of even numbers from 1 to 20

even = [x for x in range(1,21) if x % 2 == 0]
print(f'Even numbers: {even}')

# 3. Get sentence and create list of word lengths
#The quick brown fox jumps

sentence = input("Enter a sentence: ")
sentence_split = sentence.lower().split()

word_lengths = [len(word) for word in sentence_split]

print(f'Word lengths: {word_lengths}')

# 4. Create list of uppercase words (only words > 3 chars)

long_words = [word.upper() for word in sentence_split if len(word) > 3]

print(f'Long words (uppercase): {long_words}')