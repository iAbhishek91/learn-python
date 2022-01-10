import random
from blackJackArt import logo, cards_pattern, hidden_card

print(logo)
print('='*65)
print('='*65)

BLACK_JACK = 21
DEALER_THRESHOLD = 17

LABEL_A = cards_pattern('A')
LABEL_2 = cards_pattern('2')
LABEL_3 = cards_pattern('3')
LABEL_4 = cards_pattern('4')
LABEL_5 = cards_pattern('5')
LABEL_6 = cards_pattern('6')
LABEL_7 = cards_pattern('7')
LABEL_8 = cards_pattern('8')
LABEL_9 = cards_pattern('9')
LABEL_10 = cards_pattern('10')
LABEL_J = cards_pattern('J')
LABEL_Q = cards_pattern('Q')
LABEL_K = cards_pattern('K')


def removeAndReturnCard():
    cards = {
        'A': { 'cards': LABEL_A, 'value': 11}, 
        '2': { 'cards': LABEL_2, 'value' : 2,},
        '3': { 'cards': LABEL_3, 'value' : 3,},
        '4': { 'cards': LABEL_4, 'value' : 4,},
        '5': { 'cards': LABEL_5, 'value' : 5,},
        '6': { 'cards': LABEL_6, 'value' : 6,},
        '7': { 'cards': LABEL_7, 'value' : 7,},
        '8': { 'cards': LABEL_8, 'value' : 8,},
        '9': { 'cards': LABEL_9, 'value' : 9,},
        '10': { 'cards': LABEL_10, 'value' : 10,},
        'J': { 'cards': LABEL_J, 'value' : 10,},
        'Q': { 'cards': LABEL_Q, 'value' : 10,},
        'K': { 'cards': LABEL_K, 'value' : 10,},
    }
    card_label = random.choice([ x for x in cards ])
    cards_with_label = cards[card_label]['cards']
    card_label_value = cards[card_label]['value']

    selectedCard = random.choice(cards_with_label)
    cards_with_label.remove(selectedCard)

    return {
        'card': selectedCard,
        'value': card_label_value
    }


dealer_cards = []
player_cards = []

player_cards.append(removeAndReturnCard()) # first players card
dealer_cards.append(removeAndReturnCard()) # hidden dealers card
player_cards.append(removeAndReturnCard()) # second players card
dealer_cards.append(removeAndReturnCard()) # first dealer card
dealer_value = 0
player_value = 0


def displayIndividualInfo(individual_type: str, value = 0, is_display = True) -> int:
    individual_cards = []
    individual_value = value
    
    if individual_type == 'player':
        individual_cards = player_cards
    else:
        individual_cards = dealer_cards

    for card in individual_cards:
        if is_display: print (card['card'])
        individual_value += int(card['value'])

    if is_display:
        print(f"{individual_type.title()}'s value: {individual_value}")
        print('='*65)
    return individual_value


# Display dealers information
print(hidden_card)
print(dealer_cards[1]['card'])
print(f"Dealer's value: {dealer_cards[1]['value']}")
print('='*65)

# calculate dealers information
dealer_value = displayIndividualInfo(individual_type = 'dealer', is_display = False)

# calculate and Display players information
player_value = displayIndividualInfo(individual_type ='player')

# if dealer and player have blackjack, its a draw finish the game
if dealer_value == BLACK_JACK and player_value == BLACK_JACK:
    displayIndividualInfo('dealer')
    print('Surprising, both you and dealer have BLACKJACK!! Its a draw')
    # no money deducted from pot
# if dealer has blackjack, dealer win
elif dealer_value == BLACK_JACK:
        displayIndividualInfo('dealer')
        print("Dealer win!! - It's a BLACKJACK")
        # TODO: blackjack pot: money deducted
# if player has blackjack, player wins
elif player_value == BLACK_JACK:
        # double money is added to the pot
        print("You win!! - Its a BLACKJACK")
# start the game
else:
    # play loop
    while player_value < BLACK_JACK or dealer_value >= BLACK_JACK:
        player_choice = input('What would you like to do? (1.STAND, 2.HIT, 3.SPLIT, 4.DOUBLE, 5.SURRENDER): ').upper()
        if player_choice not in ["1" ,"2", "3", "4", "5", "STAND", "HIT", "SPLIT", "DOUBLE", "SURRENDER"]:
            print('Invalid input, game exiting!')
            exit(-1)
        
        if player_choice in ["STAND", "1"]:
            print("STAND/STICK/STAY selected, select no more cards and wait...")
            dealer_value = displayIndividualInfo(individual_type = 'dealer')
            player_value = displayIndividualInfo(individual_type = 'player')
            
            # if dealer needs to take another card
            while dealer_value < DEALER_THRESHOLD:
                print(f"Dealer's value is {dealer_value} which is < {DEALER_THRESHOLD}, picking a random card...")
                dealer_cards.append(removeAndReturnCard())
                dealer_value = displayIndividualInfo(individual_type = 'dealer', is_display = False)
            break

        if player_choice in ["HIT", "2"]:
            print("HIT selected, please take a random card from the deck...")
            player_cards.append(removeAndReturnCard())
            player_value = displayIndividualInfo(individual_type = 'player')

    dealer_value = displayIndividualInfo(individual_type = 'dealer')

    if player_value > dealer_value:
        if player_value <= BLACK_JACK:
            print('You win!!')
        else:
            print('Dealer win, you Busted!')
    elif dealer_value > player_value:
        if dealer_value <= BLACK_JACK:
            print('Dealer win!!')
        else:
            print('You win, dealer Busted!')
    else:
        print('Game draw -__-')