from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# The objects associated with the coffee making machine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
while is_on:
    # Get items to make
    item = menu.get_items()
    # Take input from the user
    drink_item = input(f"what drink do you need?{item} ")
    if drink_item == 'report':
        coffee_maker.report()
        money_machine.report()
    elif drink_item == 'off':
        is_on = False
    else:
        drink = menu.find_drink(drink_item)
        # This line of ocde takes care of the drink availabilty and money payed by the user
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            is_on = False








