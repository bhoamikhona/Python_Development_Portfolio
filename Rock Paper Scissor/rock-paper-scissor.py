import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of choices - rock, paper, scissors
choices = [rock, paper, scissors]

# User input for their choice
choice_made = input("What do you choose? Type 0 for Rock, 1 for Paper, or  2 for Scissors.\n")

your_choice = int(choice_made)

print("You Chose: \n")
print(choices[your_choice])

# Computer choice
integer = random.randint(0, 2)
computer_choice = choices[integer]

print("Computer Chose: \n")
print(computer_choice)

# Win/Lose/Draw Determination
if your_choice == integer:
    print("Draw!")
elif your_choice == 0 and integer == 1 or your_choice == 1 and integer == 2 or your_choice == 2 and integer == 0:
    print("You Lose!")
else:
    print("You Win!")
