import random

LEVELS = ['easy', 'hard']
HARD_ROUNDS = 6
EASY_ROUNDS = 10

# user input
level = input(f"Choose your level ({LEVELS}): ")

# random number between 0 - 100
number = random.randint(0, 100)

# calculate no_of_round, based on level
no_of_round = EASY_ROUNDS if level == 'easy' else HARD_ROUNDS



while no_of_round > 0:
    print(f"You have {no_of_round} round left!!")
    no_of_round -= 1

    guessed_no = int(input("Enter your guess (0 - 100): "))

    if guessed_no > number:
        print("Your guess is too HIGH!")
        continue
    elif guessed_no < number:
        print("Your guess is too LOW!")
        continue
    else:
        print('You Win')
        break

print(f'THE END: the number was {number}')
