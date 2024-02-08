print(r"""
                         _____________________
                        |  _________________  |
  _______ _             | | TIP          0. | |
 |__   __(_)            | |_________________| |
    | |   _ _ __        |  ___ ___ ___   ___  |
    | |  | | '_ \       | | 7 | 8 | 9 | | + | |
    | |  | | |_) |      | |___|___|___| |___| |
    |_|  |_| .__/       | | 4 | 5 | 6 | | - | |
           | |          | |___|___|___| |___| |
           |_|          | | 1 | 2 | 3 | | x | |
                        | |___|___|___| |___| |
                        | | . | 0 | = | | / | |
                        | |___|___|___| |___| |
                        |_____________________|
""")
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = tip * .01 + 1
total_bill = "{:.2f}".format(bill / people * tip, 2)

print(f"Each person should pay: ${total_bill}")
