# Exercise 11: List Operations
# Objective: Practice creating and manipulating lists

# Hint: Create list with square brackets: list = ['item1', 'item2']
# Hint: Use .append() to add, .remove() to delete
# Hint: Use .sort() to sort, len() to get length

# Create a list of 5 favorite fruits

fruits = ["strawberry", "melon", "banana", "grape", "apple"]

# Display original list

print(f'Original list of fruits: {fruits}')

# Add two more fruits

fruits.append("watermelon")
fruits.append("lemon")
print(f'List of fruits after adding: {fruits}')

# Remove a fruit

fruits.remove("apple")
print(f'List of fruits after removing: {fruits}')

# Sort the list

fruits.sort()
print(f'Sorted list of fruits: {fruits}')

# Display final list and length

print(f'Total fruits {len(fruits)}')