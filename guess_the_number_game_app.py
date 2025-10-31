import random

def print_ascii_art():
    art = r"""
  _____                     _               _             
 |  __ \                   | |             | |            
 | |  \/ __ _ ___ ___   __| | ___  _ __   | |_ ___  _ __ 
 | | __ / _` / __/ __| / _` |/ _ \| '_ \  | __/ _ \| '__|
 | |_\ \ (_| \__ \__ \| (_| | (_) | | | | | || (_) | |   
  \____/\__,_|___/___(_)__,_|\___/|_| |_|  \__\___/|_|   

                Welcome to the Guess the Number Game!
    """
    print(art)

def guess_the_number():
    print_ascii_art()
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range 1 to 100.")
            elif guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts. 🎉")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

guess_the_number()

