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
number = int(input("Enter a number: "))

# Checks if the given number is odd or even, then store to output variable.
output = f"{number} is an even number." if number % 2 == 0 else f"{number} is an odd number."

print(output) # Prints output
