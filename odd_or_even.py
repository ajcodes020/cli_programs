print(r"""
                       _                   
                      | |                  
 _ __  _   _ _ __ ___ | |__   ___ _ __ ___ 
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/ __|
| | | | |_| | | | | | | |_) |  __/ |  \__ \
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|  |___/
""")

print("This program will check if a given integer number is odd or even.")

# Asks user for an integer number.
number = int(input("Enter an integer number: "))


def is_even(n):
    """ return True if given integer number is even, otherwise False """
    return True if n % 2 == 0 else False


print(f"{number} is an even number.") if is_even(number) else print(f"{number} is an odd number.")
