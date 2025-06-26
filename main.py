from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_maker.report()
money_machine.report()
turn_on = True
menu = Menu()
while turn_on:
    option = menu.get_items()
    print(option)
    turn_on = False