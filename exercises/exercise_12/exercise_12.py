# Exercise 12: Shopping List Manager
# Objective: Create an interactive shopping list program

# Hint: Use while True: for infinite loop, break to exit
# Hint: Use enumerate(list, 1) to get numbered items
# Hint: Check if list is empty with len(list) == 0
# Hint: Use list.pop(index) to remove by position

# Create empty shopping list

shooping_list = []

# Main program loop

while True:
    print(f'Shopping List Manager\n')
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item to add: ")
        shooping_list.append(item)
        print(f'{item} added to the list')

    elif choice == "2":
        if len(shooping_list) == 0:
            print("Your shopping list is empty")
        else:
            print(f'Your shopping list:\n')
            for index, item in enumerate(shooping_list,1):
                print(f'{index}. {item}')

    elif choice == "3":
        if len(shooping_list) == 0:
            print("Your shopping list is empty")
        else:
            print(f'Your shopping list:\n')
            for index, item in enumerate(shooping_list,1):
                print(f'{index}. {item}')

            item_rem = int(input("Enter item number to remove: "))
            if 1 <= item_rem <= len(shooping_list):
                removed_item = shooping_list.pop(item_rem - 1)
                print(f'{removed_item} removed from the list')
            else:
                print("Invalid item")

    elif choice == "4":
        print("Goodbye!")     
        break 

    else:
        print("Invalid choice. Please choose 1-4")

    


    # Display menu


    # Get user choice


    # Handle each option with if/elif/else
