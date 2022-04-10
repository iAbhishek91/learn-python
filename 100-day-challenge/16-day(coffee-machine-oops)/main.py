from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


command_name = ""
nero_menu = Menu()
nero_money_machine = MoneyMachine()
nero_coffee_maker = CoffeeMaker()


while command_name != "off":
    command_name = input(f"What would you like? ({nero_menu.get_items()}):")

    if command_name == "off":
        continue

    if command_name == "report":
        nero_coffee_maker.report()
        nero_money_machine.report()
        continue

    drinks_details = nero_menu.find_drink(command_name)
    if drinks_details is not None:
        if nero_coffee_maker.is_resource_sufficient(drinks_details):
            nero_money_machine.make_payment(drinks_details.cost)
            nero_coffee_maker.make_coffee(drinks_details)

print("Turning off the machine")
