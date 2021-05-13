from art import logo, vs
from game_data import data
from random import choice
from replit import clear

# Game Logo
print(logo)

def format_data(data_choice):
    name = data_choice["name"]
    followers = data_choice["follower_count"]
    description = data_choice["description"]
    country = data_choice["country"]
    return [f"{name}, a {description}, from {country}.", followers]


def calculate(followers_A, followers_B):
    if followers_A > followers_B:
        return "A"
    else:
        return "B"

def game():
    
    choice_B = choice(data)
    continue_playing = True
    current_score = 0

    while continue_playing == True:

        choice_A = choice_B
        choice_B = choice(data)
        while choice_A == choice_B:
            choice_B = choice(data)

        formated_choice_A = format_data(choice_A)
        formated_choice_B = format_data(choice_B)

        print("Compare A: " + formated_choice_A[0])
        print(vs)
        print("Against B: " + formated_choice_B[0])

        correct_answer = calculate(formated_choice_A[1], formated_choice_B[1])

        player_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        if player_answer == correct_answer:
            clear()
            print(logo)
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
            continue_playing = False

game()