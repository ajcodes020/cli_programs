import random
from resources import hangman_stages, word_list
import os

chosen_word = random.choice(word_list)
user_guess = []
user_life = 6

while user_life > 0:
    guess = input("\nGuess a letter: ").lower()
    os.system("cls")
    for letter in chosen_word:
        if guess == letter or letter in user_guess:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")
    if guess in chosen_word and len(guess) == 1:
        if guess not in user_guess:
            for _ in range(chosen_word.count(guess)):
                user_guess.append(guess)
        else:
            print(f"You already guessed the letter {guess}.")
    else:
        user_life -= 1
    print(hangman_stages[user_life])
    if len(user_guess) == len(chosen_word):
        print("\nYou won!")
        break
else:
    print(f"You have {user_life} life remaining. You lose! The word is: {chosen_word}")
