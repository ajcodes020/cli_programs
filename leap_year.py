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

# Checks if the given year is divisible by 4 or not.
if year % 4 == 0:

    # If the year is divisible by 400, it is a leap year (e.g., 2000).
    # If the year is divisible by 100 but not by 400, it is not a leap year (e.g., 1700).
    if year % 400 == 0:
        print(f"Year {year} is a leap year")
    elif year % 100 == 0:
        print(f"Year {year} is not a leap year")
    else:
        print(f"Year {year} is a leap year")

# If the year is not divisible by 4 without a remainder, then it is not a leap year.
else:
    print(f"Year {year} is not a leap year")
