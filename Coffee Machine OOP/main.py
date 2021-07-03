from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

system_running = True

while system_running:
    customer_order = input(f"What would you like? ({menu.get_items()}): ")

    if customer_order == "off":
        system_running = False
    elif customer_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_ordered = menu.find_drink(customer_order)
        if drink_ordered is not None:
            are_resources_sufficient = coffee_maker.is_resource_sufficient(drink_ordered)
            if are_resources_sufficient:
                paid_enough = money_machine.make_payment(drink_ordered.cost)
                if paid_enough:
                    coffee_maker.make_coffee(drink_ordered)
