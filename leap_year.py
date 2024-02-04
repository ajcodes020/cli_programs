print(r"""
       __-'==                                                                           _
  _--''__---/\_          _   _                     _    _             _  _             | |
  7         ,-.';       /|   |\                    |\   |\            /  |\            |_|
 (        ,- ",/         |___|  _   _    _         | \  |  _         /   |  _   _  ,_   _
 (-,  _--" ,-'           |   | / | | \  | \  / |   |  \ | /_\ / / |  \___|//_\ / | | ` / \
 \  \`; / /,_-          \|   |/\_|/|_/_/|_/_/\_|  \|   \| \__/\_\_|     /| \__/\_|/|   \_/
  \\  : \__-=-               '     |    |     /|        `              ( |
   \;-"-.                          |    |     \|                        \|
    | \                 
""")

print("This program will check if the year provided is a leap year or not.")

# Asks user for a year.
year = int(input("What year do you want to check? "))


def is_leap(year):
    """ returns True if year is a leap year, otherwise False """
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


print(f"{year} is a leap year.") if is_leap(year) else print(f"{year} is not a leap year.")
