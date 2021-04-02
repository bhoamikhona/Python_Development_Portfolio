# Greeting
print("Welcome to the tip calculator.")

# User input for total bill
total_bill = input("What was the toal bill? $")

# User input for tip percentage
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

# User input for number to people to split the bill between
number_of_people = input("How many people to split the bill? ")

# Calculation
bill_plus_tip = float(total_bill) + ((float(total_bill) * float(tip_percentage))/100)
individual_bill = round(bill_plus_tip / float(number_of_people), 2)
individual_bill = "{:.2f}".format(individual_bill)

# Printing the Result
print(f"Each person should pay: ${individual_bill}")
