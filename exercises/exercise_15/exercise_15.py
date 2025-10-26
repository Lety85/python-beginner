# Exercise 15: Word Frequency Counter
# Objective: Count how many times each word appears in a sentence

# Hint: Convert to lowercase with .lower()
# Hint: Split into words with .split()
# Hint: Use dictionary to store word: count pairs
# Hint: Use dict.get(key, 0) to safely get current count
# Hint: Use max(dict, key=dict.get) to find most common

# Get sentence from user

sentence = input("Enter a sentence: ")
#The quick brown fox jumps over the lazy dog and the fox ran away

# Convert to lowercase and split into words

lower_sentence = sentence.lower()
split_sentence = sentence.lower().split()
print(lower_sentence)
print(split_sentence)

# Count word frequencies using a dictionary

dictionary = {}

for word in split_sentence:
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word] = 1

# Display all word frequencies

print(f'Word frequencies:\n')

for key, element in dictionary.items():  
    print(f'{key}: {element}')

# Find and display most common word

most_common = max(dictionary, key=dictionary.get)
max_count = dictionary[most_common]
print(f'\nMost common word: \"{most_common}\" (appears {max_count} times)')