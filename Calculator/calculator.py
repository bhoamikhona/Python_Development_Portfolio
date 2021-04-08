#Calculator
from replit import clear
from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("First Number: "))
    for symbol in operations:
            print(symbol)

    continue_calculating = True

    while continue_calculating:

        operation_symbol = input("Select an Operation: ")
        num2 = float(input("Next Number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        to_be_continued = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if to_be_continued == 'y':
            num1 = answer
        else:
            continue_calculating = False
            clear()
            calculator()

calculator()