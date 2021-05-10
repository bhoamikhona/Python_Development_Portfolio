# Imports
from random import randint
from art import logo

# Logo & Greeting
print(logo)
print("Welcome to the Number Guessing Game!")

# Choosing a level of difficulty and initializing input_number of attempts
level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level_of_difficulty == 'hard':
    attempts = 5
else:
    attempts = 10

print(f"You have {attempts} attempts remaining to guess the input_number.")


chosen_number = randint(1, 100)

# Hint for testing the code
# print(f"Pssst, the correct answer is {chosen_number}")


print("I'm thinking of a input_number between 1 and 100.")

while attempts > 0:
    input_number = input("Make a guess: ")
    guessed_number = int(input_number)
    attempts -= 1

    if guessed_number == chosen_number:
        print(f"You got it! The answer was {chosen_number}")
        attempts = 0
    elif attempts == 0:
        print("You've run out of guesses, you lose.")
    else:
        if guessed_number > chosen_number:
            print("Too High.")
        else:
            print("Too Low.")

        print("Guess Again.")
        print(f"You have {attempts} attempts remaining to guess the input_number.")

