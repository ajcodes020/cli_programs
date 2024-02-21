import random
import os


def evaluate(cards):
    """ Returns total value of cards """
    total = 0
    aces = 0
    for card in cards:
        total += card
        aces += 1 if card == 11 else 0
    while total > 21 and aces > 0:
        total -= 10
    return total


def blackjack():
    """ Starts/reset blackjack game"""
    single_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    random.shuffle(single_deck)
    player_cards = []
    computer_cards = []
    proceed = True
    while proceed:
        while len(player_cards) < 2:
            player_cards.append(single_deck.pop())
            computer_cards.append(single_deck.pop())
        print(f"Your cards: {player_cards}, current score: {evaluate(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}, current score: {computer_cards[0]}")
        while evaluate(player_cards) < 21:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                player_cards.append(single_deck.pop())
                print(f"Your cards: {player_cards}, current score: {evaluate(player_cards)}")
            else:
                while evaluate(computer_cards) < 17:
                    computer_cards.append(single_deck.pop())
                break
        print(f"Your final hand: {player_cards}, final score: {evaluate(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {evaluate(computer_cards)}")
        if evaluate(player_cards) > 21:
            print("You went over. You lose.")
        elif evaluate(computer_cards) > 21:
            print("Computer's hand is busted. You win.")
        elif evaluate(player_cards) > evaluate(computer_cards):
            print("Your cards are higher. You win.")
        elif evaluate(player_cards) == evaluate(computer_cards):
            print("Draw.")
        else:
            print("You lose.")
        should_continue = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
        if should_continue == 'y':
            os.system("cls")
            blackjack()
        else:
            proceed = False


blackjack()
