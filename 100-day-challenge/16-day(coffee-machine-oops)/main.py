###
# Espresso: 50ml water, 18g coffee | $1.50
# Latte: 200ml water, 24g coffee, 150ml milk | $2.50
# Cappuccino: 250ml water, 24 coffee, 100ml milk | $3.00
###

###
# constants...
ESPRESSO = {'name': 'Espresso', 'water': 50, 'coffee': 18, 'milk': 0, 'price': 1.50}
LATTE = {'name': 'Latte', 'water': 200, 'coffee': 24, 'milk': 150, 'price': 2.50}
CAPPUCCINO = {'name': 'Cappuccino', 'water': 250, 'coffee': 24, 'milk': 100, 'price': 3.00}
MAX_WATER_IN_ML = 300
MAX_MILK_IN_ML = 200
MAX_COFFEE_IN_GRAM = 100
COINS = {
    'Penny': 0.01,
    'Nickle': 0.05,
    'Dime': 0.10,
    'Quarter': 0.25
}

###
# variables...
started = True
milk = MAX_MILK_IN_ML
water = MAX_WATER_IN_ML
coffee = MAX_COFFEE_IN_GRAM
money = 0.0


###
# functions...
def print_report(display_cost=True):
    """prints available resources and money"""
    print('"""REPORT"""')
    print(f'Milk: {milk}ml')
    print(f'Water: {water}ml')
    print(f'Coffee: {coffee}g')
    if display_cost:
        print(f'Money: ${money}')


def return_coffee_details(coffee_no: int) -> object:
    if coffee_no == 1:
        return ESPRESSO
    elif coffee_no == 2:
        return LATTE
    elif coffee_no == 3:
        return CAPPUCCINO


def check_resources(coffee_no: int) -> bool:
    """validate if enough resources are available to prepare the coffee"""
    coffee_details = return_coffee_details(coffee_no)

    # True if resources are available else False
    return (
        milk >= coffee_details['milk']
        and water >= coffee_details['water']
        and coffee >= coffee_details['coffee']
    )


def pay(coffee_no: int):
    """add coins and return the changes"""
    price = return_coffee_details(coffee_no)['price']
    no_of_penny = int(input("How many penny? "))
    no_of_nickle = int(input("How many nickle? "))
    no_of_dime = int(input("How many dime? "))
    no_of_quarter = int(input("How many quarter? "))
    entered_amount = (
            COINS['Penny'] * no_of_penny
            + COINS['Nickle'] * no_of_nickle
            + COINS['Dime'] * no_of_dime
            + COINS['Quarter'] * no_of_quarter
    )

    if entered_amount < price:
        print('Less coins, money refunded!')
        return 0

    print(f"Change returned: {entered_amount - price}")

    return price


def prepare_coffee(coffee_no: int):
    """prepare coffee, deduct available resources"""
    coffee_details = return_coffee_details(coffee_no)
    print(f'Enjoy your {coffee_details["name"]}!')
    return coffee_details


while started:
    choice = input('What would you wish to do? (stop/report/coffee) ')
    if choice == 'stop':
        started = False
    elif choice == 'report':
        print_report()
    elif choice == 'coffee':
        coffee_type = int(input('Choose your coffee number: (1. espresso, 2. latte, 3. cappuccino) '))
        if check_resources(coffee_type):
            money += pay(coffee_type)
            coffee_resources = prepare_coffee(coffee_type)
            water -= coffee_resources['water']
            milk -= coffee_resources['milk']
            coffee -= coffee_resources['coffee']
        else:
            print("Insufficient resources...")
            print_report(display_cost=False)
    else:
        print('Invalid input, enter (stop/report/coffee)')
        exit(-1)
