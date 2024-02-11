cipher_logo = r"""
 ____  ____  _____ ____  ____  ____    ____  _  ____  _     _____ ____ 
/   _\/  _ \/  __// ___\/  _ \/  __\  /   _\/ \/  __\/ \ /|/  __//  __\
|  /  | / \||  \  |    \| / \||  \/|  |  /  | ||  \/|| |_|||  \  |  \/|
|  \__| |-|||  /_ \___ || |-|||    /  |  \__| ||  __/| | |||  /_ |    /
\____/\_/ \|\____\\____/\_/ \|\_/\_\  \____/\_/\_/   \_/ \|\____\\_/\_\
                                                                       
"""


def caesar(process, message, count):
    hidden_message = ""
    for letter in message:
        if letter not in alphabet:
            hidden_message += str(letter)
        else:
            letter_code = alphabet.index(letter) + count if process == "encode" else alphabet.index(letter) - count
            letter_code %= len(alphabet)
            hidden_message += alphabet[letter_code]
    print(f"The {process}d message is: {hidden_message}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

proceed = True
print(cipher_logo)
while proceed:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(direction, text, shift)
    yes_no = input("Do you want to proceed? (Yes/No): ").lower()
    proceed = True if yes_no == 'yes' else False
else:
    print("Goodbye")
