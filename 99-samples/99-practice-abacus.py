import random
from time import sleep
from functools import reduce

operators = ['ADD', 'MUL']

operator = input("Enter the operation you wish to perform (ADD, MUL): ")
no_of_numbers = int(input(f"How many number you wish to {operator} (2 - 20)? "))
max_no_of_digits = int(input("Enter the max number of digits in each number(1 - 6): "))
is_negative_no_allowed = bool(str(input("Negative number allowed? (Y/N): ")).lower() == 'y')
sleep_time = int(input("delay(in seconds) in generating numbers(3 - 10): " ))

# input validity checks
if operator not in operators:
    print(f"Invalid operator, valid values {operators}. Process exiting...")
    exit(-1)

if not str(max_no_of_digits).isnumeric() and  (max_no_of_digits < 1 or max_no_of_digits > 6):
    print("Invalid max no of digits, valid values b/w 1 to 6. Process exiting...")
    exit(-1)

if no_of_numbers < 2 or no_of_numbers > 20:
    print("Invalid no of numbers, valid values b/w 2 to 20. Process exiting...")
    exit(-1)

if sleep_time < 4 or sleep_time > 10:
    print("Invalid sleep time, valid values b/w 3 to 10. Process exiting...")
    exit(-1)

# calculation lambdas
calculations = {
    'ADD': lambda a, b : a + b,
    'MUL': lambda a, b : a * b
}

# calculates the values
min_no = -(int("9"*max_no_of_digits)) if is_negative_no_allowed else 1
max_no = int("9"*max_no_of_digits)
numbers = []
wish_to_continue = 'Y'


while wish_to_continue == 'Y':
    # generate the numbers
    print('Generating numbers...')
    print("#"*40)
    count = no_of_numbers
    while count > 0:
        count -= 1
        numbers.append(random.randint(min_no, max_no))

    # print the numbers
    for number in numbers:
        print(number)
        sleep(sleep_time)

    # print the answer
    result = reduce(calculations[operator], numbers)
    print(f"Result is :", result)
    print("#"*40)

    # reset
    wish_to_continue = (input("Do you wish to continue with same input? (Y/N): ")).upper()
    count = no_of_numbers
    numbers = []

print("Session over!")
print("-"*40)