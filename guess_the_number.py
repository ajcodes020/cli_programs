import random


def guess_the_number():
    """ starts the game """
    print("Welcome to Guess the Number.")
    print("A random number between 1 and 100 is generated.")
    random_number = random.randint(1, 100)
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
    remaining_tries = 10 if difficulty == 'easy' else 5

    while remaining_tries > 0:
        print(
            f"You have {remaining_tries} attempts remaining to guess the number."
        )
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print("You win.")
            break
        elif guess > random_number:
            print("Too high.")
            remaining_tries -= 1
        else:
            print("Too low.")
            remaining_tries -= 1


guess_the_number()
