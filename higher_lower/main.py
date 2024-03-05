import random
import os
from resources import game_vs, game_data


def compare(choice1, choice2):
    """ Returns True if first parameter has more followers """
    if choice1['follower_count'] > choice2['follower_count']:
        return True
    else:
        return False


random.shuffle(game_data)
score = 0
winner = ""
data_a = game_data.pop()
should_continue = True

while should_continue:
    os.system("cls")

    if score != 0:
        print(f"You guessed right. Score: {score}")
        print(winner)
    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}")
    print(game_vs)
    data_b = game_data.pop()
    print(f"Compare B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == 'A':
        if compare(data_a, data_b):
            score += 1
            winner = f"{data_a['name']} has {data_a['follower_count']} followers compared to {data_b['name']} with only {data_b['follower_count']} followers."
            data_a = data_b
        else:
            os.system("cls")
            print(f"{data_a['name']} only has {data_a['follower_count']} followers compared to {data_b['name']} with {data_b['follower_count']} followers.")
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    elif choice == 'B':
        if compare(data_b, data_a):
            score += 1
            winner = f"{data_a['name']} only has {data_a['follower_count']} followers compared to {data_b['name']} with {data_b['follower_count']} followers."
            data_a = data_a
        else:
            os.system("cls")
            print(f"{data_a['name']} has {data_a['follower_count']} followers compared to {data_b['name']} with only {data_b['follower_count']} followers.")
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    else:
        print("Not an option.")
