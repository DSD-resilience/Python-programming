import random
# random number generator

# random_integer = random.randint(4,13)
# print(random_integer)

# another_random_number = random.random()
# print(another_random_number)

# A coin flip would look like this:
#coin_flip = random.binomialvariate(2,0.5)
#if coin_flip == 1 :
    #print("The coin is heads.")
#else :
    #print("The coin is tails.")

# but what are methods anyway?
# lists, data types, variables... basically everything is an object.
# a method is something an object can DO
#"Hey object, do this action! upper case! lower case! extend!"
# object.method()

import random

# ASCII Art
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
---'    ____)____
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

# List of choices
choices = [rock, paper, scissors]

# Mapping choice to name
choice_names = ["Rock", "Paper", "Scissors"]

# Get user's choice
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

# Validate input
if user_input < 0 or user_input > 2:
    print("Invalid number. You lose!")
else:
    print(f"\nYou chose {choice_names[user_input]}:")
    print(choices[user_input])

    # Computer choice
    computer_input = random.randint(0, 2)
    print(f"Computer chose {choice_names[computer_input]}:")
    print(choices[computer_input])

    # Determine winner
    if user_input == computer_input:
        print("It's a draw!")
    elif (user_input == 0 and computer_input == 2) or \
         (user_input == 1 and computer_input == 0) or \
         (user_input == 2 and computer_input == 1):
        print("You win!")
    else:
        print("You lose!")

