import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: "))
print(rps[choice])
computer = random.randint(0, 2)
print(f"Computer chose: {rps[computer]}")

rock_condition = ["draw", "lose", "win"]
paper_condition = ["win", "draw", "lose"]
scissors_condition = ["lose", "win", "draw"]
outcome = [rock_condition, paper_condition, scissors_condition]
print(f"You {outcome[choice][computer]} against the computer.")
