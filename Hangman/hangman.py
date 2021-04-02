# Imports
import random
import hangman_art
import hangman_words
from replit import clear

# Choose a word from word list
chosen_word = random.choice(hangman_words.word_list)

# Chosen Word's Length
word_length = len(chosen_word)

# Initial Variables
end_of_game = False
lives = 6
already_guessed = []

# Printing Hangman logo - ASCII Art
print(hangman_art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in already_guessed:
        print(f"Letter {guess} has already been guessed, try another one.")
    else:
        already_guessed.append(guess)

    # Check the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Letter {guess} is not in the word. Try another one.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # ASCII Art stages
    print(hangman_art.stages[lives])
