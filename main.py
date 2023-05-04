from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:

    available_items = menu.get_items()
    users_request = input(f"What would you like? {available_items}\n")

    if users_request == "off":
        is_on = False
    elif users_request == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(users_request)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

