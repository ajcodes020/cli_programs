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
year = int(input("What year do you want to check? "))

if year % 4 == 0:
    if year % 400 == 0:
        print(f"Year {year} is a leap year")
    elif year % 100 == 0:
        print(f"Year {year} is not a leap year")
    else:
        print(f"Year {year} is a leap year")
else:
  print(f"Year {year} is not a leap year")
