from data import MENU, resources

system_running = True

def sufficient_resources(coffee_choice):
    """Returns true if the ingredients are sufficient and deducts the amount of ingredients needed to make the
    coffee. Otherwise, returns the ingredient which is not enough to make the coffee. """

    required_water = MENU[coffee_choice]["ingredients"]["water"]
    required_milk = MENU[coffee_choice]["ingredients"]["milk"]
    required_coffee = MENU[coffee_choice]["ingredients"]["coffee"]

    available_water = resources["water"]
    available_milk = resources["milk"]
    available_coffee = resources["coffee"]

    if required_water > available_water:
        return "water"
    elif required_milk > available_milk:
        return "milk"
    elif required_coffee > available_coffee:
        return "coffee"
    else:
        resources["water"] -= required_water
        resources["milk"] -= required_milk
        resources["coffee"] -= required_coffee
        resources["money"] += MENU[coffee_choice]["cost"]
        return "true"


def calculate(no_of_quarters, no_of_dimes, no_of_nickels, no_of_pennies):
    """Returns the total calculated from coins inserted."""
    quarter = 0.25 * no_of_quarters
    dime = 0.10 * no_of_dimes
    nickel = 0.05 * no_of_nickels
    penny = 0.01 * no_of_pennies

    total_paid = quarter + dime + nickel + penny

    return total_paid


while system_running:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if customer_choice == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        money = resources["money"]
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")

    elif customer_choice == "off":
        system_running = False

    elif customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":
        sufficient = sufficient_resources(customer_choice)

        if sufficient == "true":
            print("Please insert coins.")
            quarters = float(input("Quarters: "))
            dimes = float(input("Dimes: "))
            nickels = float(input("Nickels: "))
            pennies = float(input("Pennies: "))

            paid = calculate(quarters, dimes, nickels, pennies)

            coffee_cost = MENU[customer_choice]["cost"]

            if coffee_cost > paid:
                print("Sorry that is not enough money. Money Refunded.")
            else:
                money_change = paid - coffee_cost
                money_change = round(money_change, 2)
                print(f"Here is your change of ${money_change}")
                print(f"Here is your {customer_choice}, Enjoy!")

        else:
            print(f"Not Enough {sufficient}")
