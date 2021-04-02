# Imports
from replit import clear
from art import logo

# Printing Logo
print(logo)

# Initializing Variables
bidders = {}
more_bidders = True

while more_bidders == True:
    # User input for name
    name = input("What is your name?\n")
    
    # User input for bid
    bid = input("What is your bid?\n$")

    # Type conversion to int for value 'bid'
    bidders[name] = int(bid)

    # User input for more bidders
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    another_bidder.lower()

    clear()
    
    if another_bidder == "no":
        more_bidders = False

# Calculating highest bidder
max_bid = 0
max_bidder_name = ""
for name in bidders:
    if bidders[name] > max_bid:
        max_bid = bidders[name]
        max_bidder_name = name

# Printing the result
print(f"The winner is {max_bidder_name} with the bid of ${max_bid}.")
    
