############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Code #####################

from replit import clear
from random import choice
from art import logo


"""Returns a random card from the Deck."""
def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

"""Take a list of cards and return the sum calculated from the cards."""
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

"""Compares and returns the result."""
def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You Lose, Opponent has a BlackJack!"
    elif player_score == 0:
        return "You Win, You have a BlackJack!"
    elif player_score > 21:
        return "You Lose, You went over 21!"
    elif computer_score > 21:
        return "You Win, Opponent went over 21!"
    elif player_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"

def blackjack():
    
    print(logo)

    player_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score > 21 or player_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_should_deal == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    blackjack()