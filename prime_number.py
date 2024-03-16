print("This program will check if a given integer number is a prime number.")

# Asks user for an integer number.
number = int(input("Enter an integer number: "))


def prime_checker(n):
    """ Returns True if given integer number is a prime number, else False """
    for i in range(2, n):
        if number % i == 0:
            return False
    else:
        return True


print(f"{number} is a prime number.") if prime_checker(number) else print(f"{number} is not a prime number.")
