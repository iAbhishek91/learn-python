import random


print("Welcome to the PyPassword Generator!")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '£', '$', '%', '^', '&', '*', '(', ')', '_']
available_combination = ['letters', 'numbers', 'symbols']

length = int(input("How many letters would you like in your password?"))
no_of_symbols = int(input("How many symbols would you like?"))
no_of_numbers = int(input("How many numbers would you like?"))


password = ''
for i in range(0, length):
    char_type = random.choice(available_combination)
    if char_type == 'symbols' and no_of_symbols > 0:
        no_of_symbols -= 1
        if no_of_symbols == 0: available_combination.remove('symbols')
        char = random.choice(symbols)
    elif char_type == 'numbers' and no_of_numbers > 0:
        no_of_numbers -= 1
        if no_of_symbols == 0: available_combination.remove('numbers')
        char = random.choice(numbers)
    else:
        if no_of_symbols + no_of_numbers >= length - i:
            char_type = random.choice(['numbers', 'symbols'])
            if no_of_symbols > 0 and char_type == 'symbols':
                no_of_symbols -= 1
                char = random.choice(symbols)
            if no_of_numbers > 0 and char_type == 'numbers':
                no_of_symbols -= 1
                char = random.choice(numbers)
        else:
            char = random.choice(letters)
    password = password + char

print(f"Your password is: {password}")

# Optional refactoring
# generate letters, digits and symbols in order
# then shuffle the list random.shuffle(x)
