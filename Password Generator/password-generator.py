#Password Generator Project
import random

# List of Letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of Symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Greeting
print("Welcome to the PyPassword Generator!")

# User input for number of letters
nr_letters= int(input("How many letters would you like in your password?\n"))

# User input for number of symbols
nr_symbols = int(input(f"How many symbols would you like?\n"))

# User input for number of numbers
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Empty password list
password_list = []

# Appending random elements from the list (letters/numbers/symbols)
for i in range(nr_letters):
    ran = random.randint(0, len(letters) - 1)
    password_list.append(letters[ran])

for i in range(nr_numbers):
    ran = random.randint(0, len(numbers) - 1)
    password_list.append(numbers[ran])

for i in range(nr_symbols):
    ran = random.randint(0, len(symbols) - 1)
    password_list.append(symbols[ran])

# Shuffling the list
random.shuffle(password_list)

# Empty string
password = ""

# Converting password list to a string
for i in password_list:
    password = password + i

# Printing the result
print(password)
