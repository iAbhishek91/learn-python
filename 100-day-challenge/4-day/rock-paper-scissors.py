# Game of rock, paper and scissors
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
label = ["ROCK", "PAPER", "SCISSORS"]
computer_choice = random.randint(0, 2)

print('*'*20)
print(f"Your choice: {label[choice]}, and Computer choice: {label[computer_choice]}")
print('*'*20)

if choice == computer_choice:
    result = "It's a draw"
elif choice == 0:
    if computer_choice == 1:
        result = "Computer wins"
    else:
        result = "You wins"
elif choice == 1:
    if computer_choice == 2:
        result = "Computer wins"
    else:
        result = "You wins"
elif choice == 2:
    if computer_choice == 0:
        result = "Computer wins"
    else:
        result = "You wins"

print(f"{result}!")
