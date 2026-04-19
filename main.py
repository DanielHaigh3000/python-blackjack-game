import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def init ():
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    continue_game = True
    another_card = ''

    give_card(user_cards)
    give_card(user_cards)
    is_user_blackjack = check_blackjack(user_cards)
    give_card(computer_cards)
    give_card(computer_cards)
    is_computer_blackjack = check_blackjack(computer_cards)

    print(art.logo)

    show_cards('your', user_cards, 'current')
    show_cards('computer', computer_cards, 'current', True)

    if is_user_blackjack and not is_computer_blackjack:
        print("You got Blackjack! You win!")
        show_cards('your', user_cards, 'final')
        show_cards('computer', computer_cards, 'final', False)
        continue_game = False
    elif is_computer_blackjack:
        print("You lose! The computer got Blackjack.")
        show_cards('your', user_cards, 'final')
        show_cards('computer', computer_cards, 'final', False)
        continue_game = False
    else:
        another_card = ask_another_card()

    while continue_game:
        if another_card == 'y':
            give_card(user_cards)
            user_score = check_score(user_cards)
            if user_score > 21 and 11 in user_cards:
                # Change 11 to 1
                user_cards.remove(11)
                user_cards.append(1)
                user_score = check_score(user_cards)

            show_cards('your', user_cards, 'current')
            show_cards('computer', computer_cards, 'current', True)

            if user_score > 21:
                print("You went over 21. You lose.")
                show_cards('your', user_cards, 'final')
                show_cards('computer', computer_cards, 'final')
                continue_game = False
            else:
                another_card = ask_another_card()
        else:
            user_score = check_score(user_cards)
            computer_score = check_score(computer_cards)

            while computer_score < 17:
                give_card(computer_cards)
                computer_score = check_score(computer_cards)

            if computer_score > user_score and computer_score < 22:
                print("You lose!")
                show_cards('your', user_cards, 'final')
                show_cards('computer', computer_cards, 'final')
                continue_game = False
            elif computer_score == user_score:
                print("It's a draw!")
                show_cards('your', user_cards, 'final')
                show_cards('computer', computer_cards, 'final')
                continue_game = False
            else:
                print("You win!")
                show_cards('your', user_cards, 'final')
                show_cards('computer', computer_cards, 'final')
                continue_game = False

def give_card (cards_set):
    cards_set.append(random.choice(cards))

def check_blackjack (cards_set):
    return 11 in cards_set and 10 in cards_set

def check_score (cards_set):
    return sum(cards_set)

def show_cards (player, cards_set, status, hide_first = False):
    if hide_first:
        print(f"{player.capitalize()} cards: [?,{cards_set[1]}]")
    else:
        score = check_score(cards_set)
        print(f"{player.capitalize()} cards: [{','.join(map(str, cards_set))}], {status} score: {score}")

def ask_another_card ():
    is_correct_response = False
    new_card = ''
    while not is_correct_response:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if new_card == 'y' or new_card == 'n':
            is_correct_response = True
        else:
            print("Incorrect input. Please type 'y' or 'n'.")
    return new_card

def ask_new_game ():
    return input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ").lower()

# Run game at least once
while True:
    init()

    if ask_new_game() != 'y':
        print('Goodbye.')
        break