print("This program will check if a given integer number is odd or even.")

# Asks user for an integer number.
number = int(input("Enter an integer number: "))


def is_even(n):
    """ Returns True if given integer number is even, else False """
    return True if n % 2 == 0 else False


print(f"{number} is an even number.") if is_even(number) else print(f"{number} is an odd number.")
