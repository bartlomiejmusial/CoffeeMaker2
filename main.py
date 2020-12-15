from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from time import sleep

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    print("\n" * 100)
    print(logo)
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        print("\n" * 100)
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        sleep(5)
    elif choice == 'cappuccino' or choice == 'latte' or choice == 'espresso':
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost) and coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)
    else:
        print("\nWrong option! Try again.")
        sleep(5)
        continue
