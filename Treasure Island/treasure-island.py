# ASCII Art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Greeting
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Left or Right
way = input("Which way do you want to go? (left/right): \n")

# Left
if way.lower() == "left":
    
    # Swim or Wait
    swim = input("You reached at the shore, would you like to swim or wait for a boat to cross-over? (swim/wait): \n")
    
    # Wait
    if swim.lower() == "wait":
    
        # Which Door
        door = input("The boat takes you to an island where you see three doors in front of you. The first one is red, second is blue, and the third is yellow. Which one would you like to enter? (red/blue/yellow): \n")
        
        # Red Door
        if door.lower() == "red":
            print("You encounter fire! You are burned into ashes. Game Over!")
            
        # Blue Door
        elif door.lower() == "blue":
            print("You are drowned in Tsunami. Game Over!")
            
        # Yellow Door
        else:
            print("Congratulations! You are now a Millionaire! You Won!")
    
    # Swim
    else:
        print("A poisonous snake bit you. You are dead. Game Over!")

# Right
else:
    print("You took the wrong turn into the darkness. You lost your way. Game Over!")
