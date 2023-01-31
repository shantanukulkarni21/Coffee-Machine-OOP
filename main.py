from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
available_items = Menu()
make_coffee = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    # Ask for user preference
    user_pref = input(f"What would you like? {available_items.get_items()} ")

    #Check if resources are sufficient for drinks
    if user_pref == "report":
        make_coffee.report()
        money_machine.report()
    elif user_pref == "off":
        is_on = False
    else:
        drink = available_items.find_drink(user_pref)
        if make_coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            make_coffee.make_coffee(drink)


