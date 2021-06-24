from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


flag = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while flag:
    options = menu.get_items()
    request = input(f"What would you like? ({options}):")

    if request == 'off':
        flag = False
    elif request == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



