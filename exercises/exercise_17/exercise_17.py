# Exercise 17: File Operations - Simple Note Taker
# Objective: Save and read notes from a file

# Hint: Use 'with open(filename, mode) as file:' syntax
# Hint: Mode 'a' appends, mode 'r' reads
# Hint: Use file.write() and file.readlines()
# Hint: Handle FileNotFoundError with try/except
# Hint: Use .strip() to remove newline characters

def add_note():
    # Get note from user
    note = input("Enter your note: ")
    # Open file in append mode and write note
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

    

def view_notes():
    # Try to open file in read mode
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
    # Read all lines and display them
        if notes:
            for index, note in enumerate(notes, 1):
                print(f'{index}. {note.strip()}')
        else:
            print("No notes yet")
    # Handle case when file doesn't exist
    except FileNotFoundError:
        print("No notes yet")
    

# Main program loop
while True: 
    print(f'\nSimple Note Taker')
    print("1. Add note")
    print("2. View note")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()
    
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

