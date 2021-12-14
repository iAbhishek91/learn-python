import random
import re
import hangmanArt
import hangmanWords

# welcome, print logo
print(hangmanArt.logo)

# import word list
list_of_word = hangmanWords.word_list

# randomly choose a word
chosen_word = random.choice(list_of_word)  # list_of_word[random.randint(0, len(list_of_word) - 1)]

# change the word with underscore
mask_word = ['_' for i in chosen_word]

# keep track of wrong guesses
allowed_wrong_guess = len(hangmanArt.stages) - 1
wrong_guess = 0

# game logic
while [x for x in mask_word if x == '_'] and allowed_wrong_guess > wrong_guess:
    # print the the word
    print("*" * 20)
    print(' '.join(mask_word))
    print("*" * 20)

    # input single letter from user
    guess = input("Guess a letter: ")

    # validate the letter
    if re.fullmatch(r"[a-z|A-Z]", guess, flags=0):
        guess = guess.lower()
    else:
        print("Wrong input! exiting the game...")
        exit(-1)

    # check if guess is one of the letter in the word
    is_guess_correct = False

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            mask_word[i] = guess
            is_guess_correct = True

    # increase wrong guess count
    if not is_guess_correct:
        wrong_guess += 1

    # print the current state of current hangman
    print(hangmanArt.stages[allowed_wrong_guess - wrong_guess])

print("*"*20)
print(f"THE WORD WAS: '{chosen_word}'")
print("*"*20)
if wrong_guess == allowed_wrong_guess:
    print("YOU LOST")
else:
    print("YOU WIN")
print("*"*20)
