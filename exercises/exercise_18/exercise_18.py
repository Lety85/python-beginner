# Exercise 18: Number Guessing Game
# Objective: Create a number guessing game with random numbers

# Hint: Use 'import random' at the top
# Hint: Generate random number: random.randint(1, 100)
# Hint: Use while True loop and break when guessed
# Hint: Track attempts with a counter variable
# Hint: Compare guess to secret number for hints

import random

def play_game():
    # Generate random number
    secret_number = random.randint(1,100)

    # Initialize attempts counter
    attempts = 0
    # Game loop - keep asking for guesses
    print("I'm thinking of a number between 1 and 100")

    while True:
        
        # Get user guess
        guess = int(input("Enter your guess: "))
        # Increment attempts
        attempts+=1
        # Compare and give feedback
        if guess > secret_number:
            print("Too high! Try again")
        elif guess < secret_number:
            print("Too low! Try again")
        else:
            print(f'Congratulations! You guessed it in {attempts} attempts')
            
        # Break when correct
            break

# Main program

# Welcome message
print("Welcome to the Number Guessing Game!")
# Main loop for playing multiple games
while True:
    play_game()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "no":
        print("Thanks for playing!")
        break
