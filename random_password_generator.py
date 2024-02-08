import random

random_password = r"""                                                                    
 _____           _              _____                             _ 
| __  |___ ___ _| |___ _____   |  _  |___ ___ ___ _ _ _ ___ ___ _| |
|    -| .'|   | . | . |     |  |   __| .'|_ -|_ -| | | | . |  _| . |
|__|__|__,|_|_|___|___|_|_|_|  |__|  |__,|___|___|_____|___|_| |___|
                                                                    
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Random Password Generator.")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

random_password = ""
# Easy Level - Order not randomized:
for _ in range(nr_letters):
    random_password += random.choice(letters)
for _ in range(nr_symbols):
    random_password += random.choice(symbols)
for _ in range(nr_numbers):
    random_password += random.choice(numbers)
print(f"Easy password: {random_password}")

# Hard Level - Order of characters randomized:
new_password = []

for char in random_password:
    new_password += char
random.shuffle(new_password)

final_password = ""
for char in new_password:
    final_password += char
print(f"Hard password: {final_password}")
